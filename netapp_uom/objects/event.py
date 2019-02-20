from netapp_uom.objects.base import NetApp_UOM_ObjectBase

class NetApp_UOM_Event(NetApp_UOM_ObjectBase):
    """
    Class representing a single NetApp event.
    """
    def __init__(self, object_json):
        super().__init__(object_json)
