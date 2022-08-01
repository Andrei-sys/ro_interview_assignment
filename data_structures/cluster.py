from . import network_collection


class Cluster:
    def __init__(self, name: str, security_level: int, network_list: dict):
        """
        Constructor for Cluster data structure.

        self.name -> str
        self.security_level -> int
        self.networks -> list(NetworkCollection)
        """
        self.name = name
        self.security_level = security_level
        self.networks = [
            network_collection.NetworkCollection(
                network, raw_entry_list
            ) for network, raw_entry_list in network_list.items()
        ]

    def __str__(self):
        return f'I am a cluster with name : {self.name}'