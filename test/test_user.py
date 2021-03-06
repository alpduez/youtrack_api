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
from youtrack_api.model.me import Me
from youtrack_api.model.saved_query import SavedQuery
from youtrack_api.model.user_profiles import UserProfiles
from youtrack_api.model.vcs_unresolved_user import VcsUnresolvedUser
globals()['IssueTag'] = IssueTag
globals()['Me'] = Me
globals()['SavedQuery'] = SavedQuery
globals()['UserProfiles'] = UserProfiles
globals()['VcsUnresolvedUser'] = VcsUnresolvedUser
from youtrack_api.model.user import User


class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUser(self):
        """Test User"""
        # FIXME: construct object with mandatory attributes with example values
        # model = User()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
