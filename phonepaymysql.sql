/* =====================================================
   DATABASE CREATION
===================================================== */

CREATE DATABASE IF NOT EXISTS phonepe_insights;
USE phonepe_insights;

/* =====================================================
   TABLE CREATION
===================================================== */

-- Aggregated Transactions Table
CREATE TABLE aggregated_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(255),
    year INT,
    quarter INT,
    transaction_type VARCHAR(255),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

-- Aggregated Users Table
CREATE TABLE aggregated_users (
    state VARCHAR(100),
    year INT,
    quarter INT,
    app_opens BIGINT,
    registered_users BIGINT
);

-- Map Transactions Table
CREATE TABLE map_transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    transaction_count BIGINT,
    transaction_amount DOUBLE
);

-- Map Insurance Table
CREATE TABLE map_insurance (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(100),
    year INT,
    quarter INT,
    district VARCHAR(100),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

-- Top Users Table
CREATE TABLE top_users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state VARCHAR(255),
    district VARCHAR(255),
    pincode VARCHAR(10),
    registered_users BIGINT,
    year INT,
    quarter INT
);

-- Top Insurance Table
CREATE TABLE top_insurance (
    state VARCHAR(255),
    year INT,
    quarter INT,
    pincode VARCHAR(10),
    insurance_count BIGINT,
    insurance_amount DOUBLE
);

/* =====================================================
   INDEXES (Performance Optimization)
===================================================== */

CREATE INDEX idx_state_year 
ON aggregated_transactions(state, year);

CREATE INDEX idx_map_state_year 
ON map_transactions(state, year);

CREATE INDEX idx_insurance_state_year 
ON map_insurance(state, year);


/* =====================================================
   ANALYSIS QUERIES
===================================================== */

-- 1. Overall Transaction Summary
SELECT 
    SUM(transaction_amount) AS total_transaction_amount,
    SUM(transaction_count) AS total_transaction_count
FROM aggregated_transactions;


-- 2. Year-wise Transaction Growth
SELECT 
    year,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_transactions
FROM aggregated_transactions
GROUP BY year
ORDER BY year;


-- 3. Quarter-wise Transaction Trend
SELECT 
    year,
    quarter,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transactions
GROUP BY year, quarter
ORDER BY year, quarter;


-- 4. Top 10 States by Transaction Amount
SELECT 
    state,
    SUM(transaction_amount) AS total_amount
FROM aggregated_transactions
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;


-- 5. Category-wise Transaction Performance
SELECT 
    transaction_type,
    SUM(transaction_amount) AS total_amount,
    SUM(transaction_count) AS total_count
FROM aggregated_transactions
GROUP BY transaction_type
ORDER BY total_amount DESC;









-- 8. Insurance Growth (Year-wise)
SELECT 
    year,
    SUM(insurance_amount) AS total_insurance_amount,
    SUM(insurance_count) AS total_insurance_count
FROM map_insurance
GROUP BY year
ORDER BY year;


-- 9. Top 10 Pincode by Insurance Amount
SELECT 
    pincode,
    SUM(insurance_amount) AS total_amount
FROM top_insurance
GROUP BY pincode
ORDER BY total_amount DESC
LIMIT 10;


-- 10. User Growth Trend
SELECT 
    year,
    SUM(registered_users) AS total_users
FROM aggregated_users
GROUP BY year
ORDER BY year;


-- 11. Average Transaction Value per State
SELECT 
    state,
    SUM(transaction_amount) / SUM(transaction_count) AS avg_transaction_value
FROM aggregated_transactions
GROUP BY state
ORDER BY avg_transaction_value DESC;


