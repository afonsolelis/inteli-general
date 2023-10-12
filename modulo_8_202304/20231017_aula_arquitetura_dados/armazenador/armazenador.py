from confluent_kafka import Consumer, KafkaError
from pymongo import MongoClient

# Configurações do Kafka
conf = {
    'bootstrap.servers': 'localhost:9092',  # Endereço do broker Kafka
    'group.id': 'my_consumer_group',  # Identificador do grupo de consumidores
    'auto.offset.reset': 'earliest'  # Configuração para consumir todas as mensagens desde o início do tópico
}

# Configurações do MongoDB
mongo_client = MongoClient('mongodb://myusername:mypassword@localhost:27017/')  # Conexão ao MongoDB
db = mongo_client['mydatabase']  # Nome do banco de dados
collection = db['mycollection']  # Nome da coleção para armazenar os dados

# Criar o consumidor Kafka
consumer = Consumer(conf)

# Tópico para consumir mensagens
topic = 'topic_review'

# Subscrever ao tópico
consumer.subscribe([topic])

# Esperar mensagens e armazenar no MongoDB
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

    # Obter a mensagem recebida
    mensagem = msg.value().decode('utf-8')

    # Armazenar a mensagem no MongoDB
    collection.insert_one({'mensagem': mensagem})

    # Imprimir a mensagem recebida no terminal (opcional)
    print('Mensagem recebida e armazenada no MongoDB: {}'.format(mensagem))
