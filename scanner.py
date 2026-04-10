import socket
class Scanner:
    def __init__(self, ip):
        self.ip = ip 
        self.open_ports = [];

    def __repr__(self):
        return f"Scanner: {self.ip}"
    
    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result =  s.connect_ex((self.ip, port))
        return result == 0
        
    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport,upperport + 1):
            if self.is_open(port):
                self.add_port(port)
    
    def write(self, filename):
        with open(filename, 'w') as f:
            for port in self.open_ports:
                f.write(f"(port{port} is open)\n")

    def main():
        ip = input("Enter the IP Address to scan: ")
        lowerport = int(input("Enter the lower Port Number: "))
        upperport = int(input("Enter the upper port number: "))
        scanner = Scanner(ip)
        scanner.scan(lowerport, upperport)
        print(f"Open ports for {scanner.ip}: {scanner.open_ports}")
        filename = input("Enter the filename to save the results: ")
        scanner.write(filename)

    if __name__ == "__main__":
        main()