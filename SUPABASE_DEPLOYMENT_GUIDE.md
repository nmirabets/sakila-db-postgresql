# 🚀 Sakila Database Deployment Guide for Supabase

## ✅ Complete Step-by-Step Deployment Instructions

This guide will help you successfully deploy the complete Sakila sample database to Supabase using the SQL Editor.

---

## 🏗️ **Before You Begin**

**First, you'll need to create a Supabase account and project:**

1. Go to https://supabase.com/dashboard
2. Sign up for a free account (if you don't have one)
3. Create a new project
4. Wait for your project to be fully provisioned

Once your project is ready, you can proceed with the deployment steps below.


---

## 📋 **Prerequisites**

- ✅ **Supabase Project**: Created and accessible
- ✅ **SQL Editor Access**: Can access Supabase SQL Editor in your project
- ✅ **All Required Files**: Ensure you have all 9 deployment files listed below

---

## 📁 **Required Files (In Deployment Order)**

You should have these **9 files** ready for deployment:

1. `sakila_schema_00_create_schema.sql` - Database schema
2. `sakila_data_01_base_data.sql` - Base lookup data  
3. `sakila_data_02_location_data.sql` - Location data
4. `sakila_data_03_film_data.sql` - Film data
5. `sakila_data_04_staff_store_customer.sql` - Staff, store, customer, inventory
6. `sakila_data_05a_rental_data_part1.sql` - Rental data (first half)
7. `sakila_data_05b_rental_data_part2.sql` - Rental data (second half)
8. `sakila_data_06a_payment_data_part1.sql` - Payment data (first half)
9. `sakila_data_06b_payment_data_part2.sql` - Payment data (second half)

---

## 🎯 **Deployment Steps**

### **Step 1: Schema Creation**
```sql
-- File: sakila_schema_postgresql.sql
-- Size: ~550 lines
-- Creates: 16 tables, indexes, functions, triggers, views
```

1. Open **Supabase SQL Editor**
2. Copy the entire contents of `sakila_schema_00_create_schema.sql`
3. Paste into SQL Editor
4. Click **"Run"**
5. ✅ **Verify**: All 16 tables created successfully

---

### **Step 2: Base Data**
```sql
-- File: sakila_data_01_base_data.sql  
-- Size: ~380 lines
-- Populates: actor, category, country, language
```

1. Copy the entire contents of `sakila_data_01_base_data.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: 4 base tables populated

---

### **Step 3: Location Data**
```sql
-- File: sakila_data_02_location_data.sql
-- Size: ~1,230 lines  
-- Populates: city, address
-- Depends on: country (from Step 2)
```

1. Copy the entire contents of `sakila_data_02_location_data.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: City and address tables populated

---

### **Step 4: Film Data**
```sql
-- File: sakila_data_03_film_data.sql
-- Size: ~7,508 lines
-- Populates: film, film_actor, film_category
-- Depends on: language, actor, category (from previous steps)
```

1. Copy the entire contents of `sakila_data_03_film_data.sql`
2. Paste into SQL Editor  
3. Click **"Run"**
4. ✅ **Verify**: Film-related tables populated

---

### **Step 5: Staff, Store, Customer & Inventory**
```sql
-- File: sakila_data_04_staff_store_customer.sql
-- Size: ~5,240 lines
-- Populates: staff, store, customer, inventory
-- Depends on: address, film (from previous steps)
-- Special: Handles circular dependency between staff ↔ store
```

1. Copy the entire contents of `sakila_data_04_staff_store_customer.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: Staff, store, customer, and inventory tables populated

---

### **Step 6: Rental Data (Part 1)**
```sql
-- File: sakila_data_05a_rental_data_part1.sql
-- Size: ~8,040 lines (~660KB)
-- Populates: rental table (records 1-8014)
-- Depends on: inventory, customer, staff (from Step 5)
```

1. Copy the entire contents of `sakila_data_05a_rental_data_part1.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: First half of rental data inserted

---

### **Step 7: Rental Data (Part 2)**
```sql
-- File: sakila_data_05b_rental_data_part2.sql
-- Size: ~8,055 lines (~660KB)
-- Populates: rental table (records 8015-16049)
-- Continues from: Part 1 (Step 6)
```

1. Copy the entire contents of `sakila_data_05b_rental_data_part2.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: Complete rental data inserted (16,049 records total)

---

### **Step 8: Payment Data (Part 1)**
```sql
-- File: sakila_data_06a_payment_data_part1.sql
-- Size: ~8,037 lines (~550KB)
-- Populates: payment table (records 1-8017)
-- Depends on: rental, customer, staff (from previous steps)
```

1. Copy the entire contents of `sakila_data_06a_payment_data_part1.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: First half of payment data inserted

---

### **Step 9: Payment Data (Part 2) - FINAL**
```sql
-- File: sakila_data_06b_payment_data_part2.sql
-- Size: ~8,051 lines (~550KB)
-- Populates: payment table (records 8018-16049)
-- Continues from: Part 1 (Step 8)
```

1. Copy the entire contents of `sakila_data_06b_payment_data_part2.sql`
2. Paste into SQL Editor
3. Click **"Run"**
4. ✅ **Verify**: Complete payment data inserted (16,049 records total)

---

## 🎉 **Deployment Complete!**

### **Final Database Stats:**
- ✅ **16 Tables**: All populated with sample data
- ✅ **~46,000 Records**: Complete Sakila dataset
- ✅ **All Relationships**: Foreign keys and constraints working
- ✅ **PostgreSQL Optimized**: Functions, triggers, views operational

---

## ✅ **Verification & Testing**

### **Step 1: SQL Editor Verification**

Run these queries in Supabase SQL Editor to verify successful deployment:

```sql
-- Test a complex query (joins multiple tables)
SELECT 
    c.first_name || ' ' || c.last_name as customer_name,
    f.title as film_title,
    p.amount as payment_amount,
    r.rental_date
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id  
JOIN film f ON i.film_id = f.film_id
JOIN payment p ON r.rental_id = p.rental_id
ORDER BY r.rental_date DESC
LIMIT 5;
```

### **Step 2: Python Connection Test**

After successful SQL verification, test your database connection using Python:

#### **2.1 Install Python Dependencies**
```bash
# Install required packages
pip install -r requirements.txt
```

#### **2.2 Set Up Environment Variables**
Create a `.env` file in your project root with your Supabase credentials:

```env
# Option 1: Use full connection string (recommended)
SUPABASE_CONNECTION_STRING=postgresql://postgres:[your-password]@[your-host]:[port]/postgres

# Option 2: Or use individual components
SUPABASE_DB_URL=[your-supabase-db-url]
SUPABASE_DB_PASSWORD=[your-password]
```

**To get your connection details:**
1. Go to your Supabase project dashboard
2. Navigate to **Settings** → **Database**
3. Copy the connection string or individual components

#### **2.3 Run the Test Function**
```bash
# Test database connection and query
python test-function.py
```

**Expected Output:**
```
SELECT * FROM actor
     actor_id first_name last_name      last_update
0           1   PENELOPE   GUINESS  2006-02-15 09:34:33
1           2       NICK  WAHLBERG  2006-02-15 09:34:33
2           3         ED     CHASE  2006-02-15 09:34:33
3           4   JENNIFER     DAVIS  2006-02-15 09:34:33
...
```

✅ **Success**: If you see actor data displayed, your Sakila database is properly deployed and accessible!

---

## 🛡️ **Safety Features**

### **Built-in Protections:**
- ✅ **Duplicate Protection**: `ON CONFLICT DO NOTHING` prevents duplicate key errors
- ✅ **Dependency Handling**: Files ordered to respect foreign key constraints  
- ✅ **Circular Dependencies**: Staff ↔ Store handled with session replication role
- ✅ **No Truncation Issues**: Safe INSERT-only approach
- ✅ **Idempotent**: Can be run multiple times without issues

---

## 🔧 **Troubleshooting**

### **If You Get Errors:**

1. **"File too large"**: 
   - ✅ Already solved - all files are under 660KB

2. **"Foreign key violation"**:
   - ✅ Follow exact order above
   - ✅ Don't skip any files

3. **"Duplicate key error"**:
   - ✅ Already handled with ON CONFLICT clauses
   - ✅ Safe to re-run any file

4. **"Table doesn't exist"**:
   - ✅ Ensure Step 1 (schema) completed successfully
   - ✅ Check for any schema creation errors

---

## 💡 **Pro Tips**

1. **Copy-Paste Method**: Use copy-paste rather than file upload for best results
2. **One File at a Time**: Complete each step before moving to the next
3. **Verify Each Step**: Run verification queries after each major step
4. **Test with Python**: Use `test-function.py` to verify your database connection works programmatically
5. **Environment Setup**: Always create your `.env` file before running the Python test
6. **Safe to Restart**: If something fails, you can re-run from any step
7. **Keep Files**: Maintain these files for future database refreshes

---

## 🎯 **Your Database is Ready!**

After completing all 9 steps, you'll have a **fully functional Sakila database** in Supabase, perfect for:

- 📊 **Data Analysis & Visualization**
- 🔍 **SQL Query Practice**  
- 🚀 **Application Development**
- 📈 **ML Dashboard Projects**

**Happy coding!** 🎉
