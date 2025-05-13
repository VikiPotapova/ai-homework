-- Find the customer who spent the most overall (highest total amount across all orders)
SELECT customer,
       SUM(amount) as total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1; 