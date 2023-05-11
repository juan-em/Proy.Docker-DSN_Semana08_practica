from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('bienvenida', b'Hola Mundo por jem')
producer.flush()