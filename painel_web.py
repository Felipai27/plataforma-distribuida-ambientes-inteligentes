from flask import Flask, render_template_string
from kafka import KafkaConsumer
import threading

app = Flask(__name__)
dados_sensores = []

# Consumidor Kafka rodando em thread separada
def consumir_kafka():
    global dados_sensores
    consumer = KafkaConsumer(
        'topico_sensores',
        bootstrap_servers='localhost:9092',
        group_id='painel_web'
    )
    for mensagem in consumer:
        dados_sensores.append(mensagem.value.decode())
        if len(dados_sensores) > 10:  # Mostra só os últimos 10 registros
            dados_sensores.pop(0)

threading.Thread(target=consumir_kafka, daemon=True).start()

# Página web
TEMPLATE = """
<!doctype html>
<title>Painel de Monitoramento</title>
<h1>Leituras dos Sensores</h1>
<ul>
  {% for dado in dados %}
    <li>{{ dado }}</li>
  {% endfor %}
</ul>
<meta http-equiv="refresh" content="5">
"""

@app.route('/')
def index():
    return render_template_string(TEMPLATE, dados=dados_sensores)

if __name__ == '__main__':
    app.run(debug=True)
