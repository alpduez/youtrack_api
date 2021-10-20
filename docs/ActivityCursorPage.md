# ActivityCursorPage

Represents a page object that wraps a list of issue activities. The main advantage of the page in comparision to a list of activities is cursors. The page provides boundary marks that allow continuous iteration over the activities from the place the page is finished.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reverse** | **bool** |  | [optional] [readonly] 
**before_cursor** | **str** |  | [optional] [readonly] 
**after_cursor** | **str** |  | [optional] [readonly] 
**has_before** | **bool** |  | [optional] [readonly] 
**has_after** | **bool** |  | [optional] [readonly] 
**activities** | [**[ActivityItem]**](ActivityItem.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


