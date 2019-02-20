import unittest
import requests
from unittest import mock
from netapp_uom.client import NetApp_UOM_Client
from netapp_uom.http_test import mock_get_request
from netapp_uom.objects import NetApp_UOM_Collection
from netapp_uom.settings_test import NetApp_UOM_Settings_Mock

def mock_client(with_settings=False):
    """
    Generate a mock client for testing.
    """
    mock_settings = NetApp_UOM_Settings_Mock()

    if not with_settings:
        return NetApp_UOM_Client(
            mock_settings.api_host,
            mock_settings.api_user,
            mock_settings.api_password,
            api_port   = mock_settings.api_port,
            verify_ssl = mock_settings.verify_ssl
        )
    else:
        return NetApp_UOM_Client.with_settings(mock_settings)

class NetApp_UOM_Client_Test(unittest.TestCase):
    """Tests for `netapp_uom/client.py`."""

    def test_create_client(self):
        """ Test creating a new client interface. """
        client = mock_client()
        self.assertIsInstance(client, NetApp_UOM_Client)

    def test_create_client_with_settings(self):
        """ Test creating a new client interface using the `with_settings` method. """
        client = mock_client(with_settings=True)
        self.assertIsInstance(client, NetApp_UOM_Client)

    def test_client_set_params(self):
        """ Test the `set_params` method in the client. """
        client = mock_client()
        test_params = {'one': 'value_one', 'two': 'value_two'}
        params_retval = client.set_params(test_params)
        self.assertIsInstance(params_retval, dict)

    def test_client_filter(self):
        """ Test the `filter` method to make sure it returns a client object. """
        client = mock_client()
        test_filters = {'one': 'value_one', 'two': 'value_two'}
        filtered_client = client.filter(test_filters)
        self.assertIsInstance(filtered_client, NetApp_UOM_Client)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_clusters(self, mock_get):
        """ Test the `get_clusters` method. """
        client = mock_client()
        response = client.get_clusters()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_nodes(self, mock_get):
        """ Test the `get_nodes` method. """
        client = mock_client()
        response = client.get_nodes()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_aggregates(self, mock_get):
        """ Test the `get_aggregates` method. """
        client = mock_client()
        response = client.get_aggregates()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_svms(self, mock_get):
        """ Test the `get_svms` method. """
        client = mock_client()
        response = client.get_svms()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_lifs(self, mock_get):
        """ Test the `get_lifs` method. """
        client = mock_client()
        response = client.get_lifs()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_ports(self, mock_get):
        """ Test the `get_ports` method. """
        client = mock_client()
        response = client.get_ports()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_events(self, mock_get):
        """ Test the `get_events` method. """
        client = mock_client()
        response = client.get_events()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_namespaces(self, mock_get):
        """ Test the `get_namespaces` method. """
        client = mock_client()
        response = client.get_namespaces()
        self.assertIsInstance(response, NetApp_UOM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_luns(self, mock_get):
        """ Test the `get_luns` method. """
        client = mock_client()
        response = client.get_luns()
        self.assertIsInstance(response, NetApp_UOM_Collection)
