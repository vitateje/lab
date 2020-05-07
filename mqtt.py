import paho.mqtt.client as mqtt
from time import sleep

TOPICO = "testes/primeiro"

client = mqtt.Client()

client.connect("test.mosquitto.org",1883,60)

while True:
	# codificando o payload
	st = "ola-Vitor-1801745"
	payload = st.encode()
	# envia a publicação
	client.publish(TOPICO, payload, qos=0)
	print(TOPICO + "" + payload.decode())
	
	sleep(5)