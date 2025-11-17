#!/usr/bin/env python3
# generate_ecom_csvs.py
# Generates CSV files for a relational e-commerce DB.
# Streaming write; deterministic seed.
import csv, os, random, datetime, math, sys

# ---------------- CONFIG ----------------
OUT_DIR = "data_csv"
USERS = 200000        # adjust: 200k users
PRODUCTS = 50000      # adjust: 50k products
CATEGORIES = 50
WAREHOUSES = 8
ORDERS = 1000000      # 1 million orders
MAX_ITEMS_PER_ORDER = 4
SEED = 42
# ----------------------------------------

random.seed(SEED)
os.makedirs(OUT_DIR, exist_ok=True)

def dt_str(offset_days=0):
    base = datetime.datetime(2020,1,1)
    return (base + datetime.timedelta(days=offset_days)).strftime("%Y-%m-%d %H:%M:%S")

# 1) users.csv
with open(os.path.join(OUT_DIR, "users.csv"), "w", newline='') as f:
    w = csv.writer(f)
    # columns: user_id,email,full_name,phone,created_at
    # We'll emit without user_id (auto-increment on load) but include a synthetic id column to help referencing while generating other CSVs
    w.writerow(["user_id","email","full_name","phone","created_at"])
    for uid in range(1, USERS+1):
        email = f"user{uid}@example.com"
        name = f"User {uid}"
        phone = f"9{100000000 + (uid % 900000000)}"
        created = dt_str(uid % 1500)
        w.writerow([uid, email, name, phone, created])

# 2) addresses.csv (1-3 per user)
with open(os.path.join(OUT_DIR, "addresses.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["address_id","user_id","address_line","city","state","pincode","is_default"])
    addr_id = 1
    cities = ['Bengaluru','Kolkata','Mumbai','Delhi','Chennai','Hyderabad','Pune','Jaipur','Lucknow','Kochi']
    for uid in range(1, USERS+1):
        count = 1 + (uid % 3)   # 1..3 addresses
        for idx in range(count):
            city = cities[(uid + idx) % len(cities)]
            line = f"House {100 + uid%5000}, Street {1 + idx}"
            state = f"State-{(uid%28)+1}"
            pincode = f"{100000 + ((uid+idx)%900000)}"
            is_def = 1 if idx == 0 else 0
            w.writerow([addr_id, uid, line, city, state, pincode, is_def])
            addr_id += 1
TOTAL_ADDRESSES = addr_id - 1

# 3) categories.csv
with open(os.path.join(OUT_DIR, "categories.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["category_id","name"])
    for cid in range(1, CATEGORIES+1):
        w.writerow([cid, f"Category {cid}"])

# 4) products.csv
with open(os.path.join(OUT_DIR, "products.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["product_id","name","description","brand","price","active"])
    brands = ["BrandA","BrandB","BrandC","BrandD","BrandE","BrandF","BrandG","BrandH","BrandI","BrandJ"]
    for pid in range(1, PRODUCTS+1):
        name = f"Product {pid}"
        desc = f"Description for product {pid}"
        brand = brands[pid % len(brands)]
        price = round( ( (pid % 1000) * 0.75 ) + 49.99, 2)
        active = 1
        w.writerow([pid, name, desc, brand, price, active])

# 5) product_categories.csv (1-3 categories per product)
with open(os.path.join(OUT_DIR, "product_categories.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["product_id","category_id"])
    for pid in range(1, PRODUCTS+1):
        choices = 1 + (pid % 3)
        for k in range(choices):
            cid = ((pid + k) % CATEGORIES) + 1
            w.writerow([pid, cid])

# 6) warehouses.csv
with open(os.path.join(OUT_DIR, "warehouses.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["warehouse_id","name","location"])
    for wid in range(1, WAREHOUSES+1):
        w.writerow([wid, f"WH-{wid}", f"City-{wid}"])

# 7) inventory.csv (product × warehouse)
with open(os.path.join(OUT_DIR, "inventory.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["inventory_id","product_id","warehouse_id","quantity","updated_at"])
    iid = 1
    for pid in range(1, PRODUCTS+1):
        for wid in range(1, WAREHOUSES+1):
            qty = (pid * wid) % 500
            updated = dt_str((pid + wid) % 800)
            w.writerow([iid, pid, wid, qty, updated])
            iid += 1

# 8) orders.csv
with open(os.path.join(OUT_DIR, "orders.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["order_id","user_id","address_id","status","total_amount","created_at"])
    for oid in range(1, ORDERS+1):
        uid = ((oid - 1) % USERS) + 1
        # pick a default address for that user: address id is roughly user_id * avg_addr
        # to find a valid address_id for user, we compute offset: first address for user = sum of previous counts + 1
        # For simplicity we compute address_id as: base = (uid -1) * 2 + 1  (since avg 2 addresses)
        base_addr = (uid - 1) * 2 + 1
        address_id = base_addr + (oid % 2)   # choose 1 or 2
        status_options = ['CREATED','PAID','SHIPPED','DELIVERED','CANCELLED','REFUNDED']
        status = status_options[oid % len(status_options)]
        total = round( ((oid % 100) * 5.5) + 99.99, 2)
        created = dt_str(oid % 2000)
        w.writerow([oid, uid, address_id, status, total, created])

# 9) order_items.csv
with open(os.path.join(OUT_DIR, "order_items.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["order_item_id","order_id","product_id","quantity","price"])
    oi_id = 1
    for oid in range(1, ORDERS+1):
        items = 1 + (oid % MAX_ITEMS_PER_ORDER)
        for j in range(items):
            pid = ((oid * (j+1)) % PRODUCTS) + 1
            qty = 1 + ((oid + j) % 3)
            price = round( ((pid % 1000) * 0.75) + 49.99, 2)
            w.writerow([oi_id, oid, pid, qty, price])
            oi_id += 1

# 10) payments.csv (one per paid/shipped/delivered order)
with open(os.path.join(OUT_DIR, "payments.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["payment_id","order_id","amount","method","status","transaction_ref","created_at"])
    pay_id = 1
    for oid in range(1, ORDERS+1):
        # simple rule: if order status index in sequence is 1..3 => create payment
        idx = oid % 6
        if idx in (1,2,3):  # PAID/SHIPPED/DELIVERED roughly
            amount = round( ((oid % 100) * 5.5) + 99.99, 2)
            method = ['CARD','UPI','NETBANKING','WALLET'][oid % 4]
            status = 'SUCCESS' if (oid % 50) != 0 else 'FAILED'
            tx = f"TXN{pay_id:012d}"
            created = dt_str( (oid % 2000) + 1 )
            w.writerow([pay_id, oid, amount, method, status, tx, created])
            pay_id += 1

# 11) shipments.csv (for shipped/delivered orders)
with open(os.path.join(OUT_DIR, "shipments.csv"), "w", newline='') as f:
    w = csv.writer(f)
    w.writerow(["shipment_id","order_id","warehouse_id","carrier","tracking_number","status","shipped_at","delivered_at"])
    ship_id = 1
    carriers = ['BlueX','QuickShip','FlyLog','ShipMate','LocalCourier','RoadRunner']
    for oid in range(1, ORDERS+1):
        idx = oid % 6
        if idx in (2,3):  # SHIPPED or DELIVERED in pattern
            wid = ((oid - 1) % WAREHOUSES) + 1
            carrier = carriers[oid % len(carriers)]
            trk = f"TRK{ship_id:012d}"
            status = 'DELIVERED' if (oid % 3 == 0) else 'IN_TRANSIT'
            shipped_at = dt_str((oid % 2000) + 2)
            delivered_at = dt_str((oid % 2000) + 5) if status == 'DELIVERED' else ''
            w.writerow([ship_id, oid, wid, carrier, trk, status, shipped_at, delivered_at])
            ship_id += 1

print("CSV generation complete in folder:", OUT_DIR)
print("Files:", ", ".join(sorted(os.listdir(OUT_DIR))))
print("Counts: USERS=%d PRODUCTS=%d ORDERS=%d" % (USERS, PRODUCTS, ORDERS))

