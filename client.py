import socket
import threading
import datetime

def receive_messages(sock):
    while True:
        try:
            msg = sock.recv(1024).decode()
            print(msg)
        except:
            print("[System] Disconnected from server.")
            sock.close()
            break

def send_messages(sock, username):
    while True:
        msg = input()
        timestamp = datetime.datetime.now().strftime("%H:%M")
        formatted = f"[{timestamp}] {username}: {msg}"
        sock.send(formatted.encode())

def start_client(username):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 5555))

    thread = threading.Thread(target=receive_messages, args=(sock,))
    thread.start()

    send_messages(sock, username)

if __name__ == "__main__":
    username = input("Enter your username: ")
    start_client(username)
