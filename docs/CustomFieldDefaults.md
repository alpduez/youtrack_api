# CustomFieldDefaults

Represents default project-related settings of the custom field. These settings are applied at the moment when the custom field is attached to a project. After that, any changes in default settings do not affect the field settings for this project.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_be_empty** | **bool** |  | [optional] 
**empty_field_text** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**parent** | [**CustomField**](CustomField.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


