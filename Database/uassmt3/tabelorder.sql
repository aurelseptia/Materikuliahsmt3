CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    order_date DATETIME NOT NULL,
    status ENUM('pending', 'paid', 'shipped', 'completed', 'canceled') NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    shipping_address TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
