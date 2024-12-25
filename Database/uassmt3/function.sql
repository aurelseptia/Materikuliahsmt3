DELIMITER $$

CREATE FUNCTION calculate_order_total(orderID INT)
RETURNS DECIMAL(10, 2)
DETERMINISTIC
BEGIN
    DECLARE total DECIMAL(10, 2);
    SELECT SUM(quantity * price_per_item) INTO total
    FROM order_details
    WHERE order_id = orderID;
    RETURN total;
END $$

DELIMITER ;
