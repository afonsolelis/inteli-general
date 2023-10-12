from confluent_kafka import Producer
from faker import Faker
import json

# Configurações do Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'client.id': 'estoque-producer'
}

# Criar o produtor Kafka
producer = Producer(conf)

# Tópico para enviar mensagens
topic = 'topic_review'

# Criar uma instância da classe Faker
fake = Faker()

# Função para gerar dados de estoque fictícios em JSON usando Faker
def generate_stock_data():
    product = fake.word()
    quantity = fake.random_int(min=1, max=100)
    price = fake.random_number(digits=2) / 100  # Criar preço com duas casas decimais
    timestamp = fake.unix_time()
    stock_data = {
        'product': product,
        'quantity': quantity,
        'price': price,
        'timestamp': timestamp
    }
    return json.dumps(stock_data)

# Simular a ingestão de 10.000 dados de estoque fictícios via fila Kafka
for _ in range(10000):
    stock_data = generate_stock_data()
    # Enviar dados de estoque para o tópico
    producer.produce(topic, key='key', value=stock_data)
    producer.flush()

print('Envio de dados de estoque concluído.')
