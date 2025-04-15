# MODULE - Graph Users and Groups

**Date created** | 01/03/2025

**Last updated** | 04/09/2025

## Author and Contributors

**Author** | Gianni DePaola

**Author** | Nick Biacsi (Slof)

## Script Functionality

### Why was it written?
Create a reusable module to handle certain API calls to MS Graph relating to users and groups.

### Requirements
Python Modules: requests, graph-headers  
Graph API permissions: User.Read.All, Group.Read.All

### Deployment Instructions
```pip install git+https://unionhomemortgage.visualstudio.com/IT%20Security/_git/MODULE-graph_users_groups```

### Classes and Functions

#### Class: Users
##### get_entra_user(upn: str) -> dict
Gets an Entra user by their UPN.

**Args:**
- `upn` (str): The user's User Principal Name (UPN)

**Returns:**
- `dict`: The user object from Graph API

##### get_user_groups(user: str) -> list
Returns the groups that a user is a member of.

**Args:**
- `user` (str): The user's User Principal Name (UPN) or id.

**Returns:**
- `list`: A list of group names that the user is a member of.

##### disable_entra_account(user_id: str) -> None
Disables a user's Entra account.

**Args:**
- `user_id` (str): The user's ID or UPN.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### enable_entra_account(user_id: str) -> None
Enables a user's Entra account.

**Args:**
- `user_id` (str): The user's ID or UPN.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### revoke_signin_sessions(user_id: str) -> None
Revokes all sign-in sessions for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### get_user_authenticator_app(user_id: str) -> list
Gets the Microsoft authenticator apps for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `list`: A list of authenticator app methods for the user.

##### remove_user_authenticator_app(user_id: str, method_id: str) -> None
Removes the authenticator app for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the authenticator app method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### remove_user_authenticator_phone(user_id: str, method_id: str) -> None
Removes a phone method for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the phone method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### remove_user_authenticator_fido2(user_id: str, method_id: str) -> None
Removes a FIDO2 method for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the FIDO2 method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### remove_user_authenticator_email(user_id: str, method_id: str) -> None
Removes an email method for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the email method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### remove_user_authenticator_softwareoath(user_id: str, method_id: str) -> None
Removes a software OATH method for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the software OATH method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### remove_user_authenticator_tap(user_id: str, method_id: str) -> None
Removes a temporary access pass (TAP) method for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.
- `method_id` (str): The ID of the TAP method to remove.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `None`

##### get_user_authentication_methods(user_id: str) -> list
Gets the authentication methods for a user.

**Args:**
- `user_id` (str): The user's ID or UPN.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `list`: A list of authentication methods for the user.

#### Class: Groups
##### get_group_users(group_id: str) -> list
Returns the users in a group.

**Args:**
- `group_id` (str): The group's ID.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `list`: A list of user names in the group.

#### Class: IdentityProtection
##### get_risky_users() -> list[dict]
Gets high and medium risky users from the Microsoft Graph API.

**Raises:**
- `GraphAPIError`: If the API call fails.

**Returns:**
- `list[dict]`: A list of dictionaries containing `userPrincipalName` and `riskLastUpdatedDateTime`.

##### dismiss_user_risk(user_identifier: str) -> None
Dismisses the risk for a user.

**Args:**
- `user_identifier` (str): The UPN or ID of the user.

**Raises:**
- `GraphAPIError`: If the API call fails or if the user ID cannot be retrieved.

**Returns:**
- `None`

### Error Handling

#### Class: GraphAPIError
Custom exception for Graph API errors.

**Args:**
- `status_code` (int): The HTTP status code returned by the API.
- `message` (str): The error message returned by the API.

**Usage:**
This exception is raised when an API call fails, allowing the calling code to handle the error appropriately.