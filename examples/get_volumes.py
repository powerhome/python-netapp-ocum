import json
from netapp_uom.client import NetApp_UOM_Client

# Create a new client
uom_client = NetApp_UOM_Client('hostname', 'username', 'password')

# Get all volumes from the UOM
all_volumes = uom_client.get_volumes()

# Dump the JSON for all volumes to stdout
print('All UOM Volumes:')
print(json.dumps(all_volumes.json, indent=2))

# Do something with each volume
for volume in all_volumes:

    # Show the volumes JSON
    print('Volume Name: {0}'.format(volume['volume']['label']))
    print('Volume ID: {0}'.format(volume['id']))

    print(json.dumps(volume.json, indent=2))

# Get a specific subset of clients
filtered_clients = uom_client.get_volumes(params={
    'clusterId': '1',
    'aggregateId': '1'
})
