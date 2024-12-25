ALTER TABLE order_details
ADD CONSTRAINT fk_order_details_orders
FOREIGN KEY (order_id) REFERENCES orders(order_id);
