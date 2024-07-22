import socket
import threading
import signal
import sys
import argparse

AUDIT_PORTS = [
    21,  # FTP
    22,  # SSH
    23,  # Telnet
    25,  # SMTP
    53,  # DNS
    80,  # HTTP
    110,  # POP3
    115,  # SFTP
    135,  # RPC
    139,  # NetBIOS
    143,  # IMAP
    194,  # IRC
    443,  # SSL
    445,  # SMB
    1433,  # MSSQL
    3306,  # MySQL
    3389,  # Remote Desktop
    5632,  # PCAnywhere
    5900,  # VNC
    25565  # Minecraft
]

def start_tcp_server(port):
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        try:
            server_socket.bind(('0.0.0.0', port))
        except OSError as e:
            print(f"Error: Could not bind to port {port}. {e}")
            return
        server_socket.listen()
        server_socket.settimeout(1)  # Set timeout for accept operation
        print(f"TCP server listening on port {port}")
        while running:
            try:
                conn, addr = server_socket.accept()
            except socket.timeout:
                continue  # Go back to the top of the loop and check running flag
            except Exception as e:
                break  # Handle other exceptions or break
            with conn:
                print(f"Connected by {addr}")
                # Handle the connection
        print(f"TCP server on port {port} shutting down")

def start_udp_server(port):
    global running
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        try:
            server_socket.bind(('0.0.0.0', port))
        except OSError as e:
            print(f"Error: Could not bind to port {port}. {e}")
            return
        server_socket.settimeout(1)  # Set timeout for recvfrom operation
        print(f"UDP server listening on port {port}")
        while running:
            try:
                data, addr = server_socket.recvfrom(1024)
            except socket.timeout:
                continue  # Go back to the top of the loop and check running flag
            except Exception as e:
                break  # Handle other exceptions or break
            print(f"Received message from {addr}")
            # Handle data here
        print(f"UDP server on port {port} shutting down")

def signal_handler(signal, frame):
    global running
    print('Exiting gracefully...')
    running = False

def main():
    parser = argparse.ArgumentParser(description="Start TCP and UDP servers on consecutive ports.")
    parser.add_argument("start_port", type=int, nargs='?', help="The starting port number for the servers")
    parser.add_argument("num_servers", type=int, nargs='?', help="The number of servers to start")
    parser.add_argument("--type", choices=["tcp", "udp", "audit"], help="Specify the type of servers to start (tcp, udp, audit)")
    args = parser.parse_args()

    global running
    running = True

    threads = []

    if args.type == "audit":
        for port in AUDIT_PORTS:
            thread = threading.Thread(target=start_tcp_server, args=(port,))
            threads.append(thread)
            thread.start()
    else:
        for i in range(args.start_port, args.start_port + args.num_servers):
            if args.type == "tcp" or (args.type is None and i % 2 == 0):
                thread = threading.Thread(target=start_tcp_server, args=(i,))
            elif args.type == "udp" or (args.type is None and i % 2 != 0):
                thread = threading.Thread(target=start_udp_server, args=(i,))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()

# Register the signal handler for CTRL+C
signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    main()
