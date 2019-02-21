import unittest
from netapp_ocum.objects.event import NetApp_OCUM_Event

class NetApp_OCUM_Object_Event_Test(unittest.TestCase):
    """Tests for `netapp_ocum/objects/event.py`."""

    def test_event_instance(self):
        """ Test creating an instance of `NetApp_OCUM_Event` """
        event = NetApp_OCUM_Event({
            'id': 1
        })
        self.assertIsInstance(event, NetApp_OCUM_Event)
