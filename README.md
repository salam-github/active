# TinyScanner: A Simple Port Scanner

## Overview

TinyScanner is a lightweight, command-line tool designed for network administrators, security professionals, and technology enthusiasts to perform basic port scanning operations. It supports scanning both TCP and UDP ports to identify open or potentially filtered ports on a target host. This tool is particularly useful for network diagnostics, security audits, and educational purposes.

## How to Run TinyScanner

### Prerequisites

- Python 3.x installed on your system.
- Network access to the host you intend to scan.

### Running the Scanner

1. **Clone or download the TinyScanner script** to your local machine.

2. **Open a terminal or command prompt** and navigate to the directory containing `tinyscanner.py`.

3. **Execute the script** with the required parameters:
python tinyscanner.py <host> <port/port-range> [-u] [-t]

markdown
Copy code
- `<host>`: The IP address or hostname of the target machine.
- `<port/port-range>`: Specify a single port (e.g., 80) or a range of ports (e.g., 20-80).
- `-u`: Perform a UDP scan (optional).
- `-t`: Perform a TCP scan (optional).

**Example**:
python tinyscanner.py 192.168.1.1 80-90 -t -u

vbnet
Copy code
This command scans ports 80 through 90 on the host `192.168.1.1` for both TCP and UDP protocols.

## How It Works

TinyScanner utilizes Python's `socket` module to attempt connections on specified ports. For TCP scans, it tries to establish a connection using the `connect_ex` method. An open port is identified if the connection is successful. For UDP scans, due to the connectionless nature of UDP, the scanner sends a basic payload and waits for a response. If no response is received, the port is considered open/filtered. The scanner leverages multi-threading to perform scans concurrently, reducing the overall scan time.

## Disclaimers and Challenges

### UDP Scanning

Detecting open UDP ports presents unique challenges due to the protocol's connectionless design. Unlike TCP, a lack of response from a UDP port does not definitively indicate the port's status. As such, TinyScanner may report UDP ports as "open/filtered" or "open/filtered (no response)" based on the absence of a response or an ICMP port unreachable message. This method is chosen for its simplicity and practicality for basic scans, though it may not always provide conclusive results.

### Legal and Ethical Considerations

Port scanning can be interpreted as intrusive by network operators. Always ensure you have explicit permission to scan the network or host in question. Unauthorized scanning may be illegal or violate local policies.

## Testing Locally with Server Code

To aid in testing TinyScanner, we provide a simple server script capable of running both TCP and UDP servers on specified ports. This script can simulate a real-world environment on your local machine for safe and convenient testing.

### Running the Server Script

1. Save the provided server script as `servers.py`.

2. Run the script with Python, specifying the starting port and the number of servers:
python servers.py <start_port> <num_servers>

csharp
Copy code
This will start alternating TCP and UDP servers on consecutive ports beginning from `<start_port>`.

### Example

To start 10 servers beginning at port 80 (5 TCP and 5 UDP servers on alternating ports):
python servers.py 80 10

python
Copy code

This setup allows you to test TinyScanner's functionality by scanning your localhost (`127.0.0.1`) on the ports you've opened with the server script.

## Conclusion

TinyScanner is a straightforward tool for basic port scanning tasks. While it has limitations, particularly in UDP port detection, it serves as an educational resource and a starting point for more complex network diagnostics. Always use TinyScanner responsibly and with permission.