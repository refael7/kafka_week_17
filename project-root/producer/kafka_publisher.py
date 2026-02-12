from mongo_connection import collection, producer, TOPIC_NAME
import json
import time


def stream_from_mongo():
    while True:
        batch = list(collection.find().limit(30).skip(30))

        if not batch:
            print("Everything went up.")
            break

        for document in batch:
            document['_id'] = str(document['_id'])

            producer.produce(
                TOPIC_NAME,
                value=json.dumps(document).encode('utf-8'))

            time.sleep(0.5)
            producer.poll(0)
        producer.flush()


if __name__ == "__main__":
    stream_from_mongo()