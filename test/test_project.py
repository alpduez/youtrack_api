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
from youtrack_api.model.issue_folder import IssueFolder
from youtrack_api.model.project_all_of import ProjectAllOf
from youtrack_api.model.user import User
from youtrack_api.model.user_group import UserGroup
globals()['Issue'] = Issue
globals()['IssueFolder'] = IssueFolder
globals()['ProjectAllOf'] = ProjectAllOf
globals()['User'] = User
globals()['UserGroup'] = UserGroup
from youtrack_api.model.project import Project


class TestProject(unittest.TestCase):
    """Project unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProject(self):
        """Test Project"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Project()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
