import pymongo
import psycopg2
import uuid
from datetime import datetime

# Conectar ao MongoDB
client = pymongo.MongoClient("mongodb://myusername:mypassword@localhost:27017/")
db_mongo = client["seu_banco_de_dados"]  # Substitua "seu_banco_de_dados" pelo nome do seu banco MongoDB
collection_mongo = db_mongo["sua_colecao"]  # Substitua "sua_colecao" pelo nome da sua coleção MongoDB

# Conectar ao PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="mydatabase",  # Substitua pelo nome do seu banco PostgreSQL
    user="myuser",  # Substitua pelo seu nome de usuário PostgreSQL
    password="mypassword"  # Substitua pela sua senha PostgreSQL
)
cur = conn.cursor()

# Criar a tabela se ela não existir
cur.execute("""
    CREATE TABLE IF NOT EXISTS sua_tabela (
        id SERIAL PRIMARY KEY,
        data_ingestao TIMESTAMP,
        value JSONB,
        product_metadata INTEGER,
        organization_id UUID
    )
""")
conn.commit()

# Ler dados do MongoDB e organizar em uma lista de tuplas para inserção no PostgreSQL
data_to_insert = []
for document in collection_mongo.find():
    transformed_data = generate_random_data()
    # Verificar se o documento já foi inserido para evitar duplicatas
    if transformed_data["organization_id"] not in existing_ids:
        data_to_insert.append((
            transformed_data["data_ingestao"],
            transformed_data["value"],
            transformed_data["product_metadata"],
            transformed_data["organization_id"]
        ))

# Inserir dados no PostgreSQL
for record in data_to_insert:
    cur.execute("""
        INSERT INTO sua_tabela (data_ingestao, value, product_metadata, organization_id)
        VALUES (%s, %s, %s, %s)
    """, record)

# Commit e fechar conexões
conn.commit()
cur.close()
conn.close()
