from kafka import KafkaConsumer

consumer = KafkaConsumer('bienvenida', bootstrap_servers=['localhost:9092'])
for message in consumer:
    print(message.value.decode('utf-8'))