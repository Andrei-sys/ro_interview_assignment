import ipaddress
from . import entry


class NetworkCollection:
    def __init__(self, ipv4_network: str, raw_entry_list: list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """

        self.ipv4_network = ipaddress.ip_network(ipv4_network)
        self.ipv4_network_hosts = list(self.ipv4_network.hosts())
        self.ipv4_network_hosts = [str(host)
                                   for host in self.ipv4_network_hosts]
        # remove invalid records at this stage for performance
        self.raw_entry_list = raw_entry_list
        self.remove_invalid_records()

        self.entries = [entry.Entry(
            item['address'],
            item['available'],
            item['last_used']
        ) for item in raw_entry_list]

        self.sort_records()

    def __str__(self):
        return f'I am a network collection with network : {self.ipv4_network}'

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        remove = []
        for item in self.raw_entry_list:
            if item['address'] not in self.ipv4_network_hosts:
                remove.append(item)
        for current in remove:
            self.raw_entry_list.remove(current)

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)
