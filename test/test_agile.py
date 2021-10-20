"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.agile_status import AgileStatus
from youtrack_api.model.color_coding import ColorCoding
from youtrack_api.model.column_settings import ColumnSettings
from youtrack_api.model.custom_field import CustomField
from youtrack_api.model.project import Project
from youtrack_api.model.sprint import Sprint
from youtrack_api.model.sprints_settings import SprintsSettings
from youtrack_api.model.swimlane_settings import SwimlaneSettings
from youtrack_api.model.user import User
from youtrack_api.model.user_group import UserGroup
globals()['AgileStatus'] = AgileStatus
globals()['ColorCoding'] = ColorCoding
globals()['ColumnSettings'] = ColumnSettings
globals()['CustomField'] = CustomField
globals()['Project'] = Project
globals()['Sprint'] = Sprint
globals()['SprintsSettings'] = SprintsSettings
globals()['SwimlaneSettings'] = SwimlaneSettings
globals()['User'] = User
globals()['UserGroup'] = UserGroup
from youtrack_api.model.agile import Agile


class TestAgile(unittest.TestCase):
    """Agile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAgile(self):
        """Test Agile"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Agile()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
