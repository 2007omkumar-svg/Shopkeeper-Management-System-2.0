# Shopkeeper Management System 2.0

A desktop inventory management system built with Python, Tkinter and MySQL.

## Features
- Add, update, delete and search products
- Inventory table with stock tracking
- MySQL database storage
- Input validation and error handling
- Tkinter GUI

## Setup
1. Install Python 3 and MySQL.
2. Create the database:
```sql
CREATE DATABASE shop;
```
3. Copy `config.example.json` to `config.json` and enter your MySQL password.
4. Install dependencies:
```bash
pip install -r requirements.txt
```
5. Run:
```bash
python src/main.py
```

Never upload `config.json`; it is ignored by Git.


## Demo Data

After creating the `shop` database, you can optionally run the sample statements below in MySQL:

```sql
USE shop;

INSERT INTO kirana
(pid, pname, price, discount, quantity, instock, soldout)
VALUES
(101, 'Parle-G Biscuits', 10.00, 5.00, 100, 82, 18),
(102, 'Tata Salt', 28.00, 0.00, 60, 54, 6),
(103, 'Maggi Noodles', 14.00, 2.00, 80, 71, 9),
(104, 'Amul Milk', 32.00, 0.00, 50, 39, 11);
```

## GitHub Presentation Tips

For a portfolio repository, add screenshots of:
1. Main dashboard
2. Add/update product form
3. Inventory table
4. MySQL database table

Keep secrets such as `config.json` out of the repository.

## Learning Outcomes

This project demonstrates:

- Python programming
- Object-oriented organization
- GUI development with Tkinter
- Relational database design
- SQL CRUD operations
- Input validation
- Exception handling
- Separation of UI and database logic
- Git/GitHub project organization
