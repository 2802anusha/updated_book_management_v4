# 📚 Book Management System - Complete Setup Guide

A full-stack **Book Management CRUD application** with React frontend, Flask backend, JWT authentication, and Docker containerization.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Prerequisites](#prerequisites)
5. [Installation & Setup](#installation--setup)
   - [Linux Setup](#linux-setup)
   - [Windows Setup](#windows-setup)
6. [Database Configuration](#database-configuration)
7. [Docker Setup](#docker-setup)
8. [Running the Application](#running-the-application)
9. [API Endpoints](#api-endpoints)
10. [Testing](#testing)
11. [JWT Authentication](#jwt-authentication)
12. [Troubleshooting](#troubleshooting)
13. [Development Workflow](#development-workflow)

---

## 🎯 Overview

This application allows users to:

- ✅ **Create** — Add new books to the inventory
- ✅ **Read** — View all books with details
- ✅ **Update** — Edit existing book information
- ✅ **Delete** — Remove books from the system
- 🔐 **JWT Authentication** — Secure login/signup
- 📊 **Testing** — Automated tests with Playwright and Pytest
- 🐳 **Containerization** — Full Docker support

### CRUD Operations

| Operation | HTTP Method | Endpoint | Description |
|-----------|-------------|----------|-------------|
| Create | POST | `/create` | Add a new book |
| Read (All) | GET | `/` | Fetch all books |
| Read (One) | GET | `/<id>` | Fetch specific book |
| Update | PUT | `/update/<id>` | Edit a book |
| Delete | DELETE | `/delete/<id>` | Remove a book |

---

## 🛠️ Tech Stack

### Frontend
- **React** (v18.3.1) — UI framework
- **Vite** (v5.3.4) — Build tool & dev server
- **Bootstrap** (v5.3.3) — CSS framework
- **Axios** (v1.7.7) — HTTP client
- **React Router** (v6.27.0) — Client-side routing
- **Playwright** (v1.56.0) — E2E testing framework
- **ESLint** — Code linting

### Backend
- **Flask** (v3.0.0) — Python web framework
- **Flask-CORS** (v4.0.0) — Cross-origin support
- **Flask-JWT-Extended** (v4.6.0+) — JWT authentication
- **Flasgger** (v0.9.7.1) — API documentation
- **psycopg2** (v2.9.10) — PostgreSQL adapter
- **PyODBC** — ODBC database connectivity
- **Pytest** (v7.4.3) — Testing framework
- **Pandas** & **NumPy** — Data analysis

### Database
- **SQLite** — Development database (file-based)
- **PostgreSQL** — Production database (optional)
- **MSSQL** — Alternative production database (optional)

### DevOps
- **Docker** — Containerization
- **Docker Compose** — Multi-container orchestration
- **Python 3.11** (Flask container)
- **Node.js 18** (React container)

---

## 📁 Project Structure

```
simple_book_management_may_2026/
├── Client/                              # React Frontend
│   ├── src/
│   │   ├── App.jsx                      # Main app component
│   │   ├── main.jsx                     # React entry point
│   │   ├── Books.jsx                    # List all books
│   │   ├── CreateBook.jsx               # Add new book form
│   │   ├── UpdateBook.jsx               # Edit book form
│   │   ├── Login.jsx                    # JWT login page
│   │   ├── Signup.jsx                   # JWT signup page
│   │   └── Nav.jsx                      # Navigation component
│   ├── tests/                           # Playwright E2E tests
│   │   ├── app.spec.js
│   │   ├── books.spec.js
│   │   ├── complete-flow.spec.js
│   │   ├── create-book.spec.js
│   │   └── update-book.spec.js
│   ├── public/                          # Static assets
│   ├── Dockerfile                       # Frontend container
│   ├── package.json                     # Node dependencies
│   ├── vite.config.js                   # Vite configuration
│   ├── playwright.config.js             # Playwright config
│   ├── eslint.config.js                 # ESLint rules
│   └── index.html                       # HTML template
│
├── Server/                              # Flask Backend
│   ├── app.py                           # Main Flask app
│   ├── mssql_app.py                     # MSSQL variant
│   ├── tests/
│   │   ├── pytest/
│   │   │   ├── test_books_api.py        # API unit tests
│   │   │   └── conftest.py              # Pytest configuration
│   │   ├── postman_newman/
│   │   │   ├── run-newman-tests.sh      # Newman test runner
│   │   │   ├── book_api_postman_collection.json
│   │   │   └── postman_environment.json
│   │   └── Flask_CRUD_TestPlan_44TCs.csv
│   ├── requirements.txt                 # Python dependencies
│   ├── setup_database.sql               # Database initialization
│   ├── Dockerfile                       # Backend container
│   ├── run-pytest.sh                    # Pytest runner script
│   ├── pytest.ini                       # Pytest config
│   ├── install_odbc.sh                  # ODBC driver installer
│   └── generate-unified-report.sh       # Test report generator
│
├── docker-compose.yml                   # Multi-container config
├── README.md                            # Original documentation
├── updated_readme.md                    # This file
├── JWT_LOGIN_INSTRUCTIONS.md            # JWT setup guide
├── PostgreSQL Setup.md                  # PostgreSQL guide
├── docker-network-setup.md              # Docker networking guide
├── FEATURE_IMPLEMENTATION_GUIDE.md      # Feature additions guide
└── app_documentation.md                 # API documentation
```

---

## 📋 Prerequisites

### All Platforms (Linux & Windows)

- **Git** — Version control
  - Linux: `sudo apt install git`
  - Windows: Download from https://git-scm.com/

### For Local Development (Without Docker)

#### Linux
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3.11
sudo apt install -y python3.11 python3.11-venv python3-pip

# Install Node.js 18+
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install SQLite
sudo apt install -y sqlite3

# Install PostgreSQL (optional)
sudo apt install -y postgresql postgresql-contrib

# Install Docker (optional, if using containers)
sudo apt install -y docker.io docker-compose
sudo usermod -aG docker $USER
```

#### Windows
- **Python 3.11+** — Download from https://www.python.org/ (add to PATH)
- **Node.js 18+** — Download from https://nodejs.org/
- **SQLite** — Included with Python
- **PostgreSQL** (optional) — Download from https://www.postgresql.org/download/windows/
- **Docker Desktop** (optional) — Download from https://www.docker.com/products/docker-desktop/
- **Git Bash** or **PowerShell** — For running commands
- **WSL 2** (recommended) — Windows Subsystem for Linux 2

### For Docker Setup

- **Docker** (20.10+)
  - Linux: `sudo apt install docker.io docker-compose`
  - Windows: Install Docker Desktop

- **Docker Compose** (2.0+) — Usually included with Docker Desktop

### Verify Installations

```bash
# Check Python
python3 --version          # Should be 3.11+
# OR
python --version           # Windows

# Check Node.js
node --version             # Should be 18+
npm --version              # Should be 9+

# Check Git
git --version

# Check Docker (if installing)
docker --version
docker-compose --version
```

---

## 🚀 Installation & Setup

### Linux Setup

#### Step 1: Clone Repository
```bash
cd ~/Downloads
git clone <repository-url>
cd simple_book_management_may_2026
```

#### Step 2: Backend Setup

```bash
# Navigate to Server directory
cd Server

# Create Python virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Initialize database
python3 app.py  # This creates books.db

# Run Flask server (default port 5001)
flask run --host=0.0.0.0 --port=5001
# OR
python3 app.py

# You should see: "Running on http://127.0.0.1:5001"
```

In a **new terminal**:

#### Step 3: Frontend Setup

```bash
# Navigate to Client directory
cd Client

# Install Node dependencies
npm install

# Start development server (default port 5173)
npm run dev

# You should see: "VITE v5.3.4 ready in ... ms"
```

#### Step 4: Access Application

Open browser and navigate to:
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5001
- **API Docs**: http://localhost:5001/apidocs

---

### Windows Setup

#### Step 1: Clone Repository

Using **PowerShell** or **Git Bash**:

```powershell
cd $env:USERPROFILE\Downloads
git clone <repository-url>
cd simple_book_management_may_2026
```

#### Step 2: Backend Setup

```powershell
# Navigate to Server directory
cd Server

# Create Python virtual environment
python -m venv venv

# Activate virtual environment (PowerShell)
.\venv\Scripts\Activate.ps1

# OR for Git Bash
source venv/Scripts/activate

# Upgrade pip
python -m pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Initialize and run Flask server
python app.py

# Server runs on http://127.0.0.1:5001
```

In a **new PowerShell/Git Bash window**:

#### Step 3: Frontend Setup

```powershell
# Navigate to Client directory
cd Client

# Install Node dependencies
npm install

# Start development server
npm run dev

# Frontend runs on http://localhost:5173
```

#### Step 4: Access Application

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:5001
- **API Docs**: http://localhost:5001/apidocs

---

## 🗄️ Database Configuration

### SQLite (Default - Development)

SQLite is file-based and requires no setup.

**Automatic initialization:**
```bash
# Running the app creates books.db automatically
python3 app.py
```

**Database location:**
```
Server/books.db
```

**View database with SQLite Browser:**
```bash
# Linux
sudo apt install sqlite3
sqlite3 Server/books.db

# Windows - Download DB Browser for SQLite
# https://sqlitebrowser.org/
```

---

### PostgreSQL Setup (Optional - Production)

#### Linux

```bash
# Install PostgreSQL
sudo apt update
sudo apt install -y postgresql postgresql-contrib

# Start PostgreSQL service
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Switch to postgres user
sudo -i -u postgres

# Open PostgreSQL CLI
psql

# In psql, set password for superuser
ALTER USER postgres WITH PASSWORD 'your-secure-password';

# Create database
CREATE DATABASE books_db;

# Create user
CREATE USER books_user WITH PASSWORD 'books-password';

# Grant privileges
GRANT ALL PRIVILEGES ON DATABASE books_db TO books_user;

# Exit psql
\q
```

#### Windows

```powershell
# Download PostgreSQL installer
# https://www.postgresql.org/download/windows/

# During installation, remember the superuser password

# After installation, open Command Prompt and connect:
psql -U postgres

# Create database and user
CREATE DATABASE books_db;
CREATE USER books_user WITH PASSWORD 'books-password';
GRANT ALL PRIVILEGES ON DATABASE books_db TO books_user;
\q
```

#### Configure Flask for PostgreSQL

Update `Server/requirements.txt`:
```
psycopg2-binary==2.9.10
```

Create `.env` file in `Server/` directory:
```
DATABASE_URL=postgresql://books_user:books-password@localhost:5432/books_db
JWT_SECRET_KEY=your-secure-secret-key
FLASK_ENV=production
```

Update `Server/app.py` to use PostgreSQL:
```python
import os
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL',
    'postgresql://books_user:books-password@localhost:5432/books_db'
)
db = SQLAlchemy(app)
```

---

### MSSQL Setup (Optional)

Refer to [docker-network-setup.md](docker-network-setup.md) for complete MSSQL + Docker setup.

**Quick Setup:**
```bash
# Using Docker (recommended)
docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=YourStrong@Pass123" \
  -p 1433:1433 -d mcr.microsoft.com/mssql/server:2019-latest

# Update requirements.txt
pip install pyodbc

# Update connection string in app.py
```

---

## 🐳 Docker Setup

### Prerequisites
- Docker installed
- Docker Compose installed

### Option 1: Docker Compose (Recommended)

#### Linux/Windows (Git Bash)

```bash
# Navigate to project root
cd simple_book_management_may_2026

# Build images
docker-compose build

# Start containers
docker-compose up -d

# Check running containers
docker-compose ps

# View logs
docker-compose logs -f

# Access services
# Frontend: http://localhost:5173
# Backend: http://localhost:5001
# API Docs: http://localhost:5001/apidocs

# Stop containers
docker-compose down

# Remove images and volumes
docker-compose down -v
```

### Option 2: Manual Docker Commands

#### Build Images

```bash
# Build backend image
docker build -t book-management-backend ./Server

# Build frontend image
docker build -t book-management-frontend ./Client
```

#### Create Network

```bash
docker network create book-management-network
```

#### Run Backend Container

```bash
docker run -d \
  --name book-management-backend \
  --network book-management-network \
  -p 5001:5001 \
  -e FLASK_APP=app.py \
  -e FLASK_ENV=production \
  -e JWT_SECRET_KEY=your-secret-key \
  -v backend_data:/app/data \
  book-management-backend
```

#### Run Frontend Container

```bash
docker run -d \
  --name book-management-frontend \
  --network book-management-network \
  -p 5173:5173 \
  -e VITE_BACKEND_URL=http://localhost:5001 \
  book-management-frontend
```

#### Check Container Status

```bash
# List running containers
docker ps

# View logs
docker logs book-management-backend
docker logs book-management-frontend

# Access container shell
docker exec -it book-management-backend /bin/bash
docker exec -it book-management-frontend /bin/sh
```

#### Stop Containers

```bash
docker stop book-management-backend book-management-frontend
docker rm book-management-backend book-management-frontend
```

### Docker Troubleshooting

```bash
# Check Docker daemon status
docker ps

# If containers fail to start, check logs
docker logs container-name

# Rebuild without cache
docker-compose build --no-cache

# Remove dangling images
docker system prune -a

# View Docker network
docker network ls
docker network inspect book-management-network
```

---

## ▶️ Running the Application

### Local Development (Without Docker)

#### Terminal 1: Backend

```bash
cd Server

# Activate virtual environment
# Linux:
source venv/bin/activate
# Windows:
.\venv\Scripts\Activate.ps1

# Run Flask
python3 app.py
# OR
flask run --host=0.0.0.0 --port=5001
```

#### Terminal 2: Frontend

```bash
cd Client

# Install dependencies (first time only)
npm install

# Start dev server
npm run dev
```

#### Access the App

- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:5001
- **API Documentation**: http://localhost:5001/apidocs

---

### Using Docker Compose

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f

# Access services
# Frontend: http://localhost:5173
# Backend: http://localhost:5001

# Stop services
docker-compose down
```

---

### Environment Variables

Create `.env` file in `Server/` directory:

```
# Flask Configuration
FLASK_ENV=production
FLASK_APP=app.py

# JWT Configuration
JWT_SECRET_KEY=your-super-secret-key-change-in-production

# Database Configuration
BOOKS_DB_PATH=/app/data/books.db
DATABASE_URL=postgresql://user:password@localhost:5432/books_db

# MSSQL Configuration
MSSQL_SERVER=localhost
MSSQL_USER=sa
MSSQL_PASSWORD=YourStrong@Pass123
MSSQL_DB=books_db
```

Create `.env` file in `Client/` directory:

```
VITE_BACKEND_URL=http://localhost:5001
```

---

## 📡 API Endpoints

All endpoints are prefixed with `http://localhost:5001`

### Book Management

#### Get All Books
```http
GET /
Content-Type: application/json

# Response (200 OK)
[
  {
    "id": 1,
    "name": "The Great Gatsby",
    "publisher": "Scribner",
    "date": "2023-01-15",
    "cost": 19.99
  },
  ...
]
```

#### Get Single Book
```http
GET /:id
Content-Type: application/json

# Response (200 OK)
{
  "id": 1,
  "name": "The Great Gatsby",
  "publisher": "Scribner",
  "date": "2023-01-15",
  "cost": 19.99
}
```

#### Create Book (Protected - JWT Required)
```http
POST /create
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>

{
  "name": "New Book",
  "publisher": "Publisher Name",
  "date": "2024-01-01",
  "cost": 25.99
}

# Response (201 Created)
{
  "id": 2,
  "message": "Book created successfully"
}
```

#### Update Book (Protected - JWT Required)
```http
PUT /update/:id
Content-Type: application/json
Authorization: Bearer <JWT_TOKEN>

{
  "name": "Updated Title",
  "publisher": "New Publisher",
  "date": "2024-06-01",
  "cost": 29.99
}

# Response (200 OK)
{
  "message": "Book updated successfully"
}
```

#### Delete Book (Protected - JWT Required)
```http
DELETE /delete/:id
Authorization: Bearer <JWT_TOKEN>

# Response (200 OK)
{
  "message": "Book deleted successfully"
}
```

---

### Authentication (JWT)

#### User Signup
```http
POST /signup
Content-Type: application/json

{
  "username": "newuser",
  "password": "secure-password"
}

# Response (201 Created)
{
  "message": "User created successfully"
}
```

#### User Login
```http
POST /login
Content-Type: application/json

{
  "username": "newuser",
  "password": "secure-password"
}

# Response (200 OK)
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Health Check
```http
GET /health

# Response (200 OK)
{
  "status": "healthy"
}
```

---

## ✅ Testing

### Frontend Testing (Playwright)

#### Install Browsers (First Time)
```bash
cd Client
npm run test:install
```

#### Run Tests
```bash
# Run all tests
npm run test

# Run tests in headed mode (see browser)
npm run test:headed

# Debug mode
npm run test:debug

# UI Mode
npm run test:ui

# View HTML report
npm run test:report
```

#### Test Files
```
Client/tests/
├── app.spec.js              # App navigation tests
├── books.spec.js            # Book listing tests
├── create-book.spec.js      # Create book functionality
├── update-book.spec.js      # Update book functionality
├── complete-flow.spec.js    # End-to-end workflows
└── test-setup.js            # Test utilities
```

---

### Backend Testing (Pytest)

#### Install Test Dependencies
```bash
cd Server
pip install -r requirements.txt
```

#### Run Tests
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/pytest/test_books_api.py -v

# Generate coverage report
pytest --cov=. tests/

# Run tests with JSON report
pytest --json-report --json-report-file=pytest-report.json

# Run tests with script
bash run-pytest.sh
```

#### Test Files
```
Server/tests/pytest/
├── test_books_api.py        # API unit tests
└── conftest.py              # Pytest configuration
```

#### Pytest Configuration
See [Server/pytest.ini](Server/pytest.ini)

---

### API Testing (Newman/Postman)

```bash
cd Server/tests/postman_newman

# Install dependencies
npm install

# Run Newman tests
bash run-newman-tests.sh

# View reports
# - newman-report.html
# - newman-enhanced-report.html
# - newman-result.json
```

#### Postman Files
```
Server/tests/postman_newman/
├── book_api_postman_collection.json    # API endpoints
└── postman_environment.json             # Environment variables
```

---

## 🔐 JWT Authentication

JWT (JSON Web Token) secures API endpoints requiring authentication.

### Setup

#### Backend Configuration

In `Server/app.py`:
```python
from flask_jwt_extended import JWTManager, jwt_required, create_access_token

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev-secret-key')
jwt = JWTManager(app)

# Protect endpoints
@app.route('/create', methods=['POST'])
@jwt_required()
def create_book():
    current_user = get_jwt_identity()
    # ... create book code
```

#### Frontend Configuration

In `Client/src/App.jsx` or `axios` setup:
```javascript
import axios from 'axios';

// Set token in localStorage after login
localStorage.setItem('access_token', response.data.access_token);

// Add token to request headers
axios.defaults.headers.common['Authorization'] = 
  `Bearer ${localStorage.getItem('access_token')}`;

// Remove token on logout
localStorage.removeItem('access_token');
delete axios.defaults.headers.common['Authorization'];
```

### Login Flow

1. **Signup**: User creates account with username/password
2. **Login**: User submits credentials, receives JWT token
3. **Store Token**: Token saved in localStorage (Client)
4. **Use Token**: Add `Authorization: Bearer <token>` to requests
5. **Logout**: Remove token from localStorage

### Full JWT Setup Guide

See [JWT_LOGIN_INSTRUCTIONS.md](JWT_LOGIN_INSTRUCTIONS.md)

---

## 🐛 Troubleshooting

### Common Issues

#### Port Already in Use

**Linux/Mac:**
```bash
# Kill process using port 5001
lsof -i :5001
kill -9 <PID>

# OR find and kill port 5173
lsof -i :5173
kill -9 <PID>
```

**Windows PowerShell:**
```powershell
# Find process on port 5001
netstat -ano | findstr :5001

# Kill process
taskkill /PID <PID> /F
```

---

#### CORS Errors

**Solution:** Backend Flask app already has CORS enabled.

If getting CORS errors, verify in `Server/app.py`:
```python
from flask_cors import CORS
CORS(app)  # Enables all origins
```

---

#### Database Locked Error

**Cause:** SQLite database is being accessed by multiple processes.

**Solution:**
```bash
# Remove old database
rm Server/books.db

# Restart Flask server
python3 Server/app.py
```

---

#### Virtual Environment Not Activating

**Linux:**
```bash
source venv/bin/activate
# Verify activation
which python  # Should show venv path
```

**Windows PowerShell:**
```powershell
.\venv\Scripts\Activate.ps1
# If error, run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

#### npm Dependencies Issues

```bash
# Clear npm cache
npm cache clean --force

# Remove node_modules and reinstall
rm -rf node_modules package-lock.json
npm install

# Or use npm ci (clean install)
npm ci
```

---

#### Docker Container Won't Start

```bash
# Check logs
docker-compose logs backend
docker-compose logs frontend

# Rebuild without cache
docker-compose build --no-cache

# Start with verbose output
docker-compose up
```

---

#### Backend Connection Refused

If frontend can't reach backend at `http://localhost:5001`:

**Check if backend is running:**
```bash
curl http://localhost:5001/health
```

**Verify backend port:**
```bash
# Linux
netstat -tlnp | grep 5001

# Windows
netstat -ano | findstr :5001
```

---

### Getting Help

1. Check logs for error messages
2. Verify all prerequisites are installed
3. Ensure ports 5001 and 5173 are free
4. Review [FEATURE_IMPLEMENTATION_GUIDE.md](FEATURE_IMPLEMENTATION_GUIDE.md)
5. Check [PROJECT_EXPLANATION_FROM_SCRATCH.md](PROJECT_EXPLANATION_FROM_SCRATCH.md)

---

## 📈 Development Workflow

### Feature Implementation Checklist

1. **Plan** — Define requirements and architecture
2. **Database** — Add migrations (if needed)
3. **Backend** — Implement API endpoints
4. **Frontend** — Create UI components
5. **Test** — Write unit and E2E tests
6. **Review** — Code review and debugging
7. **Deploy** — Push to Docker or production

### Useful Commands

```bash
# Backend Development
cd Server
source venv/bin/activate      # Linux
pip install -r requirements.txt
python3 app.py

# Frontend Development
cd Client
npm install
npm run dev
npm run lint                  # Check code style
npm run build                 # Build for production

# Testing
npm run test                  # Frontend tests
pytest                        # Backend tests
bash run-pytest.sh            # Automated test suite

# Docker
docker-compose up -d          # Start services
docker-compose down           # Stop services
docker-compose logs -f        # View logs
```

### Code Style & Linting

**Frontend:**
```bash
cd Client
npm run lint                  # Check for errors
npm run lint -- --fix         # Auto-fix issues
```

**Backend:**
```bash
cd Server
pip install flake8
flake8 app.py                 # Check style
```

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [React Documentation](https://react.dev/)
- [Vite Documentation](https://vitejs.dev/)
- [Playwright Testing](https://playwright.dev/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Docker Documentation](https://docs.docker.com/)
- [JWT Documentation](https://jwt.io/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## 📞 Support

For issues, questions, or contributions:

1. Check existing documentation files
2. Review error messages and logs
3. Verify all prerequisites are installed
4. Test with `docker-compose` for consistency
5. Create detailed issue reports with:
   - OS and versions
   - Exact error messages
   - Steps to reproduce
   - Expected vs actual behavior

---

## 📄 License

[Add your license information here]

---

## ✨ Summary

This complete guide covers:
- ✅ Linux & Windows setup
- ✅ Database configuration (SQLite, PostgreSQL, MSSQL)
- ✅ Docker & Docker Compose setup
- ✅ Local and containerized development
- ✅ API endpoints and authentication
- ✅ Testing with Playwright & Pytest
- ✅ JWT authentication implementation
- ✅ Troubleshooting common issues
- ✅ Development workflow best practices

**Ready to start?** Follow the setup guide for your OS and database choice!

---

**Last Updated:** June 2026  
**Version:** 2.0  
**Compatible With:** Python 3.11+, Node.js 18+, Docker 20.10+
