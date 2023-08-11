from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
producer.send('bienvenida', b'jem este es mi hola mundo')
producer.flush()