import json
import requests
from threading import Thread

class NetApp_OCUM_HTTP(object):
    """
    Class object for handling HTTP requests/responses for the OCUM.
    """
    def __init__(self, settings):
        self.settings = settings

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
            raise Exception('Failed to GET {0}: {1}'.format(request_url, response.json()))

        responses[accept] = response.json()['_embedded'][embedded_key]

    def GET(self, url_path, accept, embedded_key, name_from, params={}):
        """
        Make a GET request to the OCUM API method with an optional filter. Start
        a thread for each accept type.
        """
        responses = {}
        threads = []

        api_url = 'https://{0}:{1}/api/ontap/{2}'.format(
            self.settings.api_host,
            self.settings.api_port,
            url_path
        )

        for accept_type in accept:
            t = Thread(target=self._GET_worker,
                       args=(api_url, params, accept_type, responses, embedded_key))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        # Extract object IDs
        object_ids = [x['id'] for x in responses[name_from[0]]]

        # Map objects
        mapped_objects = []

        for object_id in object_ids:
            mapped_object = {
                'id': object_id,
                'name': None,
                'type': url_path,
                'data': {}
            }
            for accept_type, accept_responses in responses.items():
                for accept_response in accept_responses:
                    if accept_type == name_from[0]:
                        if accept_response['id'] == object_id:
                            mapped_object['data'][accept_type] = accept_response

                            # Extract the name of the object
                            if accept_type == name_from[0]:
                                mapped_object['name'] = accept_response[name_from[1]][name_from[2]]

            mapped_objects.append(mapped_object)

        return mapped_objects
