"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.multi_value_activity_item import MultiValueActivityItem
from youtrack_api.model.visibility_activity_item_all_of import VisibilityActivityItemAllOf
from youtrack_api.model.visibility_group_activity_item import VisibilityGroupActivityItem
from youtrack_api.model.visibility_user_activity_item import VisibilityUserActivityItem
globals()['MultiValueActivityItem'] = MultiValueActivityItem
globals()['VisibilityActivityItemAllOf'] = VisibilityActivityItemAllOf
globals()['VisibilityGroupActivityItem'] = VisibilityGroupActivityItem
globals()['VisibilityUserActivityItem'] = VisibilityUserActivityItem
from youtrack_api.model.visibility_activity_item import VisibilityActivityItem


class TestVisibilityActivityItem(unittest.TestCase):
    """VisibilityActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testVisibilityActivityItem(self):
        """Test VisibilityActivityItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = VisibilityActivityItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()