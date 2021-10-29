#Biblioteca para Acesso
from netmiko import ConnectHandler

#Informações do Usuario
cisco = { 
'device_type': 'cisco_ios', 
'host': 'sandbox-iosxe-latest-1.cisco.com', 
'username': 'developer', 
'password': 'C1sco12345', 
}  

#Conexão com o elemento
net_connect = ConnectHandler(**cisco)
net_connect.find_prompt()

#Comando Enviado
output = net_connect.send_command("show runn")

with open('cisco.csv','w+', encoding = 'utf-8') as arquivo:
    arquivo.write(output)

