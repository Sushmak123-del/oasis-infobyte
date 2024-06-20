import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    # Loop to receive messages from the client
    while True:
        # Receive message from client
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break

        # Print client's message
        print(f"[{client_address}] {message}")

        # Echo the message back to the client
        client_socket.send(message.encode('utf-8'))

    # Close client connection
    print(f"[DISCONNECTED] {client_address} disconnected.")
    client_socket.close()

# Server configuration
server_host = '127.0.0.1'
server_port = 5555

# Create a socket for the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the specified host and port
server.bind((server_host, server_port))

# Start listening for incoming connections
server.listen()

print(f"[LISTENING] Server is listening on {server_host}:{server_port}")

# Main loop to accept incoming connections
while True:
    # Accept a new connection
    client_socket, client_address = server.accept()

    # Create a new thread to handle client communication
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()

import socket

# Client configuration
server_host = '127.0.0.1'
server_port = 5555

# Create a socket for the client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client.connect((server_host, server_port))

# Function to send messages to the server
def send_message():
    while True:
        # Input message from user
        message = input("Type your message: ")

        # Send message to server
        client.send(message.encode('utf-8'))

        # Receive echo message from server
        echo_message = client.recv(1024).decode('utf-8')
        print(f"[RECEIVED] {echo_message}")

# Start sending messages in a separate thread
send_thread = threading.Thread(target=send_message)
send_thread.start()

# Main loop to keep the client running
while True:
    continue
