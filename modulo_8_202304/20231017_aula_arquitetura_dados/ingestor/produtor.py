from confluent_kafka import Producer

# Configurações do Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'client.id': 'python-producer'
}

# Função de callback para confirmação de entrega
def delivery_report(err, msg):
    if err is not None:
        print('Erro ao enviar a mensagem: {}'.format(err))
    else:
        print('Mensagem enviada com sucesso para o tópico {} [{}]'.format(msg.topic(), msg.partition()))

# Criar o produtor Kafka
producer = Producer(conf)

# Tópico para enviar a mensagem
topic = 'topic_review'

# Enviar a mensagem para o tópico
producer.produce(topic, key=None, value='Olá, mundo!', callback=delivery_report)

# Esperar a entrega de todas as mensagens
producer.flush()
