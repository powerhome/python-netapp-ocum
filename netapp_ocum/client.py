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
        return NetApp_OCUM_Collection(self.request, 'clusters', self._set_params(params))

    def get_svms(self, params={}):
        """
        Return a list of SVMs from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'svms', self._set_params(params))

    def get_nodes(self, params={}):
        """
        Return a list of nodes from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'nodes', self._set_params(params))

    def get_aggregates(self, params={}):
        """
        Return a list of aggregates from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'aggregates', self._set_params(params))

    def get_aggregate_metrics(self, params={}):
        """
        Get aggregate metrics from the `aggregates/capacity-utilization` endpoint.
        """
        return NetApp_OCUM_Collection(self.request, 'aggregates/capacity-utilization', self._set_params(params))

    def get_volumes(self, params={}):
        """
        Return a list of volumes from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'volumes', self._set_params(params))

    def get_volume_metrics(self, params={}):
        """
        Get volume metrics from the `volumes/capacity-utilization` endpoint.
        """
        return NetApp_OCUM_Collection(self.request, 'volumes/capacity-utilization', self._set_params(params))

    def get_volume_relationships(self, params={}):
        """
        Return a list of mirror relationships of volumes from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'volumes/relationships-transfer-status', self._set_params(params))

    def get_ports(self, params={}):
        """
        Return a list of ports from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'ports', self._set_params(params))

    def get_events(self, params={}):
        """
        Return a list of events from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'events', self._set_params(params))

    def get_lifs(self, params={}):
        """
        Return a list of LIFs from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'lifs', self._set_params(params))

    def get_luns(self, params={}):
        """
        Return a list of LUNs from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'luns', self._set_params(params))

    def get_namespaces(self, params={}):
        """
        Return a list of namespaces from the OCUM.
        """
        return NetApp_OCUM_Collection(self.request, 'namespaces', self._set_params(params))
