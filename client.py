import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 1024))
print("message du serveur: ", client_socket.recv(1024).decode("utf-8"))

while True:
    message_to_send = input("Message à envoyer: ")
    client_socket.send(message_to_send.encode("utf-8"))
    if message_to_send == "x":
        break
    
print("fermeture socket")
client_socket.close()
