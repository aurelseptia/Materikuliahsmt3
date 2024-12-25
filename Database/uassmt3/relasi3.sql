ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_products
FOREIGN KEY (product_id) REFERENCES products(product_id);
