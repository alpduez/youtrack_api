"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.issue_folder import IssueFolder
from youtrack_api.model.suggestion import Suggestion
globals()['IssueFolder'] = IssueFolder
globals()['Suggestion'] = Suggestion
from youtrack_api.model.search_suggestions import SearchSuggestions


class TestSearchSuggestions(unittest.TestCase):
    """SearchSuggestions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSearchSuggestions(self):
        """Test SearchSuggestions"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SearchSuggestions()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
