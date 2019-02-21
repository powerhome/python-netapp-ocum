from netapp_ocum.objects.cluster import NetApp_OCUM_Cluster
from netapp_ocum.objects.node import NetApp_OCUM_Node
from netapp_ocum.objects.aggregate import NetApp_OCUM_Aggregate
from netapp_ocum.objects.volume import NetApp_OCUM_Volume
from netapp_ocum.objects.svm import NetApp_OCUM_SVM
from netapp_ocum.objects.port import NetApp_OCUM_Port
from netapp_ocum.objects.lif import NetApp_OCUM_LIF
from netapp_ocum.objects.event import NetApp_OCUM_Event
from netapp_ocum.objects.namespace import NetApp_OCUM_Namespace
from netapp_ocum.objects.lun import NetApp_OCUM_LUN

class NetApp_OCUM_Collection(object):
    """
    Class representing a collection of NetApp objects.
    """
    def __init__(self, response, object_type):
        self._response = response
        self._type     = object_type
        self._objects  = self._map_objects()

        # List of all object's JSON
        self.json      = self._map_json()

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
            'cluster': NetApp_OCUM_Cluster,
            'node': NetApp_OCUM_Node,
            'aggregate': NetApp_OCUM_Aggregate,
            'volume': NetApp_OCUM_Volume,
            'svm': NetApp_OCUM_SVM,
            'port': NetApp_OCUM_Port,
            'lif': NetApp_OCUM_LIF,
            'event': NetApp_OCUM_Event,
            'namespace': NetApp_OCUM_Namespace,
            'lun': NetApp_OCUM_LUN
        }.get(self._type)

    def _get_object_key(self):
        """
        Return the top level object key used when extracting information
        from a OCUM JSON response.
        """
        return {
            'cluster': 'netapp:clusterInventoryList',
            'node': 'netapp:nodeInventoryList',
            'aggregate': 'netapp:aggregateInventoryList',
            'volume': 'netapp:volumeInventoryList',
            'svm': 'netapp:svmInventoryList',
            'port': 'netapp:portInventoryList',
            'lif': 'netapp:lifInventoryList',
            'event': 'netapp:eventDtoList',
            'namespace': 'netapp:namespaceInventoryList',
            'lun': 'netapp:lunInventoryList'
        }.get(self._type)

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
