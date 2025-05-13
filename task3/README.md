# SQL Queries for Order Analysis

This directory contains SQL scripts for analyzing order data in SQLite database.

## File Structure

- `schema.sql` - Contains the table definition for the orders table
- `queries/` - Directory containing various analysis queries
  - `march_2024_sales.sql` - Calculates total sales volume for March 2024
  - `top_customer.sql` - Finds the customer with highest total spending
  - `last_three_months_avg.sql` - Calculates average order value for the last 3 months

## Table Structure

The `orders` table has the following structure:
- `id` (INTEGER PRIMARY KEY) - Unique identifier for each order
- `customer` (TEXT) - Customer name or identifier
- `amount` (REAL) - Order amount
- `order_date` (DATE) - Date when the order was placed

## Usage

These queries are written for SQLite database system. To use them:

1. First run the `schema.sql` to create the table structure
2. Then you can run any of the analysis queries from the `queries/` directory

Note: The date functions used in these queries (strftime, date) are SQLite-specific. If you need to use these queries with a different database system, you'll need to modify the date handling syntax accordingly. 