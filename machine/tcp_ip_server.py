__author__ = 'nikaashpuri'
import socket
import sys
import os
sys.path.append('/public_html/aquabrim_project')

from views import collect_data_from_device_using_tcp
from aquabrim_project.settings import BASE_DIR
from views import TCP_SERVER_IP, TCP_SERVER_PORT

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (TCP_SERVER_IP, TCP_SERVER_PORT)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

filename = '/logs/django_log'
f = open(filename, 'a+')
f.close()

# dict to store all connections
dict_device_id_to_connection = {}

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        received_string = connection.recv(1024)
        # Receive the data in small chunks and retransmit it

        # filename = os.path.join(BASE_DIR, 'recieved_log')
        f = open(filename, 'a+')
        f.write(received_string + repr(client_address) + '\n')
        f.close()
        # now either this string has come from the website or from a device
        if received_string.split(" ")[0] == 'send':
            # we have to send this to the device
            # for now we just send this to 123456
            # print dict_device_id_to_connection
            connection = dict_device_id_to_connection['123456']
            connection.sendall(received_string.split(" ")[1])
            pass
        else:
            # we receive this connection
            # Clean up the connection
            # store the connection for future use
            # device_id = received_string.split(" ")[0]
            # first three bytes denote the device id
            device_id = received_string[:3]
            dict_device_id_to_connection[device_id] = connection
            print >>sys.stderr, 'stored the connection for future use... ', received_string
            # connection.close()
            # now send this command to Django
            collect_data_from_device_using_tcp(received_string)

    except Exception as e:
        print >>sys.stderr, "Exception: ", e
        # filename = os.path.join(BASE_DIR, 'recieved_log')
        f = open(filename, 'a+')
        f.write("Exception: " + repr(e) + '\n')
        f.close()

