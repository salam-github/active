import socket
import sys
from argparse import ArgumentParser

def scan_port(host, port, protocol='tcp'):
    try:
        if protocol == 'tcp':
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            sock.close()
        elif protocol == 'udp':
            # UDP scanning is atm less reliable and requires sending data to the port and waiting for a response
            # This is a veeeery basic implementation and may not accurately reflect the open/closed state of UDP ports
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(1)
            try:
                sock.sendto(b'', (host, port))  # Sending empty bytes
                data, _ = sock.recvfrom(1024)
                print(f"Port {port}/UDP is open/filtered")
            except socket.timeout:
                print(f"Port {port}/UDP is open/filtered (no response)")
            except Exception as e:
                print(f"Port {port}/UDP is closed or blocked")
            sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {str(e)}")

def main():
    parser = ArgumentParser(description="TinyScanner: A simple port scanner")
    parser.add_argument("host", help="The host to scan")
    parser.add_argument("port", help="Single port or range of ports to scan (e.g., 80 or 20-80)")
    parser.add_argument("-u", "--udp", help="Perform a UDP scan", action="store_true")
    parser.add_argument("-t", "--tcp", help="Perform a TCP scan", action="store_true")

    args = parser.parse_args()

    if not args.udp and not args.tcp:
        print("Please specify at least one protocol to scan (-u for UDP, -t for TCP)")
        sys.exit(1)

    # Parse port or port range
    if '-' in args.port:
        start_port, end_port = map(int, args.port.split('-'))
        ports = range(start_port, end_port + 1)
    else:
        ports = [int(args.port)]

    for port in ports:
        if args.tcp:
            scan_port(args.host, port, 'tcp')
        if args.udp:
            scan_port(args.host, port, 'udp')

if __name__ == "__main__":
    main()