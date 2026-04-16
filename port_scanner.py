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
        ports = [20,21,22,23,25,53,80,110,143,443,3306,3389]
        for port in ports:
            if lowerport <= port <= upperport:
                print(f"Scanning port {port}...")
                if self.is_open(port):
                    self.add_port(port)
                else: 
                    print(f"Port {port} is closed.")
    
    def write(self, filepath):
        if not self.open_ports:
            print("No open ports found.")
            return
        openport = [f"Port {port} is open" for port in self.open_ports]
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))

    
def main():
    ip = 'scanme.nmap.org'
    scanner = Scanner(ip)
    scanner.scan(20,450)
    scanner.write('open_ports.txt')
    

if __name__ == "__main__":
    main()


