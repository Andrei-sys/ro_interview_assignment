class Datacenter:
    def __init__(self, name, cluster_list):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """
        self.name = name
        self.clusters = cluster_list

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        pass
