"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.work_item_type import WorkItemType
from youtrack_api.model.work_time_settings import WorkTimeSettings
globals()['WorkItemType'] = WorkItemType
globals()['WorkTimeSettings'] = WorkTimeSettings
from youtrack_api.model.global_time_tracking_settings import GlobalTimeTrackingSettings


class TestGlobalTimeTrackingSettings(unittest.TestCase):
    """GlobalTimeTrackingSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGlobalTimeTrackingSettings(self):
        """Test GlobalTimeTrackingSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GlobalTimeTrackingSettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
