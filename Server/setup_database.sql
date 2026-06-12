-- ============================================
-- MSSQL Database Setup for Flask CRUD App
-- Run this inside mssql-container using sqlcmd
-- ============================================

-- Step 1: Create the database
CREATE DATABASE books_db;
GO

-- Step 2: Use the database
USE books_db;
GO

-- Step 3: Create the book table
CREATE TABLE book (
    id INT IDENTITY(1,1) PRIMARY KEY,
    publisher NVARCHAR(255) NOT NULL,
    name NVARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    cost FLOAT NOT NULL
);
GO

-- Step 4: Create the users table
CREATE TABLE users (
    id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(255) NOT NULL,
    password_hash NVARCHAR(255) NOT NULL
);
GO

-- Step 5: Insert sample data for testing
INSERT INTO book (publisher, name, date, cost) VALUES
('Penguin Random House', 'Python Crash Course', '2023-01-15', 299.99),
('O''Reilly Media', 'Learning Flask', '2023-06-20', 399.50),
('Manning Publications', 'Flask Web Development', '2024-03-10', 449.00);
GO

-- Step 6: Verify everything was created
SELECT * FROM book;
GO

SELECT * FROM users;
GO
