# Sprint

Represents a sprint that is associated with an agile board. Each sprint can include issues from one or more projects.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agile** | [**Agile**](Agile.md) |  | [optional] 
**name** | **str** |  | [optional] 
**goal** | **str** |  | [optional] 
**start** | **int** |  | [optional] 
**finish** | **int** |  | [optional] 
**archived** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**issues** | [**[Issue]**](Issue.md) |  | [optional] 
**unresolved_issues_count** | **int** |  | [optional] [readonly] 
**previous_sprint** | [**Sprint**](Sprint.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


