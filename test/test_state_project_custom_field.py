"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.bundle_project_custom_field import BundleProjectCustomField
from youtrack_api.model.custom_field import CustomField
from youtrack_api.model.project import Project
from youtrack_api.model.state_bundle import StateBundle
from youtrack_api.model.state_bundle_custom_field_defaults_all_of import StateBundleCustomFieldDefaultsAllOf
from youtrack_api.model.state_bundle_element import StateBundleElement
globals()['BundleProjectCustomField'] = BundleProjectCustomField
globals()['CustomField'] = CustomField
globals()['Project'] = Project
globals()['StateBundle'] = StateBundle
globals()['StateBundleCustomFieldDefaultsAllOf'] = StateBundleCustomFieldDefaultsAllOf
globals()['StateBundleElement'] = StateBundleElement
from youtrack_api.model.state_project_custom_field import StateProjectCustomField


class TestStateProjectCustomField(unittest.TestCase):
    """StateProjectCustomField unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStateProjectCustomField(self):
        """Test StateProjectCustomField"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StateProjectCustomField()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()