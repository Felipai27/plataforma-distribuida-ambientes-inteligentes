
from kafka import KafkaProducer
import socket

producer = KafkaProducer(bootstrap_servers='localhost:9092')

UDP_IP = 'localhost'
UDP_PORT = 5000
sock_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_udp.bind((UDP_IP, UDP_PORT))

TCP_IP = 'localhost'
TCP_PORT = 6000
sock_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_tcp.connect((TCP_IP, TCP_PORT))

print("[Gateway] Aguardando dados dos sensores...")

while True:
    data, addr = sock_udp.recvfrom(1024)
    mensagem = data.decode()
    print(f"[Gateway] Dado recebido: {mensagem}")

    producer.send('topico_sensores', mensagem.encode())
    print("[Gateway] Dado enviado para Kafka.")

    dados = dict(item.split(":") for item in mensagem.split(";"))
    temperatura = float(dados['temperatura'])
    presenca = dados['presenca'] == 'True'

    if temperatura > 25.0 and presenca:
        comando = "LIGAR_AR_CONDICIONADO"
        sock_tcp.send(comando.encode())
        print(f"[Gateway] Comando enviado ao atuador: {comando}")
    elif temperatura <= 23.0 and presenca:
        comando = "DESLIGAR_AR_CONDICIONADO"
        sock_tcp.send(comando.encode())
        print(f"[Gateway] Comando enviado ao atuador: {comando}")
