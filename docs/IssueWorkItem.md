# IssueWorkItem

Represents a work item in an issue.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | [**User**](User.md) |  | [optional] 
**creator** | [**User**](User.md) |  | [optional] 
**text** | **str** |  | [optional] 
**text_preview** | **str** |  | [optional] [readonly] 
**type** | [**WorkItemType**](WorkItemType.md) |  | [optional] 
**created** | **int** |  | [optional] 
**updated** | **int** |  | [optional] 
**duration** | [**DurationValue**](DurationValue.md) |  | [optional] 
**date** | **int** |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**uses_markdown** | **bool** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


