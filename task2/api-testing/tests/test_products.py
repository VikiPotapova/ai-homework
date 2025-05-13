import pytest
import requests
from typing import Dict, Any, List

class TestFakeStoreAPI:
    BASE_URL = "https://fakestoreapi.com/products"

    @pytest.fixture
    def products_response(self) -> List[Dict[str, Any]]:
        """Fixture to get products from the API"""
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200, f"API request failed with status code: {response.status_code}"
        return response.json()

    def test_response_status(self):
        """Test that the API returns a 200 status code"""
        response = requests.get(self.BASE_URL)
        assert response.status_code == 200, "API request failed"

    def test_product_titles(self, products_response):
        """Test that all product titles are non-empty strings"""
        invalid_products = []
        for product in products_response:
            title = product.get('title', '')
            if not isinstance(title, str) or not title.strip():
                invalid_products.append(f"Product ID {product.get('id', 'unknown')}: Empty or invalid title")
        
        assert not invalid_products, "\n".join(invalid_products)

    def test_product_prices(self, products_response):
        """Test that all product prices are non-negative numbers"""
        invalid_products = []
        for product in products_response:
            price = product.get('price', 0)
            if not isinstance(price, (int, float)) or price < 0:
                invalid_products.append(
                    f"Product ID {product.get('id', 'unknown')}: Invalid price ({price})"
                )
        
        assert not invalid_products, "\n".join(invalid_products)

    def test_product_ratings(self, products_response):
        """Test that all product ratings are less than or equal to 5"""
        invalid_products = []
        for product in products_response:
            rating = product.get('rating', {}).get('rate', 0)
            if not isinstance(rating, (int, float)) or rating > 5:
                invalid_products.append(
                    f"Product ID {product.get('id', 'unknown')}: Invalid rating ({rating})"
                )
        
        assert not invalid_products, "\n".join(invalid_products)

    def test_response_structure(self, products_response):
        """Test that the response is a list of products with required fields"""
        assert isinstance(products_response, list), "Response is not a list"
        
        required_fields = {'id', 'title', 'price', 'rating'}
        missing_fields = []
        
        for product in products_response:
            assert isinstance(product, dict), "Product is not a dictionary"
            missing = required_fields - set(product.keys())
            if missing:
                missing_fields.append(
                    f"Product ID {product.get('id', 'unknown')}: Missing fields {missing}"
                )
        
        assert not missing_fields, "\n".join(missing_fields) 