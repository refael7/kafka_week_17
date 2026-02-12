

def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            mongo_id VARCHAR(255),
            type VARCHAR(50),
            customerNumber INT PRIMARY KEY,
            customerName VARCHAR(255),
            contactLastName VARCHAR(255),
            contactFirstName VARCHAR(255),
            phone VARCHAR(50),
            addressLine1 VARCHAR(255),
            addressLine2 VARCHAR(255),
            city VARCHAR(100),
            state VARCHAR(100),
            postalCode VARCHAR(20),
            country VARCHAR(100),
            salesRepEmployeeNumber INT,
            creditLimit DECIMAL(15, 2)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            mongo_id VARCHAR(255),
            type VARCHAR(50),
            orderNumber INT PRIMARY KEY,
            orderDate DATE,
            requiredDate DATE,
            shippedDate DATE,
            status VARCHAR(50),
            comments TEXT,
            customerNumber INT
        )
    """)
    conn.commit()
    cursor.close()