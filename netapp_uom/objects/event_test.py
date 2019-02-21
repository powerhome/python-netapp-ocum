import unittest
from netapp_uom.objects.event import NetApp_UOM_Event

class NetApp_UOM_Object_Event_Test(unittest.TestCase):
    """Tests for `netapp_uom/objects/event.py`."""

    def test_event_instance(self):
        """ Test creating an instance of `NetApp_UOM_Event` """
        event = NetApp_UOM_Event({
            'id': 1
        })
        self.assertIsInstance(event, NetApp_UOM_Event)
