from concurrent import futures
import grpc
import sensores_pb2
import sensores_pb2_grpc

# Lista para armazenar os dados recebidos
dados_armazenados = []

class ArmazenamentoService(sensores_pb2_grpc.ArmazenamentoServiceServicer):
    def EnviarDados(self, request, context):
        dado = {
            'temperatura': request.temperatura,
            'luminosidade': request.luminosidade,
            'presenca': request.presenca
        }
        dados_armazenados.append(dado)
        print(f"[gRPC Servidor] Dado armazenado: {dado}")
        return sensores_pb2.Resposta(mensagem="Dados armazenados com sucesso!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sensores_pb2_grpc.add_ArmazenamentoServiceServicer_to_server(ArmazenamentoService(), server)
    server.add_insecure_port('[::]:50051')
    print("[gRPC Servidor] Servidor gRPC rodando na porta 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
