"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.issue_tag import IssueTag
from youtrack_api.model.project import Project
from youtrack_api.model.saved_query import SavedQuery
from youtrack_api.model.watch_folder import WatchFolder
globals()['IssueTag'] = IssueTag
globals()['Project'] = Project
globals()['SavedQuery'] = SavedQuery
globals()['WatchFolder'] = WatchFolder
from youtrack_api.model.issue_folder import IssueFolder


class TestIssueFolder(unittest.TestCase):
    """IssueFolder unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testIssueFolder(self):
        """Test IssueFolder"""
        # FIXME: construct object with mandatory attributes with example values
        # model = IssueFolder()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
