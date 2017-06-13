# orchestration

rest.py:
initializes a network, and makes changes of port forwarding into flow table.

client.py:
this file consist of code running on client side, which offers client to enter some math expression to calculate.

main_service.py:
this is a code of central agent, which orchestrate other services by sending them HTTP POST requests and getting response. 
this app is running on 4900 port on h2 IP address.

multiply.py, divide.py, minus.py, plus.py:
a math services which receive a math expression, perform an operation with first 2 arguments, rewrite a dictionary,
replacing these 2 arguments with a result. Sends dict back as a JSON to the main_service.py.
These services are running on different ports on h2 IP address.

1) run ofctl_rest.py app on ryu controller:
 > ryu-manager –verbose ryu.app.ofctl_rest
2) run rest.py script and enter port values
 > python ./rest.py
3) start xterms for hosts:
 > xterm h1,...
4) run main_service.py and microservices on different port of h2
5) on client side (h1) enter math expression ang get reply from main_service.py
6) check output of flow table:
 > curl -X GET http://localhost:8080/stats/flow/1


