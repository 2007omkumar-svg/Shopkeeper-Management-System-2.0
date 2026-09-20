CREATE DATABASE IF NOT EXISTS shop;
USE shop;

CREATE TABLE IF NOT EXISTS kirana (
    pid INT PRIMARY KEY,
    pname VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    discount DECIMAL(5,2) DEFAULT 0,
    quantity INT NOT NULL,
    instock INT NOT NULL,
    soldout INT NOT NULL
);

-- Optional demo records
INSERT INTO kirana
(pid, pname, price, discount, quantity, instock, soldout)
VALUES
(101, 'Parle-G Biscuits', 10.00, 5.00, 100, 82, 18),
(102, 'Tata Salt', 28.00, 0.00, 60, 54, 6),
(103, 'Maggi Noodles', 14.00, 2.00, 80, 71, 9),
(104, 'Amul Milk', 32.00, 0.00, 50, 39, 11);
