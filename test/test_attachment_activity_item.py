"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.attachment_activity_item_all_of import AttachmentActivityItemAllOf
from youtrack_api.model.created_deleted_activity_item import CreatedDeletedActivityItem
from youtrack_api.model.issue_attachment import IssueAttachment
globals()['AttachmentActivityItemAllOf'] = AttachmentActivityItemAllOf
globals()['CreatedDeletedActivityItem'] = CreatedDeletedActivityItem
globals()['IssueAttachment'] = IssueAttachment
from youtrack_api.model.attachment_activity_item import AttachmentActivityItem


class TestAttachmentActivityItem(unittest.TestCase):
    """AttachmentActivityItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAttachmentActivityItem(self):
        """Test AttachmentActivityItem"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AttachmentActivityItem()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
