from netapp_uom.objects.cluster import NetApp_UOM_Cluster
from netapp_uom.objects.node import NetApp_UOM_Node
from netapp_uom.objects.aggregate import NetApp_UOM_Aggregate
from netapp_uom.objects.volume import NetApp_UOM_Volume
from netapp_uom.objects.svm import NetApp_UOM_SVM
from netapp_uom.objects.port import NetApp_UOM_Port
from netapp_uom.objects.lif import NetApp_UOM_LIF
from netapp_uom.objects.event import NetApp_UOM_Event
from netapp_uom.objects.namespace import NetApp_UOM_Namespace
from netapp_uom.objects.lun import NetApp_UOM_LUN

class NetApp_UOM_Collection(object):
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
            'cluster': NetApp_UOM_Cluster,
            'node': NetApp_UOM_Node,
            'aggregate': NetApp_UOM_Aggregate,
            'volume': NetApp_UOM_Volume,
            'svm': NetApp_UOM_SVM,
            'port': NetApp_UOM_Port,
            'lif': NetApp_UOM_LIF,
            'event': NetApp_UOM_Event,
            'namespace': NetApp_UOM_Namespace,
            'lun': NetApp_UOM_LUN
        }.get(self._type)

    def _get_object_key(self):
        """
        Return the top level object key used when extracting information
        from a UOM JSON response.
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
