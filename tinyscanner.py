import socket
import sys
import threading
from argparse import ArgumentParser

def scan_port(host, port, protocol='tcp'):
    try:
        if protocol == 'tcp':
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(1)
                result = sock.connect_ex((host, port))
                if result == 0:
                    try:
                        service = socket.getservbyport(port, 'tcp')
                    except:
                        service = 'Unknown service'
                    print(f"Port {port}/TCP is open | Service: {service}")
                else:
                    print(f"Port {port}/TCP is closed")
        elif protocol == 'udp':
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
                sock.settimeout(1)
                try:
                    # Sending a basic payload - behavior varies by service
                    sock.sendto(b'\0', (host, port))
                    sock.recvfrom(1024)
                    print(f"Port {port}/UDP is open/filtered")
                except socket.timeout:
                    print(f"Port {port}/UDP is open/filtered (no response)")
                except Exception:
                    print(f"Port {port}/UDP is closed or blocked")
    except Exception as e:
        print(f"Error scanning port {port}: {str(e)}")

def start_scan(host, port, protocol):
    thread = threading.Thread(target=scan_port, args=(host, port, protocol))
    thread.start()
    return thread

def main():
    parser = ArgumentParser(description="TinyScanner: A simple port scanner")
    parser.add_argument("host", help="The host to scan")
    parser.add_argument("port", help="Single port or range of ports to scan (e.g., 80 or 20-80)")
    parser.add_argument("-u", "--udp", action="store_true", help="Perform a UDP scan")
    parser.add_argument("-t", "--tcp", action="store_true", help="Perform a TCP scan")

    args = parser.parse_args()

    if not args.udp and not args.tcp:
        print("Please specify at least one protocol to scan (-u for UDP, -t for TCP)")
        sys.exit(1)

    ports = []
    if '-' in args.port:
        start_port, end_port = map(int, args.port.split('-'))
        ports = range(start_port, end_port + 1)
    else:
        ports = [int(args.port)]

    threads = []
    for port in ports:
        if args.tcp:
            threads.append(start_scan(args.host, port, 'tcp'))
        if args.udp:
            threads.append(start_scan(args.host, port, 'udp'))

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()