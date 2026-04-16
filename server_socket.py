#Import Socket Library
import socket
import threading
#Define Host and Port
HOST = '127.0.0.1'
PORT = 65432
#Create TCP/IP Socket and Start Server
def start_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #Bind socket and port, then listen for incoming connections
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server is listening on {HOST}:{PORT}")
            while True:
                conn, addr = s.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
    except Exception as e: 
        print(f"An error occurred: {e}")

def handle_client(conn, addr):
    with conn:
        print(f"Connected by {addr}")
        while True: 
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received data: {data.decode()}")
            conn.sendall(data)

if __name__ == "__main__":
    start_server()
            
    


