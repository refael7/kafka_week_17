import json
from mysql_connection import mysql_conn
from schma import create_tables
from kafka_consumer import insert_to_mysql
from confluent_kafka import Consumer

conf = {
    'bootstrap.servers': 'kafka:9092',
    'group.id': 'intelligence_workers',
    'auto.offset.reset': 'earliest'
}

if __name__ == "__main__":
    db_conn = mysql_conn()

    create_tables(db_conn)

    consumer = Consumer(conf)
    consumer.subscribe(['order_data'])

    print("Consumer started, waiting for messages...")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None: continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            data = json.loads(msg.value().decode('utf-8'))
            insert_to_mysql(db_conn, data)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
        db_conn.close()