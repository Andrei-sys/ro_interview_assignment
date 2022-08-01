import re
from . import cluster


class Datacenter:
    def __init__(self, name: str, cluster_list: dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.name_std = self.name[:3].upper()

        self.raw_cluster_list = cluster_list
        self.remove_invalid_clusters()

        self.clusters = self.initialize_clusters(self.raw_cluster_list)

        for item in self.clusters:
            print(item.name)

    def initialize_clusters(self, cluster_list):
        clusters = []
        cluster_names = list(cluster_list.keys())
        for cluster_name in cluster_names:
            clusters.append(
                cluster.Cluster(
                    cluster_name,
                    cluster_list[cluster_name]['security_level'],
                    cluster_list[cluster_name]['networks']
                )
            )
            cluster_list[cluster_name]

        return clusters

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """
        pattern = '^[A-Z]{3}-[0-9]{1,3}$'

        raw_cluster_names = list(self.raw_cluster_list.keys())
        for raw_cluster_name in raw_cluster_names:

            if raw_cluster_name[:3].upper() != self.name_std:
                del self.raw_cluster_list[raw_cluster_name]
                continue

            if re.search(pattern, raw_cluster_name) == None:
                del self.raw_cluster_list[raw_cluster_name]
