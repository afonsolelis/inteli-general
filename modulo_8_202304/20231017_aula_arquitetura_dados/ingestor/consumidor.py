from confluent_kafka import Consumer, KafkaError

# Configurações do Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'group.id': 'my_consumer_group',  # Identificador do grupo de consumidores
    'auto.offset.reset': 'earliest'  # Configuração para consumir todas as mensagens desde o início do tópico
}

# Criar o consumidor Kafka
consumer = Consumer(conf)

# Tópico para consumir mensagens
topic = 'topic_review'

# Subscrever ao tópico
consumer.subscribe([topic])

# Esperar mensagens e imprimir no terminal
while True:
    msg = consumer.poll(1.0)  # Esperar por 1 segundo por mensagens

    if msg is None:
        continue
    if msg.error():
        # Lidar com erros
        if msg.error().code() == KafkaError._PARTITION_EOF:
            # Fim da partição (não há mais mensagens)
            continue
        else:
            print(msg.error())
            break

    # Imprimir a mensagem recebida no terminal
    print('Mensagem recebida: {}'.format(msg.value().decode('utf-8')))
