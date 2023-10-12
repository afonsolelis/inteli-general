# Use an official Kafka runtime as a parent image
FROM wurstmeister/kafka:latest

# Expose Kafka ports
EXPOSE 9092 9093

# Set environment variables for Kafka
ENV KAFKA_ADVERTISED_LISTENERS INSIDE://kafka:9092,OUTSIDE://localhost:9093
ENV KAFKA_LISTENER_SECURITY_PROTOCOL_MAP INSIDE:PLAINTEXT,OUTSIDE:PLAINTEXT
ENV KAFKA_LISTENERS INSIDE://0.0.0.0:9092,OUTSIDE://0.0.0.0:9093
ENV KAFKA_INTER_BROKER_LISTENER_NAME INSIDE
ENV KAFKA_ZOOKEEPER_CONNECT zookeeper:2181
ENV KAFKA_CREATE_TOPICS topic_name:1:1

# Command to run Kafka
CMD ["start-kafka.sh"]

# docker build -t meu-servico-kafka .
# docker run -d --name meu-kafka-container meu-servico-kafka
