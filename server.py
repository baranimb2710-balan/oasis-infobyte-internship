import socket
import threading
import datetime

clients = []

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message)
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    print(f"[INFO] {addr} connected.")
    while True:
        try:
            msg = client_socket.recv(1024)
            if not msg:
                break
            broadcast(msg, client_socket)
        except:
            break
    print(f"[INFO] {addr} disconnected.")
    clients.remove(client_socket)
    client_socket.close()
    broadcast(f"[System] {addr} has left the chat.".encode(), client_socket)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(2)
    print("[INFO] Server started on localhost:5555")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        client_socket.send("[System] Connected to server.".encode())
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
