from flask import Flask
from confluent_kafka import Producer, Consumer

app = Flask(__name__)

# Configurações do Kafka
KAFKA_BROKER = 'localhost:9092'  # Endereço e porta do broker Kafka
KAFKA_TOPIC = 'meu-topico'  # Nome do tópico Kafka

# Configurações do produtor Kafka
producer_config = {
    'bootstrap.servers': KAFKA_BROKER,
}

# Configurações do consumidor Kafka
consumer_config = {
    'bootstrap.servers': KAFKA_BROKER,
    'group.id': 'my-group',
    'auto.offset.reset': 'earliest'  # Consumir mensagens desde o início do tópico
}

@app.route('/')
def index():
    # Envia mensagem para o Kafka
    producer = Producer(producer_config)
    producer.produce(KAFKA_TOPIC, key='chave', value='Olá, Mundo!')
    producer.flush()

    # Consome mensagem do Kafka
    consumer = Consumer(consumer_config)
    consumer.subscribe([KAFKA_TOPIC])

    msg = consumer.poll(1.0)
    if msg is not None:
        return f'Mensagem recebida: {msg.value().decode("utf-8")}'
    else:
        return 'Nenhuma mensagem recebida.'

if __name__ == '__main__':
    app.run(debug=True)
