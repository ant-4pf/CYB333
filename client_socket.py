import socket
HOST = '127.0.0.1'
PORT = 65432

def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            message = "Hello there!"
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
    except Exception as e: 
        print(f"An error occured: {e}")
        

if __name__ == "__main__":
    start_client()