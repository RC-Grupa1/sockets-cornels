import socket

SERVER_IP = "100.85.159.89"   # IP-ul Tailscale al serverului
PORT = 1234

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Mă conectez la server...")
client.connect((SERVER_IP, PORT))

value = 1
print(f"Trimit: {value}")

client.send(str(value).encode())

response = client.recv(1024).decode()
print(f"Răspuns de la server: {response}")

client.close()
