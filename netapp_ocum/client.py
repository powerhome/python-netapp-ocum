from netapp_ocum.http import NetApp_OCUM_HTTP
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

        # Request handler
        self.request = NetApp_OCUM_HTTP(self.settings)

    def set_params(self, params):
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
        return NetApp_OCUM_Collection(
            self.request.GET('clusters', params=self.set_params(params)), 'cluster'
        )

    def get_svms(self, params={}):
        """
        Return a list of SVMs from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('svms', params=self.set_params(params)), 'svm'
        )

    def get_nodes(self, params={}):
        """
        Return a list of nodes from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('nodes', params=self.set_params(params)), 'node'
        )

    def get_aggregates(self, params={}):
        """
        Return a list of aggregates from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('aggregates', params=self.set_params(params)), 'aggregate'
        )

    def get_volumes(self, params={}):
        """
        Return a list of volumes from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('volumes', params=self.set_params(params)), 'volume'
        )

    def get_ports(self, params={}):
        """
        Return a list of ports from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('ports', params=self.set_params(params)), 'port'
        )

    def get_events(self, params={}):
        """
        Return a list of events from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('events', params=self.set_params(params)), 'event'
        )

    def get_lifs(self, params={}):
        """
        Return a list of LIFs from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('lifs', params=self.set_params(params)), 'lif'
        )

    def get_luns(self, params={}):
        """
        Return a list of LUNs from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('luns', params=self.set_params(params)), 'lun'
        )

    def get_namespaces(self, params={}):
        """
        Return a list of namespaces from the OCUM.
        """
        return NetApp_OCUM_Collection(
            self.request.GET('namespaces', params=self.set_params(params)), 'namespace'
        )
