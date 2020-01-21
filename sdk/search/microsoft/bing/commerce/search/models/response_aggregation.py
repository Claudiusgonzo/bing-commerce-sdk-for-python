# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_task import ResponseTask


class ResponseAggregation(ResponseTask):
    """Defines an aggregation result.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ResponseFilter, ResponseDiscoveredFacets,
    ResponseFieldAggregationBase

    All required parameters must be populated in order to send to Azure.

    :param errors: A list of errors that happened to the task, if any.
    :type errors: list[~microsoft.bing.commerce.search.models.ResponseError]
    :param debug:
    :type debug:
     list[~microsoft.bing.commerce.search.models.ResponseDebugInfo]
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param name: The aggregation name as defined in the requset.
    :type name: str
    :param estimated_count: An estimated count of items in this aggregation.
    :type estimated_count: long
    :param aggregations: The list of child aggregations, if any.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.ResponseAggregation]
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'errors': {'key': 'errors', 'type': '[ResponseError]'},
        'debug': {'key': 'debug', 'type': '[ResponseDebugInfo]'},
        '_type': {'key': '_type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'estimated_count': {'key': 'estimatedCount', 'type': 'long'},
        'aggregations': {'key': 'aggregations', 'type': '[ResponseAggregation]'},
    }

    _subtype_map = {
        '_type': {'Filter': 'ResponseFilter', 'DiscoveredFacets': 'ResponseDiscoveredFacets', 'Response.FieldAggregationBase': 'ResponseFieldAggregationBase'}
    }

    def __init__(self, **kwargs):
        super(ResponseAggregation, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.estimated_count = kwargs.get('estimated_count', None)
        self.aggregations = kwargs.get('aggregations', None)
        self._type = 'Aggregation'
