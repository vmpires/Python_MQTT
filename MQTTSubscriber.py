import paho.mqtt.client as mqtt
from struct import unpack
from time import sleep
 
# assinando todas as publicações do topico
TOPIC = "victor/mqtt"
 
# função chamada quando a conexão for realizada, sendo
# então realizada a subscrição
def on_connect(client, data, rc, port):
    client.subscribe([(TOPIC,0)])
 
# função chamada quando uma nova mensagem do tópico é gerada
def on_message(client, userdata, msg):
    # decodificando o valor recebido
    print (msg.payload)
 
# clia um cliente para supervisã0
client = mqtt.Client(client_id = 'SCADA',
                     protocol = mqtt.MQTTv31)
# estabelece as funçõe de conexão e mensagens
client.on_connect = on_connect
client.on_message = on_message
 
# conecta no broker
client.connect("127.0.0.1", 1883)
 
# permace em loop, recebendo mensagens
client.loop_forever()