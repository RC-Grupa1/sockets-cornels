import socket

HOST = "0.0.0.0"
PORT = 1234

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print("Server pornit, asteapta conexiuni...")

while True:
    conn, addr = server.accept()
    print(f"Conectat de la {addr}")

    data = conn.recv(1024).decode()
    if not data:
        conn.close()
        continue

    print(f"Am primit: {data}")

    response = str(int(data) + 1)
    conn.send(response.encode())

    conn.close()
