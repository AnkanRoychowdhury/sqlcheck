✅ IMPORT: users <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/users.csv'
    INTO TABLE users
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (user_id,email,full_name,phone,created_at);"
~~~

✅ IMPORT: addresses <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/addresses.csv'
    INTO TABLE addresses
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (address_id,user_id,address_line,city,state,pincode,is_default);"
~~~

✅ IMPORT: categories <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/categories.csv'
    INTO TABLE categories
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (category_id,name);"
~~~

✅ IMPORT: products <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/products.csv'
    INTO TABLE products
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (product_id,name,description,brand,price,active);"
~~~

✅ IMPORT: product_categories <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/product_categories.csv'
    INTO TABLE product_categories
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (product_id,category_id);"
~~~

✅ IMPORT: warehouses <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/warehouses.csv'
    INTO TABLE warehouses
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (warehouse_id,name,location);"
~~~

✅ IMPORT: inventory <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/inventory.csv'
    INTO TABLE inventory
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (inventory_id,product_id,warehouse_id,quantity,updated_at);"
~~~

✅ IMPORT: orders <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/orders.csv'
    INTO TABLE orders
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (order_id,user_id,address_id,status,total_amount,created_at);"
~~~

✅ IMPORT: order_items <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/order_items.csv'
    INTO TABLE order_items
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (order_item_id,order_id,product_id,quantity,price);"
~~~

✅ IMPORT: payments <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/payments.csv'
    INTO TABLE payments
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (payment_id,order_id,amount,method,status,transaction_ref,created_at);"
~~~

✅ IMPORT: shipments <br>
~~~sql
mysql -u root -p --local-infile=1 ecommerce_local \
-e "LOAD DATA LOCAL INFILE '/data_csv/shipments.csv'
    INTO TABLE shipments
    FIELDS TERMINATED BY ','
    OPTIONALLY ENCLOSED BY '\"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (shipment_id,order_id,warehouse_id,carrier,tracking_number,status,shipped_at,delivered_at);"
~~~