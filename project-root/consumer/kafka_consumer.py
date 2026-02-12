
def insert_to_mysql(conn, data):
    cursor = conn.cursor()
    if data.get('type') == 'customer':
        sql = """INSERT IGNORE INTO customers 
                 (mongo_id, type, customerNumber, customerName, contactLastName, contactFirstName, 
                  phone, addressLine1, addressLine2, city, state, postalCode, country, 
                  salesRepEmployeeNumber, creditLimit) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (
            data.get('_id'), data.get('type'), data.get('customerNumber'),
            data.get('customerName'), data.get('contactLastName'), data.get('contactFirstName'),
            data.get('phone'), data.get('addressLine1'), data.get('addressLine2'),
            data.get('city'), data.get('state'), data.get('postalCode'),
            data.get('country'), data.get('salesRepEmployeeNumber'), data.get('creditLimit')
        )
        cursor.execute(sql, values)

    elif data.get('type') == 'order':
        sql = """INSERT IGNORE INTO orders 
                 (mongo_id, type, orderNumber, orderDate, requiredDate, shippedDate, 
                  status, comments, customerNumber) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

        values = (
            data.get('_id'), data.get('type'), data.get('orderNumber'),
            data.get('orderDate'), data.get('requiredDate'), data.get('shippedDate'),
            data.get('status'), data.get('comments'), data.get('customerNumber')
        )
        cursor.execute(sql, values)

    conn.commit()
    cursor.close()