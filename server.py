import socket

HOST = 'localhost'
PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print("Server is listening on port", PORT)

conn, addr = server_socket.accept()
print('Connected by', addr)

while True:
    data = conn.recv(1024).decode()
    if not data:
        break

    command = data[0]
    text = data[1:]

    if command == 'A':
        response = ''.join(sorted(text, reverse=True))
    elif command == 'C':
        response = ''.join(sorted(text))
    elif command == 'D':
        response = text.upper()
    else:
        response = data

    conn.send(response.encode())

conn.close()
server_socket.close()
