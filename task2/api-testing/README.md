# Fake Store API Testing Script

This script performs automated testing of the Fake Store API (https://fakestoreapi.com/products) to validate product data according to specific rules.

## Validation Rules

The script checks the following:
1. HTTP status code must be 200 OK
2. For each product:
   - Title must be a non-empty string
   - Price must be a non-negative number
   - Rating must be less than or equal to 5

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Tests

To run the tests, simply execute:
```bash
python test_fakestore_api.py
```

## Output

The script will output:
- ✅ Success message if all validations pass
- ❌ Detailed error messages for any products that fail validation, including:
  - Product ID
  - Error Type
  - Error Details 