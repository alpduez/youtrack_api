"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.field_style import FieldStyle
from youtrack_api.model.issue import Issue
from youtrack_api.model.issue_tag_all_of import IssueTagAllOf
from youtrack_api.model.user import User
from youtrack_api.model.user_group import UserGroup
from youtrack_api.model.watch_folder import WatchFolder
globals()['FieldStyle'] = FieldStyle
globals()['Issue'] = Issue
globals()['IssueTagAllOf'] = IssueTagAllOf
globals()['User'] = User
globals()['UserGroup'] = UserGroup
globals()['WatchFolder'] = WatchFolder
from youtrack_api.model.issue_tag import IssueTag


class TestIssueTag(unittest.TestCase):
    """IssueTag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssueTag(self):
        """Test IssueTag"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IssueTag()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
