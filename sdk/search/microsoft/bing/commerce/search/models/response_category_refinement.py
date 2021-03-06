# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .response_string_refinement import ResponseStringRefinement


class ResponseCategoryRefinement(ResponseStringRefinement):
    """Defines a facet refinement on a category field.

    All required parameters must be populated in order to send to Azure.

    :param estimated_count: An estimate of the number of items in this
     refinement.
    :type estimated_count: long
    :param _type: Required. Constant filled by server.
    :type _type: str
    :param value: The actual filter value used to filter the list of items.
    :type value: str
    :param refinements: A list of child category refinements.
    :type refinements:
     list[~microsoft.bing.commerce.search.models.ResponseCategoryRefinement]
    """

    _validation = {
        '_type': {'required': True},
    }

    _attribute_map = {
        'estimated_count': {'key': 'estimatedCount', 'type': 'long'},
        '_type': {'key': '_type', 'type': 'str'},
        'value': {'key': 'value', 'type': 'str'},
        'refinements': {'key': 'refinements', 'type': '[ResponseCategoryRefinement]'},
    }

    def __init__(self, **kwargs):
        super(ResponseCategoryRefinement, self).__init__(**kwargs)
        self.refinements = kwargs.get('refinements', None)
        self._type = 'CategoryRefinement'
