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
from youtrack_api.model.issue_link_type import IssueLinkType
globals()['Issue'] = Issue
globals()['IssueLinkType'] = IssueLinkType
from youtrack_api.model.issue_link import IssueLink


class TestIssueLink(unittest.TestCase):
    """IssueLink unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssueLink(self):
        """Test IssueLink"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IssueLink()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
