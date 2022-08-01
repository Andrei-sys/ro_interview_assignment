from sqlite3 import DatabaseError


from data_structures.datacenter import Datacenter
from data_structures.cluster import Cluster
from data_structures.network_collection import NetworkCollection
from data_structures.entry import Entry

if __name__ == '__main__':

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    datacenter = datacenters[0]

    print(datacenter.clusters)