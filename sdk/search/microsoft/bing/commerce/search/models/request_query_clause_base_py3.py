# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RequestQueryClauseBase(Model):
    """Defines the abstract base type for a query clause.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: RequestMatch, RequestQueryClauseBlock,
    RequestLocationMatch

    All required parameters must be populated in order to send to Azure.

    :param _type: Required. Constant filled by server.
    :type _type: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        '_type': {'key': '_type', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'Match': 'RequestMatch', 'QueryClauseBlock': 'RequestQueryClauseBlock', 'LocationMatch': 'RequestLocationMatch'}
    }

    def __init__(self, **kwargs) -> None:
        super(RequestQueryClauseBase, self).__init__(**kwargs)
        self._type = None
