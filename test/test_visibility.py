"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.limited_visibility import LimitedVisibility
from youtrack_api.model.unlimited_visibility import UnlimitedVisibility
globals()['LimitedVisibility'] = LimitedVisibility
globals()['UnlimitedVisibility'] = UnlimitedVisibility
from youtrack_api.model.visibility import Visibility


class TestVisibility(unittest.TestCase):
    """Visibility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVisibility(self):
        """Test Visibility"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Visibility()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
