#!/usr/bin/env python3
import json
from netapp_ocum.client import NetApp_OCUM_Client

# Create a new client
ocum_client = NetApp_OCUM_Client('hostname', 'username', 'password')

# Get all volumes from the OCUM
all_volumes = ocum_client.get_volumes()

# Dump the JSON for all volumes to stdout
print('All OCUM Volumes:')
print(json.dumps(all_volumes.json, indent=2))

# Do something with each volume
for volume in all_volumes:

    # Show the volumes JSON
    print('Volume Name: {0}'.format(volume['volume']['label']))
    print('Volume ID: {0}'.format(volume['id']))

    print(json.dumps(volume.json, indent=2))

# Get a specific subset of clients
filtered_clients = ocum_client.get_volumes(params={
    'clusterId': '1',
    'aggregateId': '1'
})
