[![Build Status](https://api.travis-ci.org/djtaylor/python-netapp-uom.png)](https://api.travis-ci.org/djtaylor/python-netapp-uom)

# NetApp Unified OnCommand Manager (UOM) Client
This module is designed to interact with the HTTP API of the UOM for getting information about clusters, nodes, aggregates, volumes, and other NetApp objects. This is a lightweight wrapper which gets the JSON representation of each object retrieved from the API for local parsing.

**NOTE**: LUNs and Namespaces are not functionally tested since we don't have any in our infrastructure
**NOTE**: To see full API docs for UOM, visit: https://myuom.domain.com/apidocs
**NOTE**: Currently this is only tested against UOM 9.3

### Example Usage
The following shows some basic use cases for this module:

```python
import json
from netapp_uom.client import NetApp_UOM_Client

UOM_HOST='MY_UOM_HOST'
UOM_USER='MY_UOM_USER'
UOM_PASS='MY_UOM_PASSWORD'

# Create a new client connection
uom_client = NetApp_UOM_Client(UOM_HOST, UOM_USER, UOM_PASS, verify_ssl=False)

# Get a list of clusters and iterate
for cluster in uom_client.get_clusters():
  print('Cluster: {0}'.format(cluster.json['cluster']['label']))

  # Dump the raw JSON response
  print(cluster.json)

  # Dump attributes for the cluster
  for attr_key, attr_val in cluster:
    print('> {0}: {1}'.format(attr_key, attr_val))

# Get a list of volumes, filtered by cluster ID and SVM ID
# The filter only affects this query
filtered_volumes = uom_client.filter({
  'clusterId': '1',
  'svmId': '361'
}).get_volumes()

print(json.dumps(filtered_volumes.json, indent=2))

# Apply custom parameters when getting nodes
filtered_nodes = uom_client.get_nodes(params={
  'limit': 40,
  'clusterId': '1'
})

print(json.dumps(filtered_nodes.json, indent=2))


# Make a client with default filters applied to each query
filtered_client = uom_client.filter({
  'clusterId': '1',
})

# Retrieve volumes and nodes using the defined filters
filtered_client.get_volumes()
filtered_client.get_nodes()

```

### Tests
Testing is done with `unittest` and `nose` for discovery.

```
$ make test
```
