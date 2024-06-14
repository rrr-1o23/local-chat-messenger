import socket
import os


sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

server_address = './udp_socket_file'

address = './udp_client_socket_file'

try:
    os.unlink(address)
except FileNotFoundError:
    pass

jp_text = input("What information do you want?\n")
message = jp_text.encode('utf-8')

# print(message.decode('utf-8'))

sock.bind(address)

try:

    sent = sock.sendto(message, server_address)

    print('waiting to receive')

    data, server = sock.recvfrom(4096)

    # print('received {!r}'.format(data))
    print("\n" + data.decode('utf-8'))

finally:
    
    print('\nclosing socket')
    sock.close()