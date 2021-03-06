# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestAggregationBase(Model):
    """Defines the abstract base type for an aggregation request.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: RequestFilter, RequestFieldAggregationBase,
    RequestDiscoverFacets

    All required parameters must be populated in order to send to Azure.

    :param name: A label that you specify for your aggregations, which the API
     passes through and returns with the response.
    :type name: str
    :param aggregations: A list of child aggregations.
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.RequestAggregationBase]
    :param _type: Required. Constant filled by server.
    :type _type: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'Filter': 'RequestFilter', 'Request.FieldAggregationBase': 'RequestFieldAggregationBase', 'DiscoverFacets': 'RequestDiscoverFacets'}
    }

    def __init__(self, *, name: str=None, aggregations=None, **kwargs) -> None:
        super(RequestAggregationBase, self).__init__(**kwargs)
        self.name = name
        self.aggregations = aggregations
        self._type = None
