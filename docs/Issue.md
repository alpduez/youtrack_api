# Issue

Represents an issue in YouTrack.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_readable** | **str** |  | [optional] [readonly] 
**created** | **int** |  | [optional] [readonly] 
**updated** | **int** |  | [optional] [readonly] 
**resolved** | **int** |  | [optional] [readonly] 
**number_in_project** | **int** |  | [optional] [readonly] 
**project** | [**Project**](Project.md) |  | [optional] 
**summary** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**uses_markdown** | **bool** |  | [optional] 
**wikified_description** | **str** |  | [optional] [readonly] 
**reporter** | [**User**](User.md) |  | [optional] 
**updater** | [**User**](User.md) |  | [optional] 
**draft_owner** | [**User**](User.md) |  | [optional] 
**is_draft** | **bool** |  | [optional] [readonly] 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**votes** | **int** |  | [optional] [readonly] 
**comments** | [**[IssueComment]**](IssueComment.md) |  | [optional] 
**comments_count** | **int** |  | [optional] [readonly] 
**tags** | [**[IssueTag]**](IssueTag.md) |  | [optional] 
**links** | [**[IssueLink]**](IssueLink.md) |  | [optional] 
**external_issue** | [**ExternalIssue**](ExternalIssue.md) |  | [optional] 
**custom_fields** | [**[IssueCustomField]**](IssueCustomField.md) |  | [optional] 
**voters** | [**IssueVoters**](IssueVoters.md) |  | [optional] 
**watchers** | [**IssueWatchers**](IssueWatchers.md) |  | [optional] 
**attachments** | [**[IssueAttachment]**](IssueAttachment.md) |  | [optional] 
**subtasks** | [**IssueLink**](IssueLink.md) |  | [optional] 
**parent** | [**IssueLink**](IssueLink.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


