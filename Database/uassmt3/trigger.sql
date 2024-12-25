DELIMITER $$

CREATE TRIGGER update_order_total
AFTER INSERT ON order_details
FOR EACH ROW
BEGIN
    UPDATE orders
    SET total_price = (SELECT calculate_order_total(NEW.order_id))
    WHERE order_id = NEW.order_id;
END $$

DELIMITER ;
