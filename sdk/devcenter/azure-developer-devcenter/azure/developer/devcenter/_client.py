# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import Any, TYPE_CHECKING

from azure.core import PipelineClient
from azure.core.rest import HttpRequest, HttpResponse

from ._configuration import DevCenterClientConfiguration
from ._serialization import Deserializer, Serializer
from .operations import DevBoxesOperations, DevCenterOperations, EnvironmentsOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Dict

    from azure.core.credentials import TokenCredential


class DevCenterClient:  # pylint: disable=client-accepts-api-version-keyword
    """DevBox API.

    :ivar dev_center: DevCenterOperations operations
    :vartype dev_center: azure.developer.devcenter.operations.DevCenterOperations
    :ivar dev_boxes: DevBoxesOperations operations
    :vartype dev_boxes: azure.developer.devcenter.operations.DevBoxesOperations
    :ivar environments: EnvironmentsOperations operations
    :vartype environments: azure.developer.devcenter.operations.EnvironmentsOperations
    :param tenant_id: The tenant to operate on. Required.
    :type tenant_id: str
    :param dev_center: The DevCenter to operate on. Required.
    :type dev_center: str
    :param credential: Credential needed for the client to connect to Azure. Required.
    :type credential: ~azure.core.credentials.TokenCredential
    :param dev_center_dns_suffix: The DNS suffix used as the base for all devcenter requests.
     Default value is "devcenter.azure.com".
    :type dev_center_dns_suffix: str
    :keyword api_version: Api Version. Default value is "2022-03-01-preview". Note that overriding
     this default value may result in unsupported behavior.
    :paramtype api_version: str
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no
     Retry-After header is present.
    """

    def __init__(
        self,
        tenant_id: str,
        dev_center: str,
        credential: "TokenCredential",
        dev_center_dns_suffix: str = "devcenter.azure.com",
        **kwargs: Any
    ) -> None:
        _endpoint = "https://{tenantId}-{devCenter}.{devCenterDnsSuffix}"
        self._config = DevCenterClientConfiguration(
            tenant_id=tenant_id,
            dev_center=dev_center,
            credential=credential,
            dev_center_dns_suffix=dev_center_dns_suffix,
            **kwargs
        )
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.dev_center = DevCenterOperations(self._client, self._config, self._serialize, self._deserialize)
        self.dev_boxes = DevBoxesOperations(self._client, self._config, self._serialize, self._deserialize)
        self.environments = EnvironmentsOperations(self._client, self._config, self._serialize, self._deserialize)

    def send_request(self, request: HttpRequest, **kwargs: Any) -> HttpResponse:
        """Runs the network request through the client's chained policies.

        >>> from azure.core.rest import HttpRequest
        >>> request = HttpRequest("GET", "https://www.example.org/")
        <HttpRequest [GET], url: 'https://www.example.org/'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/dpcodegen/python/send_request

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "tenantId": self._serialize.url("self._config.tenant_id", self._config.tenant_id, "str", skip_quote=True),
            "devCenter": self._serialize.url(
                "self._config.dev_center", self._config.dev_center, "str", skip_quote=True
            ),
            "devCenterDnsSuffix": self._serialize.url(
                "self._config.dev_center_dns_suffix", self._config.dev_center_dns_suffix, "str", skip_quote=True
            ),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> DevCenterClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
