import socket
import os
from faker import Faker # type: ignore

def main():

    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = './udp_socket_file'

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

    print('starting up on {}'.format(server_address))

    sock.bind(server_address)

    while True:
        print('\nwaiting to receive message')

        data, address = sock.recvfrom(4096)

        print('received {} bytes from {}'.format(len(data), address))
        
        print(data.decode('utf-8'))

        if data:
            new_data = answer(data)
            sent = sock.sendto(new_data, address)
        
            print('sent {} bytes back to {}'.format(sent, address))


def answer(data):
    fake = Faker('jp-JP')
    new_data = data.decode('utf-8')
    if (new_data == "person"):
        answer = fake.name() + '\n' + fake.address()
    elif (new_data == "car-number"):
        answer = "car_number: " + fake.license_plate()
    elif (new_data == "bank-account-number"):
        answer = "bank account No.: " + fake.aba()
    elif (new_data == "mail-address"):
        answer = "mail-adress: " + fake.ascii_safe_email()
    else:
        answer = "No applicable data were found."
    
    b_answer = answer.encode(encoding='utf-8')
    return b_answer

main()