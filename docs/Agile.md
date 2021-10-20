# Agile

Represents an agile board configuration.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**owner** | [**User**](User.md) |  | [optional] 
**visible_for** | [**UserGroup**](UserGroup.md) |  | [optional] 
**visible_for_project_based** | **bool** |  | [optional] 
**updateable_by** | [**UserGroup**](UserGroup.md) |  | [optional] 
**updateable_by_project_based** | **bool** |  | [optional] 
**orphans_at_the_top** | **bool** |  | [optional] 
**hide_orphans_swimlane** | **bool** |  | [optional] 
**estimation_field** | [**CustomField**](CustomField.md) |  | [optional] 
**original_estimation_field** | [**CustomField**](CustomField.md) |  | [optional] 
**projects** | [**[Project]**](Project.md) |  | [optional] 
**sprints** | [**[Sprint]**](Sprint.md) |  | [optional] 
**current_sprint** | [**Sprint**](Sprint.md) |  | [optional] 
**column_settings** | [**ColumnSettings**](ColumnSettings.md) |  | [optional] 
**swimlane_settings** | [**SwimlaneSettings**](SwimlaneSettings.md) |  | [optional] 
**sprints_settings** | [**SprintsSettings**](SprintsSettings.md) |  | [optional] 
**color_coding** | [**ColorCoding**](ColorCoding.md) |  | [optional] 
**status** | [**AgileStatus**](AgileStatus.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


