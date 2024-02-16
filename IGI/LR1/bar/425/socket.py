import socket

# creating server socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 5001))
sock.listen()

# create client socket and establish connection beetwen them
# while it is True, they are connected
while True:
    print('Before .accept()')
    client, addr = sock.accept()
    print(f'Connection from {addr}')

    while True:
        print('Before .recv()')
        request = client.recv(4096)

        if not request:
            break
        else:
            response = 'Hello World!\n'.encode()
            client.send(response)
