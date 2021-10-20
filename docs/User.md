# User

Represents a user in YouTrack. Please note that the read-only properties of a user account, like              credentials, or email and so on, you can only change in               <a href=\"https://www.jetbrains.com/help/youtrack/devportal/?Hub-REST-API\">Hub REST API</a>.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **str** |  | [optional] [readonly] 
**full_name** | **str** |  | [optional] [readonly] 
**email** | **str** |  | [optional] [readonly] 
**jabber_account_name** | **str** |  | [optional] [readonly] 
**ring_id** | **str** |  | [optional] [readonly] 
**guest** | **bool** |  | [optional] [readonly] 
**online** | **bool** |  | [optional] [readonly] 
**banned** | **bool** |  | [optional] [readonly] 
**tags** | [**[IssueTag]**](IssueTag.md) |  | [optional] 
**saved_queries** | [**[SavedQuery]**](SavedQuery.md) |  | [optional] 
**avatar_url** | **str** |  | [optional] [readonly] 
**profiles** | [**UserProfiles**](UserProfiles.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


