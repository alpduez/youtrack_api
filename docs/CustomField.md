# CustomField

Represents a custom field in YouTrack.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**localized_name** | **str** |  | [optional] 
**field_type** | [**FieldType**](FieldType.md) |  | [optional] 
**is_auto_attached** | **bool** |  | [optional] 
**is_displayed_in_issue_list** | **bool** |  | [optional] 
**ordinal** | **int** |  | [optional] 
**aliases** | **str** |  | [optional] 
**field_defaults** | [**CustomFieldDefaults**](CustomFieldDefaults.md) |  | [optional] 
**has_running_job** | **bool** |  | [optional] [readonly] 
**is_updateable** | **bool** |  | [optional] [readonly] 
**instances** | [**[ProjectCustomField]**](ProjectCustomField.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


