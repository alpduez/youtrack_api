"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.command_limited_visibility_all_of import CommandLimitedVisibilityAllOf
from youtrack_api.model.command_visibility import CommandVisibility
from youtrack_api.model.user import User
from youtrack_api.model.user_group import UserGroup
globals()['CommandLimitedVisibilityAllOf'] = CommandLimitedVisibilityAllOf
globals()['CommandVisibility'] = CommandVisibility
globals()['User'] = User
globals()['UserGroup'] = UserGroup
from youtrack_api.model.command_limited_visibility import CommandLimitedVisibility


class TestCommandLimitedVisibility(unittest.TestCase):
    """CommandLimitedVisibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommandLimitedVisibility(self):
        """Test CommandLimitedVisibility"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommandLimitedVisibility()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
