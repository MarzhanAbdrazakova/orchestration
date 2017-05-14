# orchestration

rest.py:
this is a code, which initializes a network, and makes changes of port forwarding into flow table.

client.py:
this file consist of code running on client side, which offers client to enter some math expression to calculate.

main_service.py:
this is a code of central agent, which orchestrate other services by sending them HTTP POST requests and getting response. 
this app is running on 4900 port on h2 IP address.

multiply.py, divide.py, minus.py, plus.py:
a math services which receive a math expression, perform an operation with first 2 arguments, rewrite a dictionary,
replacing these 2 arguments with a result. Sends dict back as a JSON to the main_service.py.
These services are running on different ports on h2 IP address.

