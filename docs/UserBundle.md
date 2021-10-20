# UserBundle

Represents a set of values that contains users. You can add to the set both individual user accounts and groups of users.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**[UserGroup]**](UserGroup.md) |  | [optional] 
**individuals** | [**[User]**](User.md) |  | [optional] 
**aggregated_users** | [**[User]**](User.md) |  | [optional] 
**is_updateable** | **bool** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


