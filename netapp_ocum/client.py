from netapp_ocum.objects import NetApp_OCUM_Collection
from netapp_ocum.settings import NetApp_OCUM_Settings

class NetApp_OCUM_Client(object):
    """
    Class object for handling HTTP requests to the OCUM API.
    """
    def __init__(self, api_host, api_user, api_password,
        api_port   = 443,
        verify_ssl = True,
        filters    = {}
    ):

        # Store connection settings
        self.settings = NetApp_OCUM_Settings(
            api_host     = api_host,
            api_user     = api_user,
            api_password = api_password,
            api_port     = api_port,
            verify_ssl   = verify_ssl,
        )

        # Any filters as defined by the filter() method
        self.filters = filters

    def _set_params(self, params):
        """
        Set query parameters for the request, merge any filters defined at the
        class level. Parameters passed to the method via `params` argument
        take precedence over class level filters.
        """
        query_params = params
        if self.filters:
            for k,v in self.filters.items():
                if not k in query_params:
                    query_params[k] = v
        return query_params

    def get_clusters(self, params={}):
        """
        Return a list of clusters from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'clusters', self._set_params(params))

    def get_svms(self, params={}):
        """
        Return a list of SVMs from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'svms', self._set_params(params))

    def get_nodes(self, params={}):
        """
        Return a list of nodes from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'nodes', self._set_params(params))

    def get_aggregates(self, params={}):
        """
        Return a list of aggregates from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'aggregates', self._set_params(params))

    def get_volumes(self, params={}):
        """
        Return a list of volumes from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'volumes', self._set_params(params))

    def get_ports(self, params={}):
        """
        Return a list of ports from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'ports', self._set_params(params))

    def get_interfaces(self, params={}):
        """
        Return a list of networking interfaces from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'interfaces', self._set_params(params))

    def get_luns(self, params={}):
        """
        Return a list of LUNs from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'luns', self._set_params(params))

    def get_namespaces(self, params={}):
        """
        Return a list of namespaces from the OCUM.
        """
        return NetApp_OCUM_Collection(self.settings, 'namespaces', self._set_params(params))
