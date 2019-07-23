import json
import requests
from threading import Thread

class NetApp_OCUM_HTTP(object):
    """
    Class object for handling HTTP requests/responses for the OCUM.
    """
    def __init__(self, settings):
        self.settings = settings
        self.path = None

    def _GET_worker(self, url, params, accept, responses, embedded_key):
        """
        Worker for performing threaded HTTP GET requests.
        """
        response = requests.get(url,
            auth    = (self.settings.api_user, self.settings.api_password),
            verify  = self.settings.verify_ssl,
            headers = {
                'Accept': 'application/vnd.netapp.object.inventory.{}.hal+json'.format(accept)
            },
            params  = params
        )

        # Request failed
        if not int(response.status_code) == 200:
            raise Exception('Failed to GET {0}: {1}'.format(url, response.json()))

        responses[accept] = response.json()['_embedded'][embedded_key]

    def _sort_response_by_id(self, response, name_from):
        """
        Sort the responses by object ID.
        """
        objects_by_id = {}

        for accept_type, accept_responses in response.items():
            for accept_response in accept_responses:
                current_id = None

                # Object has a top level ID
                if 'id' in accept_response:
                    current_id = accept_response['id']

                # Object ID is nested
                else:

                    # Extract ID for volume relationship
                    if self.path == 'volumes' and accept_type == 'relationship':

                        # Map to the source volume if found, otherwise destination volume
                        if accept_response['source_volume']['id']:
                            current_id = accept_response['source_volume']['id']
                        else:
                            current_id = accept_response['destination_volume']['id']

                    # Extract ID for aggregate capacity
                    if self.path == 'aggregates' and accept_type == 'capacity':
                        current_id = accept_response['aggregate']['id']

                    # Extract ID for node capacity
                    if self.path == 'nodes' and accept_type == 'capacity':
                        current_id = accept_response['node']['id']

                if not current_id in objects_by_id:
                    objects_by_id[current_id] = {
                        'type': self.path
                    }

                if accept_type == name_from[0]:
                    objects_by_id[current_id]['name'] = accept_response[name_from[1]][name_from[2]]

                objects_by_id[current_id][accept_type] = accept_response

        # Convert to an array of objects
        object_array = []
        for object_id, object_attrs in objects_by_id.items():
            object_item = object_attrs
            object_item['id'] = object_id
            object_array.append(object_item)
        return object_array

    def GET(self, url_path, accept, embedded_key, name_from, params={}):
        """
        Make a GET request to the OCUM API method with an optional filter. Start
        a thread for each accept type.
        """
        responses = {}
        threads = []

        self.path = url_path

        api_url = 'https://{0}:{1}/api/ontap/{2}'.format(
            self.settings.api_host,
            self.settings.api_port,
            url_path
        )

        # Get objects for each type of endpoint based on Accept header
        # for accept_type in accept:
        #     self._GET_worker(api_url, params, accept_type, responses, embedded_key)

        for accept_type in accept:
            t = Thread(target=self._GET_worker, args=(api_url, params, accept_type, responses, embedded_key))
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

        # Sort response objects by ID and return
        return self._sort_response_by_id(responses, name_from)
