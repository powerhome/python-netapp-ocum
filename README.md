# NetApp OnCommand Unified Manager (OCUM)
This module is designed to read information from the NetApp OCUM to gather information about your storage infrastructure.

### Python3 / Installation
The initial release is targeting support for Python 3. Python 2 support is not planned. To install this module:

```
$ pip3 install netapp-ocum

# Or to install from source
$ git clone https://github.com/powerhome/python-netapp-ocum
$ cd python-netapp-ocum
$ python3 setup.py install
```

### Getting Started
This repository includes an [example scripts](examples/README.md) directory to help you get started.

### Supported OCUM Versions
As of the initial release, functional testing has been done against the following versions of OCUM:

 - 9.3P9

Other versions may work, but have not been tested.

### OCUM API Documentation
You can view Swagger API documentation for NetApp OCUM by going to the following URL:

 - https://my-uom.domain.com/apidocs

This page lets you test HTTP queries, view available parameters, and return data for the request.

### Tests
Testing is done with `unittest` and `nose` for discovery.

```
$ make test
```
