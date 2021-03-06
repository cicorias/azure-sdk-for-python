# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential

from ._configuration import MySQLManagementClientConfiguration
from .operations import ServersOperations
from .operations import ReplicasOperations
from .operations import ServerKeysOperations
from .operations import FirewallRulesOperations
from .operations import DatabasesOperations
from .operations import ConfigurationsOperations
from .operations import LocationBasedCapabilitiesOperations
from .operations import CheckVirtualNetworkSubnetUsageOperations
from .operations import CheckNameAvailabilityOperations
from .operations import Operations
from . import models


class MySQLManagementClient(object):
    """The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, log files and configurations with new business model.

    :ivar servers: ServersOperations operations
    :vartype servers: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.ServersOperations
    :ivar replicas: ReplicasOperations operations
    :vartype replicas: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.ReplicasOperations
    :ivar server_keys: ServerKeysOperations operations
    :vartype server_keys: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.ServerKeysOperations
    :ivar firewall_rules: FirewallRulesOperations operations
    :vartype firewall_rules: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.FirewallRulesOperations
    :ivar databases: DatabasesOperations operations
    :vartype databases: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.DatabasesOperations
    :ivar configurations: ConfigurationsOperations operations
    :vartype configurations: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.ConfigurationsOperations
    :ivar location_based_capabilities: LocationBasedCapabilitiesOperations operations
    :vartype location_based_capabilities: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.LocationBasedCapabilitiesOperations
    :ivar check_virtual_network_subnet_usage: CheckVirtualNetworkSubnetUsageOperations operations
    :vartype check_virtual_network_subnet_usage: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.CheckVirtualNetworkSubnetUsageOperations
    :ivar check_name_availability: CheckNameAvailabilityOperations operations
    :vartype check_name_availability: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.CheckNameAvailabilityOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.rdbms.mysql.v2020_07_01_privatepreview.operations.Operations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = MySQLManagementClientConfiguration(credential, subscription_id, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.servers = ServersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replicas = ReplicasOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.server_keys = ServerKeysOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.firewall_rules = FirewallRulesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.databases = DatabasesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.configurations = ConfigurationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.location_based_capabilities = LocationBasedCapabilitiesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_virtual_network_subnet_usage = CheckVirtualNetworkSubnetUsageOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.check_name_availability = CheckNameAvailabilityOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> MySQLManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
