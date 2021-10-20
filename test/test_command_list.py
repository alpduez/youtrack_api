"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.command_visibility import CommandVisibility
from youtrack_api.model.issue import Issue
from youtrack_api.model.parsed_command import ParsedCommand
from youtrack_api.model.suggestion import Suggestion
globals()['CommandVisibility'] = CommandVisibility
globals()['Issue'] = Issue
globals()['ParsedCommand'] = ParsedCommand
globals()['Suggestion'] = Suggestion
from youtrack_api.model.command_list import CommandList


class TestCommandList(unittest.TestCase):
    """CommandList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCommandList(self):
        """Test CommandList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CommandList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()