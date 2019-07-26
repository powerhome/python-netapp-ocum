import json

from netapp_ocum.http import NetApp_OCUM_HTTP
from netapp_ocum.objects.cluster import NetApp_OCUM_Cluster
from netapp_ocum.objects.node import NetApp_OCUM_Node
from netapp_ocum.objects.aggregate import NetApp_OCUM_Aggregate
from netapp_ocum.objects.volume import NetApp_OCUM_Volume
from netapp_ocum.objects.svm import NetApp_OCUM_SVM
from netapp_ocum.objects.port import NetApp_OCUM_Port
from netapp_ocum.objects.interface import NetApp_OCUM_Interface
from netapp_ocum.objects.namespace import NetApp_OCUM_Namespace
from netapp_ocum.objects.lun import NetApp_OCUM_LUN

class NetApp_OCUM_Collection(object):
    """
    Class representing a collection of NetApp objects.
    """
    def __init__(self, settings, path, params):
        self._request  = NetApp_OCUM_HTTP(settings)
        self._path     = path
        self._params   = params
        self._klass    = self._get_object_class()

        # API response / objects
        self._response = self._get_response()
        self._objects  = self._map_objects()

        # List of all object's JSON
        self.json      = self._map_json()

    def _get_response(self):
        """
        Get objects from the API.
        """
        accept_types = self._get_object_accept_type()

        return self._request.GET(self._path,
                                 params=self._params,
                                 accept=accept_types,
                                 embedded_key=self._get_object_key(),
                                 name_from=self._klass.NAME_FROM)

    def _map_json(self):
        """
        Return a list of object's JSON.
        """
        return self._response

    def _get_object_class(self):
        """
        Return the object class wrapper.
        """
        return {
            'clusters': NetApp_OCUM_Cluster,
            'nodes': NetApp_OCUM_Node,
            'aggregates': NetApp_OCUM_Aggregate,
            'volumes': NetApp_OCUM_Volume,
            'svms': NetApp_OCUM_SVM,
            'ports': NetApp_OCUM_Port,
            'interfaces': NetApp_OCUM_Interface,
            'namespaces': NetApp_OCUM_Namespace,
            'luns': NetApp_OCUM_LUN
        }.get(self._path)

    def _get_object_accept_type(self):
        """
        Return a list of available Accept-Type headers.
        """
        return {
            'clusters': ['health', 'performance', 'capacity'],
            'nodes': ['health', 'performance'],
            'aggregates': ['health', 'performance', 'capacity'],
            'volumes': [
                'health',
                'performance',
                'capacity',
                'relationship'
            ],
            'svms': ['health', 'performance'],
            'ports': ['performance', 'health'],
            'interfaces': ['performance', 'health'],
            'namespaces': ['performance', 'health'],
            'luns': ['performance']
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
            'volumes': 'netapp:volumeInventoryList',
            'svms': 'netapp:svmInventoryList',
            'ports': 'netapp:portInventoryList',
            'interfaces': 'netapp:lifInventoryList',
            'namespaces': 'netapp:namespaceInventoryList',
            'luns': 'netapp:lunInventoryList'
        }.get(self._path)

    def _map_objects(self):
        """ Map objets to their appropriate classes """
        netapp_objects = []

        for netapp_object in self._response:
            netapp_objects.append(self._klass(netapp_object))
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
