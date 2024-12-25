DELIMITER $$

CREATE EVENT delete_old_pending_orders
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    DELETE FROM orders
    WHERE status = 'pending' AND order_date < NOW() - INTERVAL 7 DAY;
END $$

DELIMITER ;
