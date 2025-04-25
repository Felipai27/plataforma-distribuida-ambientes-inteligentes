from kafka import KafkaConsumer
import grpc
import sensores_pb2
import sensores_pb2_grpc

# Configura o consumidor Kafka
consumer = KafkaConsumer(
    'topico_sensores',
    bootstrap_servers='localhost:9092',
    group_id='grupo_monitoramento'
)

# Conexão com o servidor gRPC
canal = grpc.insecure_channel('localhost:50051')
stub = sensores_pb2_grpc.ArmazenamentoServiceStub(canal)

print("[Consumidor Kafka] Aguardando mensagens...")

# Processa as mensagens do Kafka
for mensagem in consumer:
    dado_recebido = mensagem.value.decode()
    print(f"[Consumidor Kafka] Mensagem recebida: {dado_recebido}")

    # Converte o dado recebido (string) para dict
    dados = dict(item.split(":") for item in dado_recebido.split(";"))

    # Envia para o gRPC
    resposta = stub.EnviarDados(sensores_pb2.DadosSensor(
        temperatura=dados['temperatura'],
        luminosidade=dados['luminosidade'],
        presenca=dados['presenca']
    ))

    print(f"[Consumidor Kafka] Resposta do gRPC: {resposta.mensagem}")
