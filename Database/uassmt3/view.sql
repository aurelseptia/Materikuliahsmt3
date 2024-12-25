SELECT 
    orders.order_id,
    orders.order_date,
    users.full_name AS customer_name,
    users.email AS customer_email,
    users.address AS shipping_address,
    orders.status,
    orders.total_price
FROM orders
JOIN users ON orders.user_id = users.user_id;
