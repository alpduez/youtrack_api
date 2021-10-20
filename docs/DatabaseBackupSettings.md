# DatabaseBackupSettings

Represents database backup settings of the YouTrack instance.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** |  | [optional] 
**files_to_keep** | **int** |  | [optional] 
**cron_expression** | **str** |  | [optional] 
**archive_format** | **str** |  | [optional] 
**is_on** | **bool** |  | [optional] 
**available_disk_space** | **int** |  | [optional] [readonly] 
**notified_users** | [**[User]**](User.md) |  | [optional] 
**backup_status** | [**BackupStatus**](BackupStatus.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


