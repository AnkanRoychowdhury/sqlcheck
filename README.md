# 📘 E-Commerce SQL Practice Scenarios
A comprehensive list of real-world eCommerce SQL scenarios covering product data, users, order management, payments, shipments, inventory, analytics, fraud detection, and advanced SQL concepts.

---

## 🧩 LEVEL 1 — PRODUCT & USER BASICS
1. List all active products along with their brands and price.
2. Get all users registered in the last X days.
3. Count number of users per city.
4. Find users who have never placed an order.
5. List products under each category (category → products).
6. Find categories with no products assigned.

---

## 🛒 LEVEL 2 — CART OPERATIONS
7. Show cart details for a given user.
8. Find users who have items in cart but never placed an order (abandoned carts).
9. List largest carts by item count.
10. Identify products most frequently added to carts.

---

## 📦 LEVEL 3 — ORDER MANAGEMENT
11. Show all orders with user and address details.
12. Count orders by status.
13. Find total sales per day.
14. Find orders with more than 3 items.
15. Identify orders where item sum ≠ order total (audit).
16. Find top customers by total spending.
17. Show repeat customers (more than 1 order).
18. Identify first-time vs repeat buyers.
19. Find average order value per user.
20. Count cancelled orders per city.

---

## 💳 LEVEL 4 — PAYMENTS
21. List all paid orders and their payment method.
22. Find failed payments and the products involved.
23. Show refunded orders.
24. Compare total order amount vs payment amount.
25. Identify most used payment method.
26. Find users with frequent payment failures.

---

## 🚚 LEVEL 5 — SHIPMENTS
27. List all shipped orders with carrier and tracking.
28. Find delayed shipments (delivery time > X days).
29. Find warehouse with highest dispatch count.
30. Compute carrier efficiency (avg delivery time).
31. Find shipped but not delivered orders.
32. Count items shipped per warehouse.

---

## 🏬 LEVEL 6 — INVENTORY
33. Find products with low stock (< X) per warehouse.
34. Compute total stock per product across warehouses.
35. Identify warehouses with zero stock for a product.
36. Detect inventory mismatches (inactive products with stock).
37. List top stocked products.

---

## 📊 LEVEL 7 — ANALYTICS INSIGHTS
38. Top-selling products by quantity.
39. Most profitable products.
40. User cohort analysis (first order month → repeats).
41. Monthly revenue trend.
42. Customer lifetime value (LTV).
43. RFM scoring for users.
44. Highest revenue cities.
45. Highest revenue categories.
46. VIP user identification.
47. Active users (recent buyers).
48. Churned users (no orders in 6 months).

---

## 🕵️ LEVEL 8 — FRAUD DETECTION
49. Users with multiple failed payments.
50. Orders delivered without successful payment.
51. Suspicious large-quantity orders.
52. Users with repeated refunds.
53. Users ordering from widely different cities.
54. High cancellation ratio per user (>80%).
55. More than 5 orders placed in under 10 minutes.

---

## 🛠️ LEVEL 9 — ADVANCED SQL / WINDOW FUNCTIONS
56. Fetch last order per user.
57. Top product per category by revenue.
58. Rank customers by spending.
59. Rank products by sales within brand.
60. 7-day moving average of orders.
61. Detect price drift between product and order_item.
62. Order velocity per hour/day/week.

---

## 🧾 LEVEL 10 — COMPLEX BUSINESS PROBLEMS
63. Cart-to-purchase conversion rate.
64. Refund ratio per category.
65. Order → payment → shipment funnel analytics.
66. Warehouse delay identification.
67. Generate full order report (user + address + items + payment + shipment).
68. Detect inventory update anomalies.
69. Product affinity (frequently bought together).
70. Repeat purchase frequency per category.

---

## 🧠 TRICKY CASES
71. Product each user bought in highest quantity.
72. Users who bought *all* products in a specific category.
73. Longest purchase streak per user.
74. Category-level gross margin calculation.
75. Predict warehouse stock-out based on order rate.
76. Reconstruct status timeline per order.
77. Detect payments created before orders (data corruption).
78. Find duplicate users (same contact info pattern).
79. Detect orphan records (order_items without order).
80. Inventory variance audit (sum mismatch).

---

Happy querying! 🎯