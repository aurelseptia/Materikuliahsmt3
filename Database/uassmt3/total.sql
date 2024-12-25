SELECT 
    users.user_id,
    users.full_name,
    users.email,
    total_spent.total_price AS total_spent
FROM users
JOIN (
    SELECT 
        user_id, 
        SUM(total_price) AS total_price
    FROM orders
    GROUP BY user_id
) AS total_spent ON users.user_id = total_spent.user_id
ORDER BY total_spent.total_price DESC
LIMIT 1;
