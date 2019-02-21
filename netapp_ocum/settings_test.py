import unittest
from netapp_ocum.settings import NetApp_OCUM_Settings

class NetApp_OCUM_Settings_Mock(NetApp_OCUM_Settings):
    """
    Mock settings object for testing.
    """
    def __init__(self):
        super().__init__(
            api_host     = '127.0.0.1',
            api_user     = 'admin',
            api_password = 'password',
            api_port     = 443,
            verify_ssl   = True
        )

class NetApp_OCUM_Settings_Test(unittest.TestCase):
    """Tests for `netapp_ocum/settings.py`."""

    def test_create_settings(self):
        """ Test creating a new settings object. """
        settings = NetApp_OCUM_Settings_Mock()
        self.assertIsInstance(settings, NetApp_OCUM_Settings)
