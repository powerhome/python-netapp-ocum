import json
from netapp_uom.client import NetApp_UOM_Client

"""
This example script shows how to create a filtered client, if you are only
interested in a subset of data from specific sections of your NetApp inventory.
"""

# Create a new client, filtered to a specific cluster and SVM
uom_client = NetApp_UOM_Client('hostname', 'username', 'password', filter={
    'clusterId': '1',
    'svmId': '1'
})

# Get all volumes for the cluster/SVM
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
