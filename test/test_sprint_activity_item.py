"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.issue import Issue
from youtrack_api.model.multi_value_activity_item import MultiValueActivityItem
from youtrack_api.model.sprint import Sprint
from youtrack_api.model.sprint_activity_item_all_of import SprintActivityItemAllOf
globals()['Issue'] = Issue
globals()['MultiValueActivityItem'] = MultiValueActivityItem
globals()['Sprint'] = Sprint
globals()['SprintActivityItemAllOf'] = SprintActivityItemAllOf
from youtrack_api.model.sprint_activity_item import SprintActivityItem


class TestSprintActivityItem(unittest.TestCase):
    """SprintActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSprintActivityItem(self):
        """Test SprintActivityItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SprintActivityItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()