import unittest
import requests
from unittest import mock
from netapp_ocum.client import NetApp_OCUM_Client
from netapp_ocum.http_test import mock_get_request
from netapp_ocum.objects import NetApp_OCUM_Collection
from netapp_ocum.settings_test import NetApp_OCUM_Settings_Mock

def mock_client(filters={}):
    """
    Generate a mock client for testing.
    """
    mock_settings = NetApp_OCUM_Settings_Mock()

    return NetApp_OCUM_Client(
        mock_settings.api_host,
        mock_settings.api_user,
        mock_settings.api_password,
        api_port   = mock_settings.api_port,
        verify_ssl = mock_settings.verify_ssl,
        filters    = filters
    )

class NetApp_OCUM_Client_Test(unittest.TestCase):
    """Tests for `netapp_ocum/client.py`."""

    def test_create_client(self):
        """ Test creating a new client interface. """
        client = mock_client()
        self.assertIsInstance(client, NetApp_OCUM_Client)

    def test_client_set_params(self):
        """ Test the `set_params` method in the client. """
        client = mock_client()
        test_params = {'one': 'value_one', 'two': 'value_two'}
        params_retval = client._set_params(test_params)
        self.assertIsInstance(params_retval, dict)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_filtered_client(self, mock_get):
        """ Test creating a client instance with filters. """
        client = mock_client(filters={'one': 'two'})
        response = client.get_volumes()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_request_with_params(self, mock_get):
        """ Test a client request with parameters. """
        client = mock_client()
        response = client.get_volumes(params={'one': 'two'})
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_filtered_client_request_with_params(self, mock_get):
        """ Test a filtered client request with parameters. """
        client = mock_client(filters={'three': 'four'})
        response = client.get_volumes(params={'one': 'two'})
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_clusters(self, mock_get):
        """ Test the `get_clusters` method. """
        client = mock_client()
        response = client.get_clusters()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_nodes(self, mock_get):
        """ Test the `get_nodes` method. """
        client = mock_client()
        response = client.get_nodes()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_aggregates(self, mock_get):
        """ Test the `get_aggregates` method. """
        client = mock_client()
        response = client.get_aggregates()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_aggregate_metrics(self, mock_get):
        """ Test the `get_aggregate_metrics` method. """
        client = mock_client()
        response = client.get_aggregate_metrics()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_volumes(self, mock_get):
        """ Test the `get_volumes` method. """
        client = mock_client()
        response = client.get_volumes()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_volume_metrics(self, mock_get):
        """ Test the `get_volume_metrics` method. """
        client = mock_client()
        response = client.get_volume_metrics()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_svms(self, mock_get):
        """ Test the `get_svms` method. """
        client = mock_client()
        response = client.get_svms()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_lifs(self, mock_get):
        """ Test the `get_lifs` method. """
        client = mock_client()
        response = client.get_lifs()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_ports(self, mock_get):
        """ Test the `get_ports` method. """
        client = mock_client()
        response = client.get_ports()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_events(self, mock_get):
        """ Test the `get_events` method. """
        client = mock_client()
        response = client.get_events()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_namespaces(self, mock_get):
        """ Test the `get_namespaces` method. """
        client = mock_client()
        response = client.get_namespaces()
        self.assertIsInstance(response, NetApp_OCUM_Collection)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_get_luns(self, mock_get):
        """ Test the `get_luns` method. """
        client = mock_client()
        response = client.get_luns()
        self.assertIsInstance(response, NetApp_OCUM_Collection)
