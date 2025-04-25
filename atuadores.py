
import socket

HOST = 'localhost'
PORT = 6000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
sock.bind((HOST, PORT))
sock.listen(1)

print("[Atuador] Aguardando conexão do Gateway...")
conn, addr = sock.accept()
print(f"Conectado por {addr}")

while True:
    comando = conn.recv(1024).decode()
    if not comando:
        break
    print(f"[Atuador] Comando recebido: {comando}")

conn.close()
