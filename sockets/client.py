import socket

client_socket = socket.socket()

client_socket.connect(('172.17.180.136',9000))

data = client_socket.recv(1024)
print(f"Recieved from server: {data.decode()}")

client_socket.send(b"Hello, server! This is client.")

client_socket.close()