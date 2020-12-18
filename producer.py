from kafka import KafkaProducer
brokers = ['localhost:' str(i) for in in range(9092, 9095)]
producer = KafkaProducer(bootstrap_servers=brokers)
for i in range(10000):
  producer.send('Topic1', b'message: %d' % i)
producer.flush()
producer = KafkaProducer(retries=5)
