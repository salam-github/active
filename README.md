# TinyScanner

TinyScanner is a simple, command-line port scanner designed to detect open TCP and UDP ports on a target host. This tool is intended for educational purposes and network administrators looking to check their network's security.

## Disclaimer

Use TinyScanner responsibly. Scanning networks without permission is illegal and unethical. Ensure you have explicit consent from the network owner before scanning. This tool is provided for educational purposes only, and the developer assumes no liability for misuse or illegal activities.

## Features

- TCP and UDP port scanning
- Scans individual ports or ranges of ports
- Identifies open ports and the services running on them

## Installation

TinyScanner requires Python 3.6 or higher. Clone this repository or download the `tinyscanner` script directly to your local machine.

## Usage

Run TinyScanner from the command line, specifying the target host and ports to scan. You must include at least one protocol flag (`-t` for TCP, `-u` for UDP) to conduct a scan.

### Syntax

```python
python main.py <host> <port/port-range> [options]
```

### Options

- `-t`: Perform a TCP scan (required if UDP is not specified)
- `-u`: Perform a UDP scan (required if TCP is not specified)
- `<host>`: The target IP address or hostname
- `<port/port-range>`: A single port (e.g., `80`) or a range of ports (e.g., `80-100`)

### Examples

- Scan a single TCP port: `python main.py -t 192.168.1.1 80`
- Scan a range of TCP ports: `python main.py -t 192.168.1.1 20-25`
- Scan a single UDP port: `python main.py -u 192.168.1.1 53`
- Scan a range of UDP ports: `python main.py -u 192.168.1.1 1000-1005`

## How It Works

TinyScanner creates a socket connection using the specified protocol (TCP or UDP) to the target port(s). For TCP scans, it attempts to establish a three-way handshake. If successful, the port is considered open. For UDP scans, due to the connectionless nature of UDP, the scanner sends an empty packet and listens for a response. No response or an ICMP unreachable error typically indicates the port is closed or filtered.

## Contributing

Contributions to TinyScanner are welcome. Please ensure you follow ethical guidelines and use the tool responsibly.

## License

TinyScanner is released under the MIT License. See the LICENSE file for more details.
