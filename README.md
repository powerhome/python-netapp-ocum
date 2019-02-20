[![Build Status](https://api.travis-ci.org/djtaylor/python-netapp-uom.png)](https://api.travis-ci.org/djtaylor/python-netapp-uom)

# NetApp Unified OnCommand Manager (UOM) Client
This module is designed to interact with the HTTP API of the UOM for getting information about clusters, nodes, aggregates, volumes, and other NetApp objects. This is a lightweight wrapper which gets the JSON representation of each object retrieved from the API for local parsing.

**NOTE**: LUNs and Namespaces are not functionally tested since we don't have any in our infrastructure
**NOTE**: To see full API docs for UOM, visit: https://myuom.domain.com/apidocs
**NOTE**: Currently this is only tested against UOM 9.3

### Example Usage
This module includes example scripts [example scripts](examples/README.md) to help you get started.

### Tests
Testing is done with `unittest` and `nose` for discovery.

```
$ make test
```
