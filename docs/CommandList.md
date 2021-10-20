# CommandList

Represents list of command and related comment in YouTrack. Can be used to either apply a command or get command suggestions.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** |  | [optional] 
**visibility** | [**CommandVisibility**](CommandVisibility.md) |  | [optional] 
**query** | **str** |  | [optional] 
**caret** | **int** |  | [optional] 
**silent** | **bool** |  | [optional] 
**uses_markdown** | **bool** |  | [optional] 
**run_as** | **str** |  | [optional] 
**commands** | [**[ParsedCommand]**](ParsedCommand.md) |  | [optional] 
**issues** | [**[Issue]**](Issue.md) |  | [optional] 
**suggestions** | [**[Suggestion]**](Suggestion.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


