# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_refinement_base import ResponseRefinementBase


class ResponseBoolRefinement(ResponseRefinementBase):
    """Defines a facet refinement on a boolean field.

    All required parameters must be populated in order to send to Azure.

    :param estimated_count: An estimate of the number of items in this
     refinement.
    :type estimated_count: long
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The actual filter value used to filter the list of items.
     The object includes this field only for filters with discrete values.
    :type value: bool
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'estimated_count': {'key': 'estimatedCount', 'type': 'long'},
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'bool'},
    }

    def __init__(self, **kwargs):
        super(ResponseBoolRefinement, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
        self._type = 'BoolRefinement'
