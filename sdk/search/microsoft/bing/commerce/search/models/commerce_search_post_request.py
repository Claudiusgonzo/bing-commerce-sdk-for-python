# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommerceSearchPostRequest(Model):
    """CommerceSearchPostRequest.

    :param market: The market where the results come from. Typically, `mkt` is
     the country where the user is making the request from.
    :type market: str
    :param client:
    :type client: ~microsoft.bing.commerce.search.models.RequestClient
    :param language: The language to use for user interface strings. You may
     specify the language using either a 2-letter or 4-letter code. Using
     4-letter codes is preferred.
    :type language: str
    :param query: The query that determines the result set match criteria.
    :type query: ~microsoft.bing.commerce.search.models.RequestQuery
    :param items: A description for how the items in the result set would look
     like.
    :type items: ~microsoft.bing.commerce.search.models.RequestItems
    :param aggregations:
    :type aggregations:
     list[~microsoft.bing.commerce.search.models.RequestAggregationBase]
    :param debug:  Default value: False .
    :type debug: bool
    :param search_instance_id: A saved search instance configuration to apply
     to current request. Default value: "Default" .
    :type search_instance_id: str
    """

    _attribute_map = {
        'market': {'key': 'market', 'type': 'str'},
        'client': {'key': 'client', 'type': 'RequestClient'},
        'language': {'key': 'language', 'type': 'str'},
        'query': {'key': 'query', 'type': 'RequestQuery'},
        'items': {'key': 'items', 'type': 'RequestItems'},
        'aggregations': {'key': 'aggregations', 'type': '[RequestAggregationBase]'},
        'debug': {'key': 'debug', 'type': 'bool'},
        'search_instance_id': {'key': 'searchInstanceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(CommerceSearchPostRequest, self).__init__(**kwargs)
        self.market = kwargs.get('market', None)
        self.client = kwargs.get('client', None)
        self.language = kwargs.get('language', None)
        self.query = kwargs.get('query', None)
        self.items = kwargs.get('items', None)
        self.aggregations = kwargs.get('aggregations', None)
        self.debug = kwargs.get('debug', False)
        self.search_instance_id = kwargs.get('search_instance_id', "Default")
