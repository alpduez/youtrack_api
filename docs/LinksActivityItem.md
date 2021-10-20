# LinksActivityItem

Represents a change in the `issues` attribute of an IssueLink entity. That is, each issue has the `links` attribute that contains an array of IssueLink entities. Each of them represents a link between the target issue and a collection of issues. For example, a set of issues to which the target one is linked as \"Duplicated by\". The change in the list of these issues is represented by `LinksActivityItem` entity.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | [**Issue**](Issue.md) |  | [optional] 
**removed** | [**[Issue]**](Issue.md) |  | [optional] 
**added** | [**[Issue]**](Issue.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


