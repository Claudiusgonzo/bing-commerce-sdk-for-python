# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ResponseItem(Model):
    """Defines an item from your content catalog.

    :param index_id: The ID of the index the item belongs to.
    :type index_id: str
    :param item_id: An ID that uniquely identifies an item within the index.
    :type item_id: str
    :param score: A value that indicates how well the item matches the query.
     Higher values indicate a closer match.
    :type score: float
    :param fields: An object with the selected fields as properties.
    :type fields: object
    :param debug:
    :type debug:
     list[~microsoft.bing.commerce.search.models.ResponseDebugInfo]
    """

    _attribute_map = {
        'index_id': {'key': 'indexId', 'type': 'str'},
        'item_id': {'key': 'itemId', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
        'fields': {'key': 'fields', 'type': 'object'},
        'debug': {'key': 'debug', 'type': '[ResponseDebugInfo]'},
    }

    def __init__(self, *, index_id: str=None, item_id: str=None, score: float=None, fields=None, debug=None, **kwargs) -> None:
        super(ResponseItem, self).__init__(**kwargs)
        self.index_id = index_id
        self.item_id = item_id
        self.score = score
        self.fields = fields
        self.debug = debug