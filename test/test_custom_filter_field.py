"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.custom_field import CustomField
from youtrack_api.model.custom_filter_field_all_of import CustomFilterFieldAllOf
from youtrack_api.model.filter_field import FilterField
globals()['CustomField'] = CustomField
globals()['CustomFilterFieldAllOf'] = CustomFilterFieldAllOf
globals()['FilterField'] = FilterField
from youtrack_api.model.custom_filter_field import CustomFilterField


class TestCustomFilterField(unittest.TestCase):
    """CustomFilterField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomFilterField(self):
        """Test CustomFilterField"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomFilterField()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()