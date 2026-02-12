from connection import cursor


def top_10_customers():
    query = """
        SELECT c.customerName, COUNT(o.orderNumber)
        FROM orders o
        JOIN customers c
            ON o.customerNumber = c.customerNumber
        GROUP BY c.customerNumber
        ORDER BY COUNT(o.orderNumber) DESC
        LIMIT 10
        """

    cursor.execute(query)
    results = cursor.fetchall()
    return results