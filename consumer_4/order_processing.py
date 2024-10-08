import pika
import pymysql
import time
from datetime import datetime

db=pymysql.connect(
	host='host.docker.internal', 
	user='root', 
	password='Dont4get!', 
	db='ims'
	)

cursor=db.cursor()

def connect_to_rabbitmq():
	connection=None
	while connection is None:
		try:
			connection=pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
			channel=connection.channel()
			channel.queue_declare('order_processing_queue')
			print("Connected to rabbitmq")
			return connection, channel
		except pika.exceptions.AMQPConnectionError:
			print("Failed, retrying in 5sec")
			time.sleep(5)

connection, channel=connect_to_rabbitmq()

def callback(ch, method, properties, body):
    order_data = eval(body)
    print(f"Order process data received: {order_data}")

    # Insert order into the database
    query = "INSERT INTO orders (item_id, quantity, customer_name, shipping_address) VALUES (%s, %s, %s, %s)"
    values = (order_data["item_id"], order_data["quantity"], order_data["customer_name"], order_data["shipping_address"])
    cursor.execute(query, values)
    db.commit()
    print("Order placed successfully")

    # Update inventory by decrementing the quantity of the ordered item
    update_query = "UPDATE items SET quantity = quantity - %s WHERE id = %s"
    update_values = (order_data["quantity"], order_data["item_id"])
    cursor.execute(update_query, update_values)
    db.commit()

    print("Inventory updated")


channel.basic_consume(queue='order_processing_queue', on_message_callback=callback, auto_ack=True)
print("Ready to place orders")
channel.start_consuming()