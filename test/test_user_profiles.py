"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.general_user_profile import GeneralUserProfile
from youtrack_api.model.notifications_user_profile import NotificationsUserProfile
from youtrack_api.model.time_tracking_user_profile import TimeTrackingUserProfile
globals()['GeneralUserProfile'] = GeneralUserProfile
globals()['NotificationsUserProfile'] = NotificationsUserProfile
globals()['TimeTrackingUserProfile'] = TimeTrackingUserProfile
from youtrack_api.model.user_profiles import UserProfiles


class TestUserProfiles(unittest.TestCase):
    """UserProfiles unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserProfiles(self):
        """Test UserProfiles"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserProfiles()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
