"""
    YouTrack REST API

    YouTrack issue tracking and project management system  # noqa: E501

    The version of the OpenAPI document: 2021.3
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import youtrack_api
from youtrack_api.model.backup_status import BackupStatus
from youtrack_api.model.user import User
globals()['BackupStatus'] = BackupStatus
globals()['User'] = User
from youtrack_api.model.database_backup_settings import DatabaseBackupSettings


class TestDatabaseBackupSettings(unittest.TestCase):
    """DatabaseBackupSettings unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatabaseBackupSettings(self):
        """Test DatabaseBackupSettings"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DatabaseBackupSettings()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
