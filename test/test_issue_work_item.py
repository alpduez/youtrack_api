"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.duration_value import DurationValue
from youtrack_api.model.issue import Issue
from youtrack_api.model.user import User
from youtrack_api.model.work_item_type import WorkItemType
globals()['DurationValue'] = DurationValue
globals()['Issue'] = Issue
globals()['User'] = User
globals()['WorkItemType'] = WorkItemType
from youtrack_api.model.issue_work_item import IssueWorkItem


class TestIssueWorkItem(unittest.TestCase):
    """IssueWorkItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssueWorkItem(self):
        """Test IssueWorkItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IssueWorkItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()