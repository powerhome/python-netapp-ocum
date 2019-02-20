from netapp_uom.http import NetApp_UOM_HTTP
from netapp_uom.objects import NetApp_UOM_Collection
from netapp_uom.settings import NetApp_UOM_Settings

class NetApp_UOM_Client(object):
    """
    Class object for handling HTTP requests to the UOM API.
    """
    def __init__(self, api_host, api_user, api_password,
        api_port=443,
        verify_ssl=True,
        filters={}
    ):

        # Store connection settings
        self.settings = NetApp_UOM_Settings(
            api_host     = api_host,
            api_user     = api_user,
            api_password = api_password,
            api_port     = api_port,
            verify_ssl   = verify_ssl,
        )

        # Any filters as defined by the filter() method
        self.filters = filters

        # Request handler
        self.request = NetApp_UOM_HTTP(self.settings)

    @classmethod
    def with_settings(cls, settings, filters={}):
        """
        Create an instance of the client using the NetApp_UOM_Settings object.
        """
        return cls(settings.api_host, settings.api_user, settings.api_password,
            api_port   = settings.api_port,
            verify_ssl = settings.verify_ssl,
            filters    = filters,
        )

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

    def filter(self, filters):
        """
        Apply filters to the chained method.
        """
        return NetApp_UOM_Client.with_settings(self.settings, filters=filters)

    def get_clusters(self, params={}):
        """
        Return a list of clusters from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('clusters', params=self.set_params(params)), 'cluster'
        )

    def get_svms(self, params={}):
        """
        Return a list of SVMs from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('svms', params=self.set_params(params)), 'svm'
        )

    def get_nodes(self, params={}):
        """
        Return a list of nodes from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('nodes', params=self.set_params(params)), 'node'
        )

    def get_aggregates(self, params={}):
        """
        Return a list of aggregates from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('aggregates', params=self.set_params(params)), 'aggregate'
        )

    def get_volumes(self, params={}):
        """
        Return a list of volumes from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('volumes', params=self.set_params(params)), 'volume'
        )

    def get_ports(self, params={}):
        """
        Return a list of ports from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('ports', params=self.set_params(params)), 'port'
        )

    def get_events(self, params={}):
        """
        Return a list of events from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('events', params=self.set_params(params)), 'event'
        )

    def get_lifs(self, params={}):
        """
        Return a list of LIFs from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('lifs', params=self.set_params(params)), 'lif'
        )

    def get_luns(self, params={}):
        """
        Return a list of LUNs from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('luns', params=self.set_params(params)), 'lun'
        )

    def get_namespaces(self, params={}):
        """
        Return a list of namespaces from the UOM.
        """
        return NetApp_UOM_Collection(
            self.request.GET('namespaces', params=self.set_params(params)), 'namespace'
        )
