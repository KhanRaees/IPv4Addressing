"""
This module provides functions to calculate the following for an IPv4 Network:
- Network ID
- First & Last IP of Network
- Broadcast ID
- Total IPs and Usable IPs
- Subnet Mask
- Wildcard Mask
- Class of the Network
"""


class IPv4Addressing:
    """ Python Class Containing Functions For IPv4 Addressing Calculations."""

    def __init__(self, ip_address, prefix_length):
        self.ip_address = ip_address
        self.ip_list = ip_address.split(".")
        self.prefix_length = prefix_length

    def prefix_to_mask(self):
        subnet_mask = [0, 0, 0, 0]
        for x in range(int(self.prefix_length)):
            subnet_mask[int(x/8)] = subnet_mask[int(x/8)] + (1 << (7 - x % 8))
        return subnet_mask

    def hosts_in_network(self):
        total_hosts = 2 ** (32-self.prefix_length)
        usable_hosts = total_hosts - 2
        if self.prefix_length == 31:
            return total_hosts, total_hosts
        elif self.prefix_length == 32:
            return total_hosts, total_hosts
        else:
            return total_hosts, usable_hosts

    def identify_class(self, first_octet):
        if first_octet >= 0 and first_octet <= 127:
            return "A"
        elif first_octet >= 128 and first_octet <= 191:
            return "B"
        elif first_octet >= 192 and first_octet <= 223:
            return "C"
        elif first_octet >= 224 and first_octet <= 239:
            return "D"
        else:
            return "E"

    def calculate_wildcard(self):
        subnet_mask = self.prefix_to_mask()
        wildcard = [0, 0, 0, 0]
        for i in range(0, 4):
            wildcard[i] = ~ subnet_mask[i] & 0xFF
        return wildcard

    def calculate_network(self):
        mask_list = self.prefix_to_mask()
        network_id = []
        for i in range(0, 4):
            network_id.append(int(self.ip_list[i]) & int(mask_list[i]))
        return network_id

    def calculate_broadcast(self):
        broadcast = []
        network_id = self.calculate_network()
        wildcard = self.calculate_wildcard()
        for i in range(0, 4):
            broadcast.append(int(network_id[i]) | int(wildcard[i]))
        return broadcast

    def first_ip(self):
        if self.prefix_length == 31:
            first_ip = self.calculate_network()
        elif self.prefix_length == 32:
            first_ip = self.calculate_network()
        else:
            broadcast = self.calculate_broadcast()
            network_id = self.calculate_network()
            first_ip = []
            for i in range(4):
                if network_id[i] == broadcast[i]:
                    first_ip.append(network_id[i])
                else:
                    if i == 3:
                        first_ip.append(network_id[i]+1)
                    else:
                        first_ip.append(network_id[i])
        return first_ip

    def last_ip(self):
        if self.prefix_length == 31:
            last_ip = self.calculate_broadcast()
        elif self.prefix_length == 32:
            last_ip = self.calculate_network()
        else:
            last_ip = self.calculate_broadcast()
            last_ip[3] = last_ip[3] & 0xFE
        return last_ip

    def validate_prefix(self):
        if (1 <= self.prefix_length <= 32):
            return True
        else:
            return False

    def validate_ip(self):
        valid = True
        if len(self.ip_list) == 4:
            for i in range(4):
                if 0 <= int(self.ip_list[i]) <= 255:
                    valid = True
                else:
                    return False
        else:
            return False

        return valid


try:
    def ipv4_address(ip_address: str, prefix_length: int) -> tuple:
        """
        ===== Parameters =====\n
        ip_address (string) in format "X.X.X.X" where X is <0-255>\n
        prefix_length (integer) is <1-32>\n

        ===== Returns =====\n
        This function returns tuple (network_id, first_ip, last_ip, broadcast_id, total_ips, total_usable_ips, subnet_mask, wildcard_mask, network_class)
        """
        obj = IPv4Addressing(ip_address, prefix_length)

        if obj.validate_ip() and obj.validate_prefix():
            network_id = ".".join(map(str, obj.calculate_network()))
            first_ip = ".".join(map(str, obj.first_ip()))
            last_ip = ".".join(map(str, obj.last_ip()))
            broadcast_id = ".".join(map(str, obj.calculate_broadcast()))
            total_ips = obj.hosts_in_network()[0]
            total_usable_ips = obj.hosts_in_network()[1]
            subnet_mask = ".".join(map(str, obj.prefix_to_mask()))
            wildcard_mask = ".".join(map(str, obj.calculate_wildcard()))
            network_class = obj.identify_class(int(obj.ip_list[0]))

            return network_id, first_ip, last_ip, broadcast_id, total_ips, total_usable_ips, subnet_mask, wildcard_mask, network_class

        else:
            print("Given Value is Incorrect. Please Try Again.")

except(ValueError, IndexError):
    print("Given Value is Incorrect. Please Try Again.")
