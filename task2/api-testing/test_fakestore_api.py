import requests
import sys
from typing import Dict, List, Any
from dataclasses import dataclass

@dataclass
class ValidationError:
    product_id: int
    error_type: str
    details: str

def validate_product(product: Dict[str, Any]) -> List[ValidationError]:
    """
    Validates a single product object against the defined rules.
    Returns a list of ValidationError objects if any rules are violated.
    """
    errors = []
    product_id = product.get('id', 'Unknown')

    # Validate title
    title = product.get('title', '')
    if not isinstance(title, str) or not title.strip():
        errors.append(ValidationError(
            product_id=product_id,
            error_type="Invalid Title",
            details="Title must be a non-empty string"
        ))

    # Validate price
    price = product.get('price', 0)
    if not isinstance(price, (int, float)) or price < 0:
        errors.append(ValidationError(
            product_id=product_id,
            error_type="Invalid Price",
            details=f"Price must be a non-negative number, got: {price}"
        ))

    # Validate rating
    rating = product.get('rating', {})
    rate = rating.get('rate', 0)
    if not isinstance(rate, (int, float)) or rate > 5:
        errors.append(ValidationError(
            product_id=product_id,
            error_type="Invalid Rating",
            details=f"Rating must be less than or equal to 5, got: {rate}"
        ))

    return errors

def eprint(*args, **kwargs):
    """Print to stderr"""
    print(*args, file=sys.stderr, flush=True, **kwargs)

def test_fakestore_api():
    """
    Tests the Fake Store API by validating all products against the defined rules.
    """
    eprint("Starting API test...")
    
    # API endpoint
    url = "https://fakestoreapi.com/products"

    try:
        # Make the GET request
        eprint(f"Making GET request to {url}...")
        response = requests.get(url)
        
        # Verify HTTP status code
        eprint(f"Received status code: {response.status_code}")
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        
        # Get the products data
        products = response.json()
        eprint(f"Retrieved {len(products)} products")
        
        # Validate each product
        all_errors = []
        for product in products:
            errors = validate_product(product)
            all_errors.extend(errors)

        # Print validation results
        if not all_errors:
            eprint("\n✅ All products passed validation!")
        else:
            eprint("\n❌ Found validation errors:")
            for error in all_errors:
                eprint(f"\nProduct ID: {error.product_id}")
                eprint(f"Error Type: {error.error_type}")
                eprint(f"Details: {error.details}")

    except requests.RequestException as e:
        eprint(f"❌ Error making API request: {e}")
    except Exception as e:
        eprint(f"❌ Unexpected error: {str(e)}")
        import traceback
        eprint(traceback.format_exc())

if __name__ == "__main__":
    test_fakestore_api() 