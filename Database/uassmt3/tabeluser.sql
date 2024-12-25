CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'customer') NOT NULL,
    full_name VARCHAR(100),
    email VARCHAR(100),
    phone_number VARCHAR(20),
    address TEXT
);
