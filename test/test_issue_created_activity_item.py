"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.created_deleted_activity_item import CreatedDeletedActivityItem
from youtrack_api.model.issue import Issue
from youtrack_api.model.issue_created_activity_item_all_of import IssueCreatedActivityItemAllOf
globals()['CreatedDeletedActivityItem'] = CreatedDeletedActivityItem
globals()['Issue'] = Issue
globals()['IssueCreatedActivityItemAllOf'] = IssueCreatedActivityItemAllOf
from youtrack_api.model.issue_created_activity_item import IssueCreatedActivityItem


class TestIssueCreatedActivityItem(unittest.TestCase):
    """IssueCreatedActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssueCreatedActivityItem(self):
        """Test IssueCreatedActivityItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IssueCreatedActivityItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()