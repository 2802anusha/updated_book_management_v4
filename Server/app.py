from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import pyodbc
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-secret-key-change-me')
jwt = JWTManager(app)

def get_db_connection():
    conn = pyodbc.connect(
        f"DRIVER={{{os.getenv('MSSQL_DRIVER', 'ODBC Driver 17 for SQL Server')}}};"
        f"SERVER={os.getenv('MSSQL_SERVER', 'mssql-container')};"
        f"DATABASE={os.getenv('MSSQL_DATABASE', 'books_db')};"
        f"UID={os.getenv('MSSQL_USERNAME', 'sa')};"
        f"PWD={os.getenv('MSSQL_PASSWORD', 'YourStrong@Passw0rd')};"
        f"TrustServerCertificate={os.getenv('MSSQL_TRUST_CERT', 'yes')};"
    )
    return conn

def validate_book_payload(payload):
    if not request.is_json or payload is None:
        return "Request must be JSON"
    if "cost" not in payload and "Cost" in payload:
        payload["cost"] = payload["Cost"]
    required_fields = ("publisher", "name", "date", "cost")
    for field in required_fields:
        if field not in payload:
            return f"Missing field: {field}"
        if payload[field] in (None, ""):
            return f"Missing field: {field}"
    try:
        float(payload["cost"])
    except (TypeError, ValueError):
        return "Invalid cost"
    try:
        datetime.strptime(payload["date"], "%Y-%m-%d")
    except (TypeError, ValueError):
        return "Invalid date format"
    return None

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    if cursor.fetchone():
        cursor.close()
        conn.close()
        return jsonify({"error": "Username already exists"}), 409
    password_hash = generate_password_hash(password)
    cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (username, password_hash))
    conn.commit()
    cursor.execute("SELECT @@IDENTITY AS id")
    user_id = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify({"message": "User created successfully", "user_id": int(user_id)}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        return jsonify({"error": "Bad credentials"}), 401
    if not check_password_hash(user[1], password):
        return jsonify({"error": "Bad credentials"}), 401
    access_token = create_access_token(identity=str(user[0]))
    return jsonify({"access_token": access_token}), 200

@app.route('/', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, publisher, name, date, cost FROM book")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify([
        {"id": row[0], "publisher": row[1], "name": row[2], "date": str(row[3]), "cost": row[4]}
        for row in rows
    ])

@app.route('/create', methods=['POST'])
@jwt_required()
def create_books():
    new_book = request.get_json(silent=True)
    validation_error = validate_book_payload(new_book)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO book (publisher, name, date, cost) VALUES (?, ?, ?, ?)",
        (new_book['publisher'], new_book['name'], new_book['date'], new_book['cost'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(new_book), 201

@app.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_book(id):
    updated_book = request.get_json(silent=True)
    validation_error = validate_book_payload(updated_book)
    if validation_error:
        return jsonify({"error": validation_error}), 400
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE book SET publisher=?, name=?, date=?, cost=? WHERE id=?",
        (updated_book['publisher'], updated_book['name'], updated_book['date'], updated_book['cost'], id)
    )
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"data": updated_book})

@app.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_book(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM book WHERE id=?", (id,))
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Book not found"}), 404
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Book deleted successfully'})

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
