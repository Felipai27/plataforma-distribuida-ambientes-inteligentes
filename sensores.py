
import socket
import time
import random

HOST = 'localhost'
PORT = 5000
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP

while True:
    temperatura = random.uniform(20.0, 30.0)
    luminosidade = random.randint(200, 800)  # lux
    presenca = random.choice([True, False])

    mensagem = f"temperatura:{temperatura:.2f};luminosidade:{luminosidade};presenca:{presenca}"
    sock.sendto(mensagem.encode(), (HOST, PORT))
    print(f"[Sensor] Enviado: {mensagem}")
    time.sleep(5)
