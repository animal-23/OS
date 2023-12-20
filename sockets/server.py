import socket

server_socket = socket.socket()

server_socket.listen(5)
print("Server is listening to connections")

try:
    while True:
        client_socket,client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        client_socket.send(b"Hello, client! This is server.")

        data = client_socket.recv(1024)
        print(f"Recieved from client: {data.decode()}")

except KeyboardInterrupt:
    print("Keyboard interrupt recieved. Ending the processs")

finally:
    client_socket.close()
    server_socket.close()