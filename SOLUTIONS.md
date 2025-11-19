# Solutions for all scenarios (Level Wise)

---

## 🧩 LEVEL 1 — PRODUCT & USER BASICS
1. List all active products along with their brands and price.
    ~~~sql 
    SELECT product_id, name, brand, price FROM `products` WHERE active = 1;
    ~~~
2. Get all users registered in the last X days.
   ~~~sql 
   SELECT COUNT(*) AS total_users FROM users WHERE created_at >= NOW() - INTERVAL 30 DAY;
   ~~~
3. Count number of users per city.
   ~~~sql
   SELECT city, COUNT(*) AS user_count_by_city FROM addresses WHERE is_default = 1 GROUP BY city;
   ~~~
4. Find users who have never placed an order.
   ~~~mysql
   SELECT u.* FROM users u LEFT JOIN orders o ON u.user_id = o.user_id where o.user_id IS NULL;
   ~~~
5. List products under each category (category → products).
6. Find categories with no products assigned.

---

## 📦 LEVEL 3 — ORDER MANAGEMENT
11. Show all orders with user and address details.
      ~~~mysql
      SELECT * FROM `orders` WHERE user_id IS NOT NULL AND address_id IS NOT NULL;
      ~~~
12. Count orders by status.
      ~~~mysql
      SELECT status, COUNT(*) as status_count FROM orders GROUP BY status;
      ~~~
13. Find total sales per day.
      ~~~mysql
      SELECT DATE(created_at) AS order_date, COUNT(*) AS total_orders, SUM(total_amount) AS total_sales FROM orders WHERE status IN ('PAID', 'SHIPPED', 'DELIVERED') GROUP BY DATE(created_at) ORDER BY order_date;
      ~~~
14. Find orders with more than 3 items.
15. Identify orders where item sum ≠ order total (audit).
16. Find top customers by total spending.
17. Show repeat customers (more than 1 order).
18. Identify first-time vs repeat buyers.
19. Find average order value per user.
20. Count cancelled orders per city.

---