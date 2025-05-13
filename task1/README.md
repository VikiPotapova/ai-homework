# AI Homework Tasks

This repository contains two separate tasks:

## Task 1: Expense Calculator Web Application

A modern React-based web application for tracking and analyzing monthly expenses. The application allows users to:
- Add expenses with categories and amounts
- View a list of all expenses
- Calculate total expenses, daily average, and top 3 highest expenses

### Running Task 1
```bash
cd task1/expense-calculator
npm install
npm start
```

## Task 2: API Testing Script

A Python script that tests the FakeStore API (https://fakestoreapi.com/products) and validates product data according to specific rules.

### Running Task 2
```bash
cd task2/api-testing
pip install -r requirements.txt
python test_products_api.py
```

### Validation Rules
- HTTP status code must be 200 OK
- Product title must be a non-empty string
- Price must be a non-negative number
- Rating must be less than or equal to 5

The script will output any validation errors found in the product data.
