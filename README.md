[![Build Status](https://api.travis-ci.org/djtaylor/python-netapp-ocum.png)](https://api.travis-ci.org/djtaylor/python-netapp-ocum)

# NetApp OnCommand Unified Manager (OCUM)
This module is designed to read information from the NetApp OCUM to gather information about your storage infrastructure.

### Python3
The initial release is targeting support for Python 3. Python 2 support is not planned.

### Caveats
The first release of this module may not have full support for Namespaces and LUNs. We are not using either of those object types in our infrastructure, so I have no way to initially test or get example API responses.

**NOTE**: This module only supports Python 3
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
