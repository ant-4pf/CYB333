#Import Socket Library
import socket
#Define Host and Port
HOST = 'scanme.nmap.org'
PORT = 65432
#Create TCP/IP Socket and Start Server
def start_server():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            #Bind socket and port, then listen for incoming connections
            s.bind((HOST, PORT))
            s.listen()
            print(f"Server is listening on {HOST}:{PORT}")
            conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True: 
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received data: {data.decode()}")
                conn.sendall(data)
    except Exception as e: 
        print(f"An error occured: {e}")

if __name__ == "__main__":
    start_server()
            
    


