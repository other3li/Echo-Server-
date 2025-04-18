import socket

HOST = 'localhost'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    message = input("Enter message (e.g., Ahello): ")
    if not message:
        break

    client_socket.send(message.encode())
    response = client_socket.recv(1024).decode()
    print("Server response:", response)

client_socket.close()

