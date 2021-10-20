# WatchFolder

A `WatchFolder` is an `IssueFolder` that let you enable notifications for a set  of issues that it enfolds. It is a common abstract ancestor for saved searches and issue tags.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**owner** | [**User**](User.md) |  | [optional] 
**visible_for** | [**UserGroup**](UserGroup.md) |  | [optional] 
**updateable_by** | [**UserGroup**](UserGroup.md) |  | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


