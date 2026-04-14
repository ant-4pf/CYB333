import socket
class Scanner:
    def __init__(self, ip):
        self.ip = ip 
        self.open_ports = []

    def __repr__(self):
        return f"Scanner: {self.ip}"
    
    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result =  s.connect_ex((self.ip, port))
        s.close()
        return result == 0
        
    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport,upperport + 1):
            print(f"Scanning port {port}...")
            if self.is_open(port):
                self.add_port(port)
    
    def write(self, filepath):
        openport = [str(port) for port in self.open_ports]
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))

    
def main():
    ip = '8.8.8.8'
    scanner = Scanner(ip)
    scanner.scan(1,10)
    scanner.write('open_ports.txt')
    

if __name__ == "__main__":
    main()


