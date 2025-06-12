DELETE FROM users WHERE email IS NULL;
UPDATE orders SET status = 'complete' WHERE payment_received = true;
