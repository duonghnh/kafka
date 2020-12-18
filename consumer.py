from kafka import KafkaConsumer
brokers = ['localhost:' + str(i) for i in range(9092, 9095)]
consumer = KafkaConsumer('Topic1',bootstrap_servers=brokers,auto_offset_reset='earliest')
for message in consumer:
  print("%s: partition=%d offset=%d value=%s" % (message.topic, message.partition,message.offset,message.value))
 
