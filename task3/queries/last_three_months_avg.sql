-- Calculate the average order value for the last three months relative to the current date
SELECT AVG(amount) as avg_order_value
FROM orders
WHERE order_date >= date('now', '-3 months')
AND order_date <= date('now'); 