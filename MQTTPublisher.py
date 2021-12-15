import paho.mqtt.client as mqtt
from time import sleep
 
 
# topicos providos por este sensor
TOPIC = "victor/mqtt"
 
# cria um identificador baseado no id do sensor
client = mqtt.Client(client_id = 'PythonPublisher',
                     protocol = mqtt.MQTTv31)
# conecta no broker
client.connect("127.0.0.1", 1883)
 
for i in range(1):
    # envia a publicação
    message = "Hello from Python " + str(i)
    client.publish(TOPIC,payload=message,qos=0)
    print (message)
    sleep(5)