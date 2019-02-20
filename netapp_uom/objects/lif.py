from netapp_uom.objects.base import NetApp_UOM_ObjectBase

class NetApp_UOM_LIF(NetApp_UOM_ObjectBase):
    """
    Class representing a single NetApp LIF.
    """
    def __init__(self, object_json):
        super().__init__(object_json)
