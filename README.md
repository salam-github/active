TinyScanner: A Simple Port Scanner
==================================

Overview
--------

TinyScanner is a lightweight, command-line tool designed for network administrators, security professionals, and technology enthusiasts to perform basic port scanning operations. It supports scanning both TCP and UDP ports to identify open or potentially filtered ports on a target host. This tool is particularly useful for network diagnostics, security audits, and educational purposes.

How to Run TinyScanner
----------------------

### Prerequisites

-   Python 3.x installed on your system.
-   Network access to the host you intend to scan.

### Running the Scanner

1.  **Clone or download the TinyScanner script** to your local machine.

2.  **Open a terminal or command prompt** and navigate to the directory containing `tinyscanner.py`.

3.  **Execute the script** with the required parameters:

    `python tinyscanner.py <host> <port/port-range> [-u] [-t]`

    -   `<host>`: The IP address or hostname of the target machine.
    -   `<port/port-range>`: Specify a single port (e.g., 80) or a range of ports (e.g., 20-80).
    -   `-u`: Perform a UDP scan (optional).
    -   `-t`: Perform a TCP scan (optional).

**Example**:

`python tinyscanner.py 192.168.1.1 80-90 -t -u`

This command scans ports 80 through 90 on the host `192.168.1.1` for both TCP and UDP protocols.

How It Works
------------

TinyScanner utilizes Python's `socket` module to attempt connections on specified ports. For TCP scans, it tries to establish a connection using the `connect_ex` method. An open port is identified if the connection is successful. For UDP scans, due to the connectionless nature of UDP, the scanner sends a basic payload and waits for a response. If no response is received, the port is considered open/filtered. The scanner leverages multi-threading to perform scans concurrently, reducing the overall scan time.

What is a Port?
---------------

In computer networking, a port is a communication endpoint. Ports are used by the operating system to differentiate between different types of traffic. They are numbered addresses that can be used to identify a specific process or type of network service. For example, web servers typically use port 80 for HTTP and port 443 for HTTPS.

What is Port Scanning?
----------------------

Port scanning is the process of probing a server or host for open ports. This technique is commonly used by network administrators to verify security policies and by attackers to find potential weaknesses. A port scan helps to identify which ports are open and which services are running on a host.

Importance of Port Scanning in Penetration Testing
--------------------------------------------------

Port scanning is a critical step in penetration testing as it helps to map out the attack surface of a target. By identifying open ports and the services running on them, penetration testers can determine potential vulnerabilities. This information is crucial for planning subsequent attacks, such as exploiting known vulnerabilities in software or services.

Running the Server Script for Testing
-------------------------------------

To aid in testing TinyScanner, we provide a simple server script capable of running both TCP and UDP servers on specified ports. This script can simulate a real-world environment on your local machine for safe and convenient testing.

### Running the Server Script

1.  Save the provided server script as `servers.py`.

2.  Run the script with Python, specifying the starting port and the number of servers:

    `python servers.py <start_port> <num_servers>`

**Example**:

`python servers.py 80 10`

This will start alternating TCP and UDP servers on consecutive ports beginning from `<start_port>`.

Difficulties of Scanning UDP Ports
----------------------------------

Detecting open UDP ports presents unique challenges due to the protocol's connectionless design. Unlike TCP, a lack of response from a UDP port does not definitively indicate the port's status. As such, TinyScanner may report UDP ports as "open/filtered" or "open/filtered (no response)" based on the absence of a response or an ICMP port unreachable message. This method is chosen for its simplicity and practicality for basic scans, though it may not always provide conclusive results. This behavior is similar to how tools like nmap handle UDP port scanning.

Legal and Ethical Considerations
--------------------------------

Port scanning can be interpreted as intrusive by network operators. Always ensure you have explicit permission to scan the network or host in question. Unauthorized scanning may be illegal or violate local policies.

Conclusion
----------

TinyScanner is a straightforward tool for basic port scanning tasks. While it has limitations, particularly in UDP port detection, it serves as an educational resource and a starting point for more complex network diagnostics. Always use TinyScanner responsibly and with permission.