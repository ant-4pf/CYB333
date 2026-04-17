#Import socket library
import socket

#Define Host and Port
HOST = '127.0.0.1'
PORT = 65432

#Create TCP/IP Socket and Start Client
def start_client():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5.0)
            s.connect((HOST, PORT))
            message = "GET / HTTP/1.1\r\nHost: scanme.nmap.org\r\n\r\n" 
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
    #Error handling for connection issues
    except Exception as e: 
        print(f"An error occurred: {e}")
        

if __name__ == "__main__":
    start_client()