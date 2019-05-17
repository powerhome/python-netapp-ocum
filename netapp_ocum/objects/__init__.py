from netapp_ocum.objects.cluster import NetApp_OCUM_Cluster
from netapp_ocum.objects.node import NetApp_OCUM_Node
from netapp_ocum.objects.aggregate import NetApp_OCUM_Aggregate
from netapp_ocum.objects.aggregate_metrics import NetApp_OCUM_AggregateMetrics
from netapp_ocum.objects.volume import NetApp_OCUM_Volume
from netapp_ocum.objects.volume_metrics import NetApp_OCUM_VolumeMetrics
from netapp_ocum.objects.svm import NetApp_OCUM_SVM
from netapp_ocum.objects.port import NetApp_OCUM_Port
from netapp_ocum.objects.lif import NetApp_OCUM_LIF
from netapp_ocum.objects.event import NetApp_OCUM_Event
from netapp_ocum.objects.namespace import NetApp_OCUM_Namespace
from netapp_ocum.objects.lun import NetApp_OCUM_LUN
from netapp_ocum.objects.relationship import NetApp_OCUM_Relationship

class NetApp_OCUM_Collection(object):
    """
    Class representing a collection of NetApp objects.
    """
    def __init__(self, request, path, params):
        self._request  = request
        self._path     = path
        self._params   = params

        # API response / mapped objects
        self._response = self._get_response()
        self._objects  = self._map_objects()

        # List of all object's JSON
        self.json      = self._map_json()

    def _get_response(self):
        """
        Get objects from the API.
        """
        return self._request.GET(self._path, params=self._params)

    def _map_json(self):
        """
        Return a list of object's JSON.
        """
        return [x.json for x in self._objects]

    def _get_object_class(self):
        """
        Return the object class wrapper.
        """
        return {
            'clusters': NetApp_OCUM_Cluster,
            'nodes': NetApp_OCUM_Node,
            'aggregates': NetApp_OCUM_Aggregate,
            'aggregates/capacity-utilization': NetApp_OCUM_AggregateMetrics,
            'volumes': NetApp_OCUM_Volume,
            'volumes/capacity-utilization': NetApp_OCUM_VolumeMetrics,
            'volumes/relationships-transfer-status': NetApp_OCUM_Relationship,
            'svms': NetApp_OCUM_SVM,
            'ports': NetApp_OCUM_Port,
            'lifs': NetApp_OCUM_LIF,
            'events': NetApp_OCUM_Event,
            'namespaces': NetApp_OCUM_Namespace,
            'luns': NetApp_OCUM_LUN
        }.get(self._path)

    def _get_object_key(self):
        """
        Return the top level object key used when extracting information
        from a OCUM JSON response.
        """
        return {
            'clusters': 'netapp:clusterInventoryList',
            'nodes': 'netapp:nodeInventoryList',
            'aggregates': 'netapp:aggregateInventoryList',
            'aggregates/capacity-utilization': 'netapp:aggregateCapacityAndUtilizationList',
            'volumes': 'netapp:volumeInventoryList',
            'volumes/capacity-utilization': 'netapp:volumeCapacityAndUtilizationList',
            'volumes/relationships-transfer-status': 'netapp:volumeTransferStatusList',
            'svms': 'netapp:svmInventoryList',
            'ports': 'netapp:portInventoryList',
            'lifs': 'netapp:lifInventoryList',
            'events': 'netapp:eventDtoList',
            'namespaces': 'netapp:namespaceInventoryList',
            'luns': 'netapp:lunInventoryList'
        }.get(self._path)

    def _map_objects(self):
        """
        Map object response JSON data to a class object.
        """
        netapp_objects = []
        for netapp_object in self._response['_embedded'][self._get_object_key()]:
            netapp_objects.append(self._get_object_class()(netapp_object))
        return netapp_objects

    def find(self, attr_key, attr_val):
        """
        Find a single object by an attribute key/value pair.
        """
        for netapp_object in self._objects:
            if hasattr(netapp_object, attr_key) and attr_val == getattr(netapp_object, attr_key):
                return netapp_object
        return None

    def __iter__(self):
        """
        Return a dictionary of gRPC methods.
        """
        for netapp_object in self._objects:
            yield(netapp_object)
