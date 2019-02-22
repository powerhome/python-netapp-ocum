import unittest
from unittest import mock
from netapp_ocum.http import NetApp_OCUM_HTTP
from netapp_ocum.settings_test import NetApp_OCUM_Settings_Mock

def mock_get_request(*args, **kwargs):
    """
    Generate mock responses for testing.
    """
    mock_settings = NetApp_OCUM_Settings_Mock()

    def construct_mock_url(path):
        return 'https://{0}:{1}/rest/{2}'.format(
            mock_settings.api_host, mock_settings.api_port, path
        )

    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    # Cluster template values
    CLUSTER_ONE = {
        'id': 1,
        'label': 'cluster-one',
        'unsupportedStatisticTypes': []
    }
    CLUSTER_TWO = {
        'id': 2,
        'label': 'cluster-two',
        'unsupportedStatisticTypes': []
    }

    # Node template values
    NODE_ONE = {
        'id': 1,
        'label': 'cluster-one-node',
        'unsupportedStatisticTypes': []
    }
    NODE_TWO = {
        'id': 2,
        'label': 'cluster-two-node',
        'unsupportedStatisticTypes': []
    }

    # Aggregate template values
    AGGREGATE_ONE = {
        'id': 1,
        'label': 'cluster_one_aggregate',
        'unsupportedStatisticTypes': []
    }
    AGGREGATE_TWO = {
        'id': 2,
        'label': 'cluster_two_aggregate',
        'unsupportedStatisticTypes': []
    }

    # SVM template values
    SVM_ONE = {
        'id': 1,
        'label': 'cluster-one-svm',
        'unsupportedStatisticTypes': []
    }
    SVM_TWO = {
        'id': 2,
        'label': 'cluster-two-svm',
        'unsupportedStatisticTypes': []
    }

    # Volume template values
    VOLUME_ONE = {
        'id': 1,
        'label': 'cluster-one-volume',
        'unsupportedStatisticTypes': []
    }
    VOLUME_TWO = {
        'id': 2,
        'label': 'cluster-two-volume',
        'unsupportedStatisticTypes': []
    }

    # LIF template values
    LIF_ONE = {
        'id': 1,
        'label': 'cluster-one-node_lif',
        'unsupportedStatisticTypes': []
    }
    LIF_TWO = {
        'id': 2,
        'label': 'cluster-two-node_lif',
        'unsupportedStatisticTypes': []
    }

    # Port template values
    PORT_ONE = {
        'id': 1,
        'label': 'port-one',
        'unsupportedStatisticTypes': []
    }
    PORT_TWO = {
        'id': 2,
        'label': 'port-two',
        'unsupportedStatisticTypes': []
    }

    # Template value for links
    _LINKS = {
        'self': {
            'href': 'https://127.0.0.1/rest'
        },
        'curies': [
            {
                'href': 'https://127.0.0.1/rest/{#rel}',
                'name': 'netapp',
                'templated': True
            }
        ]
    }

    url_mappings = {
        construct_mock_url('clusters'): MockResponse(
            {
              "_embedded": {
                "netapp:clusterInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "networkAddress": "cluster-one.mydomain.com",
                    "nodeCount": 1,
                    "availableCapacity": 9000.005,
                    "iops": 8000.005,
                    "osVersion": "9.3P9",
                    "totalCapacity": 20000.005,
                    "serial": "1-11-111111",
                    "mbps": 300.005,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "OK",
                    "id": CLUSTER_ONE['id'],
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "networkAddress": "cluster-two.mydomain.com",
                    "nodeCount": 1,
                    "availableCapacity": 9000.005,
                    "iops": 8000.005,
                    "osVersion": "9.3P9",
                    "totalCapacity": 20000.005,
                    "serial": "1-11-111111",
                    "mbps": 300.005,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "OK",
                    "id": CLUSTER_TWO['id'],
                  },
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('nodes'): MockResponse(
            {
              "_embedded": {
                "netapp:nodeInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "availableCapacity": 9000.005,
                    "iops": 900.005,
                    "totalCapacity": 30000.005,
                    "flashCacheReadsPercent": None,
                    "usedHeadroom": 75.989,
                    "mbps": 90.5324,
                    "latency": 0.15683,
                    "utilization": 29.1943,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "OK",
                    "id": NODE_ONE['id'],
                    "node": NODE_ONE,
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "availableCapacity": 9000.005,
                    "iops": 900.005,
                    "totalCapacity": 30000.005,
                    "flashCacheReadsPercent": None,
                    "usedHeadroom": 75.989,
                    "mbps": 90.5324,
                    "latency": 0.15683,
                    "utilization": 29.1943,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "OK",
                    "id": NODE_TWO['id'],
                    "node": NODE_TWO,
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('aggregates'): MockResponse(
            {
              "_embedded": {
                "netapp:aggregateInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "aggregate": AGGREGATE_ONE,
                    "aggregateType": "Hybrid",
                    "availableCapacity": 500.453345,
                    "iops": 1500.32425,
                    "totalCapacity": 60000.4253524,
                    "aggregateDerivedType": "Hybrid (Flash Pool)",
                    "usedHeadroom": 15.02342,
                    "mbps": 90.369907,
                    "latency": 2.0235,
                    "utilization": 45.99594,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "ERROR",
                    "id": AGGREGATE_ONE['id'],
                    "node": NODE_ONE
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "aggregate": AGGREGATE_TWO,
                    "aggregateType": "HDD",
                    "availableCapacity": 5009.7142639160156,
                    "iops": 150.08,
                    "totalCapacity": 20000.83071899414,
                    "aggregateDerivedType": "HDD",
                    "usedHeadroom": 25.2698,
                    "mbps": 45.81697,
                    "latency": 4.313,
                    "utilization": 23.11369,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "ERROR",
                    "id": AGGREGATE_TWO['id'],
                    "node": NODE_TWO
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('aggregates/capacity-utilization'): MockResponse(
            {
              "_embedded": {
                "netapp:aggregateCapacityAndUtilizationList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "aggregate": AGGREGATE_ONE,
                    "raidType": "RAID-DP",
                    "aggregateType": "HDD",
                    "snapLockType": "Non-Snaplock",
                    "aggregateState": "Online",
                    "daysToFull": 1,
                    "totalDataCapacity": 1,
                    "snapshotReserveUsedCapacity": 0,
                    "resourceKey": "SOME_UUID:type=aggregate,uuid=SOME_UUID",
                    "usedDataCapacity": 1,
                    "usedDataPercentage": 1,
                    "availableDataCapacity": 1,
                    "availableDataPercentage": 1,
                    "dailyGrowthRatePercentage": 0,
                    "snapshotReserveUsedPercentage": 0,
                    "snapshotReserveAvailableCapacity": 1,
                    "snapshotReserveAvailablePercentage": 100,
                    "snapshotReserveTotalCapacity": 1,
                    "snapshotCopiesReserveFullThresholdPercentage": "90",
                    "totalCommitted": 1,
                    "growthRateSensitivityThreshold": "2.0",
                    "growthRateThresholdPercentage": "1",
                    "spaceFullThresholdPercentage": "90",
                    "spaceNearlyFullThresholdPercentage": "80",
                    "overcommittedCapacityPercentage": 0,
                    "overcommittedThresholdPercentage": "100",
                    "nearlyOvercommittedThresholdPercentage": "95",
                    "daysUntilFullThreshold": "7",
                    "externalCapacityTierSpaceUsed": 0,
                    "externalCapacityTier": None,
                    "haPair": "my_ha_pair",
                    "node": NODE_ONE
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "aggregate": AGGREGATE_TWO,
                    "raidType": "RAID-DP",
                    "aggregateType": "SSD",
                    "snapLockType": "Non-Snaplock",
                    "aggregateState": "Online",
                    "daysToFull": 1,
                    "totalDataCapacity": 1,
                    "snapshotReserveUsedCapacity": 0,
                    "resourceKey": "SOME_UUID:type=aggregate,uuid=SOME_UUID",
                    "usedDataCapacity": 1,
                    "usedDataPercentage": 1,
                    "availableDataCapacity": 1,
                    "availableDataPercentage": 1,
                    "dailyGrowthRatePercentage": 0,
                    "snapshotReserveUsedPercentage": 0,
                    "snapshotReserveAvailableCapacity": 1,
                    "snapshotReserveAvailablePercentage": 100,
                    "snapshotReserveTotalCapacity": 1,
                    "snapshotCopiesReserveFullThresholdPercentage": "90",
                    "totalCommitted": 1,
                    "growthRateSensitivityThreshold": "2.0",
                    "growthRateThresholdPercentage": "1",
                    "spaceFullThresholdPercentage": "90",
                    "spaceNearlyFullThresholdPercentage": "80",
                    "overcommittedCapacityPercentage": 0,
                    "overcommittedThresholdPercentage": "100",
                    "nearlyOvercommittedThresholdPercentage": "95",
                    "daysUntilFullThreshold": "7",
                    "externalCapacityTierSpaceUsed": 0,
                    "externalCapacityTier": None,
                    "haPair": "my_ha_pair",
                    "node": NODE_TWO
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('svms'): MockResponse(
            {
              "_embedded": {
                "netapp:svmInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "availableCapacity": 9000.9481010437011719,
                    "iops": None,
                    "totalCapacity": 10000.9500007629394531,
                    "svm": SVM_ONE,
                    "mbps": None,
                    "latency": None,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "WARNING",
                    "id": SVM_ONE['id'],
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "availableCapacity": 9000.9471092224121094,
                    "iops": None,
                    "totalCapacity": 20000.9500007629394531,
                    "svm": SVM_TWO,
                    "mbps": None,
                    "latency": None,
                    "numberOfHours": 72,
                    "policies": [],
                    "status": "WARNING",
                    "id": SVM_TWO['id'],
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('volumes/capacity-utilization'): MockResponse(
            {
              "_embedded": {
                "netapp:volumeCapacityAndUtilizationList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "volume": VOLUME_ONE,
                    "compressionSpaceSavings": 0,
                    "snapLockType": "Non-Snaplock",
                    "tieringPolicy": "Snapshot-Only",
                    "spaceGuarantee": "Volume",
                    "daysToFull": None,
                    "totalDataCapacity": 1,
                    "snapshotReserveUsedCapacity": 1,
                    "compression": "Disabled",
                    "resourceKey": "SOME_UUID:type=volume,uuid=SOME_UUID",
                    "usedDataCapacity": 1,
                    "usedDataPercentage": 1,
                    "availableDataCapacity": 1,
                    "availableDataPercentage": 1,
                    "dailyGrowthRatePercentage": 1,
                    "snapshotReserveUsedPercentage": 1,
                    "snapshotReserveAvailableCapacity": 1,
                    "snapshotReserveAvailablePercentage": 1,
                    "snapshotReserveTotalCapacity": 1,
                    "snapshotCopiesReserveFullThresholdPercentage": "90",
                    "growthRateSensitivityThreshold": "2.0",
                    "growthRateThresholdPercentage": "1",
                    "spaceFullThresholdPercentage": "90",
                    "spaceNearlyFullThresholdPercentage": "80",
                    "quotaCommittedCapacity": 0,
                    "quotaOverCommittedCapacity": 0,
                    "totalNumberOfInodes": 1,
                    "snapshotAutoDelete": "Disabled",
                    "deduplication": "Disabled",
                    "deduplicationSpaceSavings": 1,
                    "thinProvisioned": "No",
                    "autoGrow": "Disabled",
                    "snapshotCopiesCountThreshold": "250",
                    "snapshotCopiesDaysUntilFullThreshold": "7",
                    "quotaNearlyOverCommittedThresholdPercentage": "95",
                    "inodesNearlyFullThresholdPercentage": "80",
                    "inodesFullThresholdPercentage": "90",
                    "cachingPolicy": "",
                    "cacheRetentionPriority": "",
                    "snapLockExpiryDate": "",
                    "protectionRole": "Destination",
                    "snapshotOverflowPercentage": 0,
                    "inodeUtilizationPercentage": 0,
                    "daysUntilFullThreshold": "7",
                    "svm": SVM_ONE,
                    "quotaOverCommittedThresholdPercentage": "100",
                    "id": VOLUME_ONE['id'],
                    "state": "Online"
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "volume": VOLUME_TWO,
                    "compressionSpaceSavings": 0,
                    "snapLockType": "Non-Snaplock",
                    "tieringPolicy": "Snapshot-Only",
                    "spaceGuarantee": "Volume",
                    "daysToFull": 1,
                    "totalDataCapacity": 1,
                    "snapshotReserveUsedCapacity": 1,
                    "compression": "Disabled",
                    "resourceKey": "SOME_UUID:type=volume,uuid=SOME_UUID",
                    "usedDataCapacity": 1,
                    "usedDataPercentage": 1,
                    "availableDataCapacity": 1,
                    "availableDataPercentage": 1,
                    "dailyGrowthRatePercentage": 1,
                    "snapshotReserveUsedPercentage": 1,
                    "snapshotReserveAvailableCapacity": 0,
                    "snapshotReserveAvailablePercentage": 0,
                    "snapshotReserveTotalCapacity": 1,
                    "snapshotCopiesReserveFullThresholdPercentage": "90",
                    "growthRateSensitivityThreshold": "2.0",
                    "growthRateThresholdPercentage": "1",
                    "spaceFullThresholdPercentage": "90",
                    "spaceNearlyFullThresholdPercentage": "80",
                    "quotaCommittedCapacity": 0,
                    "quotaOverCommittedCapacity": 0,
                    "totalNumberOfInodes": 1,
                    "snapshotAutoDelete": "Disabled",
                    "deduplication": "Disabled",
                    "deduplicationSpaceSavings": 1,
                    "thinProvisioned": "No",
                    "autoGrow": "Disabled",
                    "snapshotCopiesCountThreshold": "250",
                    "snapshotCopiesDaysUntilFullThreshold": "7",
                    "quotaNearlyOverCommittedThresholdPercentage": "95",
                    "inodesNearlyFullThresholdPercentage": "80",
                    "inodesFullThresholdPercentage": "90",
                    "cachingPolicy": "",
                    "cacheRetentionPriority": "",
                    "snapLockExpiryDate": "",
                    "protectionRole": "Destination",
                    "snapshotOverflowPercentage": 1,
                    "inodeUtilizationPercentage": 1,
                    "daysUntilFullThreshold": "7",
                    "svm": SVM_TWO,
                    "quotaOverCommittedThresholdPercentage": "100",
                    "id": VOLUME_TWO['id'],
                    "state": "Online"
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('volumes'): MockResponse(
            {
              "_embedded": {
                "netapp:volumeInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "volume": VOLUME_ONE,
                    "aggregate": AGGREGATE_ONE,
                    "tieringPolicy": "",
                    "availableCapacity": 1697.5632781982422,
                    "iops": 230.357,
                    "totalCapacity": 17059.840000152588,
                    "svm": SVM_ONE,
                    "mbps": 1.1475372,
                    "volumeType": "FlexVol",
                    "latency": 0.71895504,
                    "numberOfHours": 89,
                    "policies": [],
                    "status": "CRITICAL",
                    "id": VOLUME_ONE['id'],
                    "node": NODE_ONE
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "volume": VOLUME_TWO,
                    "aggregate": AGGREGATE_TWO,
                    "tieringPolicy": "",
                    "availableCapacity": 1499.266414642334,
                    "iops": 770.286,
                    "totalCapacity": 11796.480003356934,
                    "svm": SVM_TWO,
                    "mbps": 6.991844,
                    "volumeType": "FlexVol",
                    "latency": 1.96707,
                    "numberOfHours": 89,
                    "policies": [],
                    "status": "CRITICAL",
                    "id": VOLUME_TWO['id'],
                    "node": NODE_TWO
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('lifs'): MockResponse(
            {
              "_embedded": {
                "netapp:lifInventoryList": [
                  {
                    "currentLocation": "cluster-one-node:a0a-101",
                    "cluster": CLUSTER_ONE,
                    "homeNode": NODE_ONE,
                    "currentPort": PORT_TWO,
                    "homePort": PORT_ONE,
                    "iops": None,
                    "homeLocation": "cluster-one-node:a0a-101",
                    "svm": SVM_ONE,
                    "mbps": None,
                    "latency": None,
                    "lif": LIF_ONE,
                    "lifType": "Network LIF",
                    "numberOfHours": 72,
                    "currentNode": NODE_ONE,
                    "policies": [],
                    "role": "Data",
                    "status": "ERROR",
                    "id": LIF_ONE['id']
                  },
                  {
                    "currentLocation": "cluster-two-node:a0a-101",
                    "cluster": CLUSTER_TWO,
                    "homeNode": NODE_TWO,
                    "currentPort": PORT_TWO,
                    "homePort": PORT_TWO,
                    "iops": None,
                    "homeLocation": "cluster-two-node:a0a-101",
                    "svm": SVM_TWO,
                    "mbps": None,
                    "latency": None,
                    "lif": LIF_TWO,
                    "lifType": "Network LIF",
                    "numberOfHours": 72,
                    "currentNode": NODE_TWO,
                    "policies": [],
                    "role": "Data",
                    "status": "ERROR",
                    "id": LIF_TWO['id']
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('ports'): MockResponse(
            {
              "_embedded": {
                "netapp:portInventoryList": [
                  {
                    "cluster": CLUSTER_ONE,
                    "speed": None,
                    "portType": "Network Port",
                    "mbps": None,
                    "utilization": None,
                    "numberOfHours": 72,
                    "policies": [],
                    "role": "Data",
                    "status": "OK",
                    "id": PORT_ONE['id'],
                    "port": PORT_ONE,
                    "node": NODE_ONE
                  },
                  {
                    "cluster": CLUSTER_TWO,
                    "speed": None,
                    "portType": "Network Port",
                    "mbps": None,
                    "utilization": None,
                    "numberOfHours": 72,
                    "policies": [],
                    "role": "Data",
                    "status": "OK",
                    "id": PORT_TWO['id'],
                    "port": PORT_TWO,
                    "node": NODE_TWO
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 76
            },
            200
        ),
        construct_mock_url('events'): MockResponse(
            {
              "_embedded": {
                "netapp:eventDtoList": [
                  {
                    "objectId": 1,
                    "type": "platform.event.Event",
                    "resourceType": None,
                    "name": "Some event name",
                    "conditionMessage": "Some event message",
                    "timestamp": 1477749913000,
                    "severity": "error",
                    "impactArea": "CAPACITY",
                    "impactLevel": "RISK",
                    "sourceFullName": "svm:/vol",
                    "state": "NEW",
                    "isCurrent": None,
                    "isResolved": None,
                    "resolvedTimestamp": None,
                    "resolvedBy": None,
                    "acknowledgedTimestamp": None,
                    "acknowledgedBy": None,
                    "source": {
                      "objectId": 1,
                      "objectType": "inventory.ontap.storage.FlexVol"
                    },
                    "sourceResourceType": "VOLUME",
                    "assignedUser": None,
                    "assignedTimestamp": None,
                    "notesCount": 0,
                    "triggeredDuration": 1,
                    "resolvedDuration": None,
                    "acknowledgedDuration": None,
                    "assignedDuration": None,
                    "value": {
                      "objectId": 1,
                      "type": "com.netapp.dfm.entity.platform.event.BuiltInEventType[95, volume.snapshot-reserve-days-until-full]",
                      "resourceType": None,
                      "uniqueName": "volume-snapshot-reserve-days-until-full",
                      "internalName": "full",
                      "prettyName": "Volume Snapshot Reserve Days Until Full",
                      "severity": "error",
                      "isEventGenerationEnabled": True,
                      "sourceTypes": [
                        "volume"
                      ],
                      "eventGenerationEnabled": True,
                      "id": 1
                    },
                    "obsoleteTimestamp": None,
                    "obsoleteDuration": None,
                    "obsoleteCause": None,
                    "obsoleteCauseEventDto": None,
                    "jobId": None,
                    "eventUrl": None,
                    "clusterId": 1,
                    "clusterNodeId": None,
                    "vserverId": 1,
                    "annotationName": None,
                    "annotation": None,
                    "groups": None,
                    "sourceResourceTypeText": None,
                    "lastObservedTime": None,
                    "resolved": None,
                    "current": None,
                    "daysOutstanding": 1,
                    "eventDuration": None,
                    "id": 1
                  },
                  {
                    "objectId": 1,
                    "type": "platform.event.Event",
                    "resourceType": None,
                    "name": "Some event name",
                    "conditionMessage": "Some event message",
                    "timestamp": 1,
                    "severity": "warning",
                    "impactArea": "CAPACITY",
                    "impactLevel": "RISK",
                    "sourceFullName": "svm:/vol",
                    "state": "NEW",
                    "isCurrent": None,
                    "isResolved": None,
                    "resolvedTimestamp": None,
                    "resolvedBy": None,
                    "acknowledgedTimestamp": None,
                    "acknowledgedBy": None,
                    "source": {
                      "objectId": 1,
                      "objectType": "inventory.ontap.storage.FlexVol"
                    },
                    "sourceResourceType": "VOLUME",
                    "assignedUser": None,
                    "assignedTimestamp": None,
                    "notesCount": 0,
                    "triggeredDuration": 1,
                    "resolvedDuration": None,
                    "acknowledgedDuration": None,
                    "assignedDuration": None,
                    "value": {
                      "objectId": 1,
                      "type": "com.netapp.dfm.entity.platform.event.BuiltInEventType[72, volume.snapshot.reserve.space.depleted]",
                      "resourceType": None,
                      "uniqueName": "volume-snapshot-reserve-space-full",
                      "internalName": "over",
                      "prettyName": "Volume Snapshot Reserve Space Full",
                      "severity": "warning",
                      "isEventGenerationEnabled": True,
                      "sourceTypes": [
                        "volume"
                      ],
                      "eventGenerationEnabled": True,
                      "id": 1
                    },
                    "obsoleteTimestamp": None,
                    "obsoleteDuration": None,
                    "obsoleteCause": None,
                    "obsoleteCauseEventDto": None,
                    "jobId": None,
                    "eventUrl": None,
                    "clusterId": 1,
                    "clusterNodeId": None,
                    "vserverId": 1,
                    "annotationName": None,
                    "annotation": None,
                    "groups": None,
                    "sourceResourceTypeText": None,
                    "lastObservedTime": None,
                    "resolved": None,
                    "current": None,
                    "daysOutstanding": 1,
                    "eventDuration": None,
                    "id": 1
                  }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('namespaces'): MockResponse(
            {
              "_embedded": {
                "netapp:namespaceInventoryList": [
                  { 'key': 'value' }, { 'key': 'value' }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
        construct_mock_url('luns'): MockResponse(
            {
              "_embedded": {
                "netapp:lunInventoryList": [
                  { 'key': 'value' }, { 'key': 'value' }
                ]
              },
              "_links": _LINKS,
              "totalCount": 2
            },
            200
        ),
    }
    return url_mappings.get(args[0], MockResponse(None, 404))

class NetApp_OCUM_HTTP_Test(unittest.TestCase):
    """Tests for `netapp_ocum/http.py`."""

    def test_http_instance(self):
        """ Test a new HTTP interface. """
        http_interface = NetApp_OCUM_HTTP(NetApp_OCUM_Settings_Mock())
        self.assertIsInstance(http_interface, NetApp_OCUM_HTTP)

    @mock.patch('requests.get', side_effect=mock_get_request)
    def test_http_get_request(self, mock_get):
        """ Test the GET method for the HTTP interface. """
        http_interface = NetApp_OCUM_HTTP(NetApp_OCUM_Settings_Mock())
        response = http_interface.GET('volumes')
        self.assertIsInstance(response, dict)
