"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.custom_field_activity_item_all_of import CustomFieldActivityItemAllOf
from youtrack_api.model.issue import Issue
from youtrack_api.model.single_value_activity_item import SingleValueActivityItem
globals()['CustomFieldActivityItemAllOf'] = CustomFieldActivityItemAllOf
globals()['Issue'] = Issue
globals()['SingleValueActivityItem'] = SingleValueActivityItem
from youtrack_api.model.project_activity_item import ProjectActivityItem


class TestProjectActivityItem(unittest.TestCase):
    """ProjectActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectActivityItem(self):
        """Test ProjectActivityItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectActivityItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()