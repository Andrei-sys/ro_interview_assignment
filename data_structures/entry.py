import datetime
import ipaddress


class Entry:
    def __init__(self, address: str, available: bool, last_used: str):
        """
        Constructor for Entry data structure.

        self.address -> str
        self.available -> bool
        self.last_used -> datetime
        """
        self.address = address
        self.available = available
        self.last_used = datetime.datetime.strptime(
            last_used, r'%d/%m/%y %H:%M:%S'
        )

    def __str__(self):
        return f'I am an entry {self.address}'

    def __eq__(self, other):
        return self.address == other.address

    def __lt__(self, other):
        return int(ipaddress.ip_address(self.address)) < int(ipaddress.ip_address(other.address))