import requests
import json
from typing import List, Dict, Any

def validate_product(product: Dict[str, Any]) -> List[str]:
    """
    Validate a single product object and return a list of validation errors.
    """
    errors = []
    
    # Validate title
    title = product.get('title', '')
    if not isinstance(title, str) or not title.strip():
        errors.append(f"Empty or invalid title for product ID {product.get('id', 'unknown')}")
    
    # Validate price
    price = product.get('price', 0)
    if not isinstance(price, (int, float)) or price < 0:
        errors.append(f"Negative or invalid price ({price}) for product ID {product.get('id', 'unknown')}")
    
    # Validate rating
    rating = product.get('rating', {}).get('rate', 0)
    if not isinstance(rating, (int, float)) or rating > 5:
        errors.append(f"Invalid rating ({rating}) exceeds 5 for product ID {product.get('id', 'unknown')}")
    
    return errors

def test_products_api():
    """
    Test the FakeStore API products endpoint and validate the data.
    """
    # API endpoint
    url = 'https://fakestoreapi.com/products'
    
    try:
        # Make GET request
        response = requests.get(url)
        
        # Validate HTTP status code
        if response.status_code != 200:
            print(f"❌ API request failed with status code: {response.status_code}")
            return
        
        print("✅ API request successful (Status 200 OK)")
        
        # Parse JSON response
        products = response.json()
        
        if not isinstance(products, list):
            print("❌ Invalid response format: expected a list of products")
            return
        
        # Validate each product
        all_errors = []
        for product in products:
            errors = validate_product(product)
            if errors:
                all_errors.extend(errors)
        
        # Print results
        if all_errors:
            print("\n🔍 Found the following data validation issues:")
            for error in all_errors:
                print(f"❌ {error}")
        else:
            print("\n✅ All products passed validation checks!")
            
        print(f"\nTotal products checked: {len(products)}")
        print(f"Total issues found: {len(all_errors)}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error occurred: {e}")
    except json.JSONDecodeError as e:
        print(f"❌ Failed to parse JSON response: {e}")
    except Exception as e:
        print(f"❌ Unexpected error occurred: {e}")

if __name__ == '__main__':
    print("🚀 Starting API validation tests...")
    test_products_api() 