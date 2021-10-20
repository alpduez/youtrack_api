# IssueAttachment

Represents a file that is attached to an issue or a comment.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**author** | [**User**](User.md) |  | [optional] 
**created** | **int** |  | [optional] [readonly] 
**updated** | **int** |  | [optional] [readonly] 
**size** | **int** |  | [optional] [readonly] 
**extension** | **str** |  | [optional] [readonly] 
**charset** | **str** |  | [optional] [readonly] 
**mime_type** | **str** |  | [optional] [readonly] 
**meta_data** | **str** |  | [optional] [readonly] 
**draft** | **bool** |  | [optional] [readonly] 
**removed** | **bool** |  | [optional] [readonly] 
**base64_content** | **str** |  | [optional] 
**url** | **str** |  | [optional] [readonly] 
**visibility** | [**Visibility**](Visibility.md) |  | [optional] 
**issue** | [**Issue**](Issue.md) |  | [optional] 
**comment** | [**IssueComment**](IssueComment.md) |  | [optional] 
**thumbnail_url** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


