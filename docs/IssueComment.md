# IssueComment

Represents an existing issue comment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**uses_markdown** | **bool** |  | [optional] 
**text_preview** | **str** |  | [optional] [readonly] 
**created** | **int** |  | [optional] [readonly] 
**updated** | **int** |  | [optional] [readonly] 
**author** | [**User**](User.md) |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**attachments** | [**[IssueAttachment]**](IssueAttachment.md) |  | [optional] 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**deleted** | **bool** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


