#!/usr/bin/env python3
import json
from netapp_ocum.client import NetApp_OCUM_Client

# Create a new client
ocum_client = NetApp_OCUM_Client('hostname', 'username', 'password')

# Get performance metrics for volumes and aggregates
aggregate_metrics = ocum_client.get_aggregate_metrics(params={'limit': 5})
volume_metrics = ocum_client.get_volume_metrics(params={'limit': 10})

print(json.dumps(aggregate_metrics.json, indent=2))
print(json.dumps(volume_metrics.json, indent=2))
