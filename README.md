## ipaddressing.py
ipaddressing.py is a python module that provides function(s) to calculate the following for an IPv4 Network:
- Network ID
- First & Last IP of Network
- Broadcast ID
- Total IPs and Usable IPs
- Subnet Mask
- Wildcard Mask
- Class of the Network

## Installation
You may copy ipaddressing.py in Python Library folder.

## Usage
The ipv4_address function takes 2 arguments and returns a tuple:
- ip_address (string) in format "X.X.X.X" where X is <0-255>
- prefix_length (integer) is <1-32>

This function returns tuple (network_id, first_ip, last_ip, broadcast_id, total_ips, total_usable_ips, subnet_mask, wildcard_mask, network_class)

```python
from ipaddressing import ipv4_address

ip = ipv4_address('192.168.1.1', 24)

try:
    print(f"Network ID: {ip[0]}")
    print(f"First Usable IP: {ip[1]}")
    print(f"Last Usable IP: {ip[2]}")
    print(f"Broadcast ID: {ip[3]}")
    print(f"Total IPs in Network: {ip[4]}")
    print(f"Total Usable IPs: {ip[5]}")
    print(f"Subnet Mask: {ip[6]}")
    print(f"Wildcard Mask: {ip[7]}")
    print(f"Class of Network: {ip[8]}")
except:
    print("Use Correct value in arguments.")
```
