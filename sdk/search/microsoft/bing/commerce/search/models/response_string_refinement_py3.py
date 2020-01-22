# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_refinement_base_py3 import ResponseRefinementBase


class ResponseStringRefinement(ResponseRefinementBase):
    """Defines a facet refinement on a string field.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ResponseCategoryRefinement

    All required parameters must be populated in order to send to Azure.

    :param estimated_count: An estimate of the number of items in this
     refinement.
    :type estimated_count: long
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The actual filter value used to filter the list of items.
    :type value: str
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'estimated_count': {'key': 'estimatedCount', 'type': 'long'},
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
    }

    _subtype_map = {
        '_type': {'CategoryRefinement': 'ResponseCategoryRefinement'}
    }

    def __init__(self, *, estimated_count: int=None, value: str=None, **kwargs) -> None:
        super(ResponseStringRefinement, self).__init__(estimated_count=estimated_count, **kwargs)
        self.value = value
        self._type = 'StringRefinement'
