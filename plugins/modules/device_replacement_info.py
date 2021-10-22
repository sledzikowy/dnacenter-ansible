#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_replacement_info
short_description: Information module for Device Replacement
description:
- Get all Device Replacement.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  faultyDeviceName:
    description:
    - FaultyDeviceName query parameter. Faulty Device Name.
    type: str
  faultyDevicePlatform:
    description:
    - FaultyDevicePlatform query parameter. Faulty Device Platform.
    type: str
  replacementDevicePlatform:
    description:
    - ReplacementDevicePlatform query parameter. Replacement Device Platform.
    type: str
  faultyDeviceSerialNumber:
    description:
    - FaultyDeviceSerialNumber query parameter. Faulty Device Serial Number.
    type: str
  replacementDeviceSerialNumber:
    description:
    - ReplacementDeviceSerialNumber query parameter. Replacement Device Serial Number.
    type: str
  replacementStatus:
    description:
    - >
      ReplacementStatus query parameter. Device Replacement status READY-FOR-REPLACEMENT, REPLACEMENT-IN-PROGRESS,
      REPLACEMENT-SCHEDULED, REPLACED, ERROR, NETWORK_READINESS_REQUESTED, NETWORK_READINESS_FAILED.
    type: list
  family:
    description:
    - Family query parameter. List of familiesRouters, Switches and Hubs, AP.
    type: list
  sortBy:
    description:
    - SortBy query parameter. SortBy this field. SortBy is mandatory when order is used.
    type: str
  sortOrder:
    description:
    - SortOrder query parameter. Order on displayNameASC,DESC.
    type: str
  offset:
    description:
    - Offset query parameter.
    type: int
  limit:
    description:
    - Limit query parameter.
    type: int
requirements:
- dnacentersdk >= 2.3.1
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Device Replacement reference
  description: Complete reference of the Device Replacement object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Device Replacement
  cisco.dnac.device_replacement_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    faultyDeviceName: string
    faultyDevicePlatform: string
    replacementDevicePlatform: string
    faultyDeviceSerialNumber: string
    replacementDeviceSerialNumber: string
    replacementStatus: []
    family: []
    sortBy: string
    sortOrder: string
    offset: 0
    limit: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "creationTime": 0,
          "family": "string",
          "faultyDeviceId": "string",
          "faultyDeviceName": "string",
          "faultyDevicePlatform": "string",
          "faultyDeviceSerialNumber": "string",
          "id": "string",
          "neighbourDeviceId": "string",
          "networkReadinessTaskId": "string",
          "replacementDevicePlatform": "string",
          "replacementDeviceSerialNumber": "string",
          "replacementStatus": "string",
          "replacementTime": 0,
          "workflowId": "string"
        }
      ],
      "version": "string"
    }
"""
