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
from youtrack_api.model.project import Project
globals()['FieldStyle'] = FieldStyle
globals()['Project'] = Project
from youtrack_api.model.project_color import ProjectColor


class TestProjectColor(unittest.TestCase):
    """ProjectColor unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testProjectColor(self):
        """Test ProjectColor"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ProjectColor()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
