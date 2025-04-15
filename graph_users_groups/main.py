import requests
from graph_headers import get_graph_headers

# Global Variables
HEADERS = ""
BASE_URL = "https://graph.microsoft.com/v1.0"

class GraphAPIError(Exception):
    """Custom exception for Graph API errors."""
    def __init__(self, status_code, message):
        self.status_code = status_code
        self.message = message
        super().__init__(f"Graph API Error {status_code}: {message}")

def authenticate(tenant_id: str, client_id: str, client_secret: str) -> dict[str, str]:
    '''
    This function takes the app registration credentials and generates Graph headers for authenticating API calls.

    Args:
        tenant_id (str): The Azure AD tenant ID
        client_id (str): The application (client) ID of an App Registration in the tenant
        client_secret (str): The client secret generated for the App Registration
    
    Returns:
        dict: A dictionary containing the headers for Graph API requests
    '''
    global HEADERS

    try:
        HEADERS = get_graph_headers(tenant_id, client_id, client_secret)
        return HEADERS
    except Exception as e:
        raise GraphAPIError(401, f"Authentication failed. Error: {str(e)}")

class Users:
    def get_entra_user(upn: str) -> dict:
        '''
        Gets an Entra user by their UPN

        Args:
            upn (str): The user's User Principal Name (UPN)
        
        Returns:
            dict: The user object from Graph API
        '''
        endpoint: str = f"{BASE_URL}/users/{upn}"
        payload = {}

        response = requests.request("GET", url=endpoint, headers=HEADERS, data=payload)

        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)

        return response.json()

    def get_user_groups(user: str) -> list:
        '''
        Returns the groups that a user is a member of.

        Args:
            user (str): The user's User Principal Name (UPN) or id.
        
        Returns:
            list: A list of group names that the user is a member of.
        '''
        endpoint: str = f"{BASE_URL}/users/{user}/memberOf"
        response = requests.get(endpoint, headers=HEADERS)

        # Check for request success
        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)

        # Extract group IDs from the response
        response_data = response.json()
        group_names = [group.get('displayName') for group in response_data.get('value', []) if 'displayName' in group]
        return group_names
    
    def disable_entra_account(user_id: str) -> None:
        '''
        Lock the specified user's Entra account.
        
        Args:
            user_id: The ID or UPN of the user to lock the account for.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.

        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}"
        body = {
            'accountEnabled': False
        }

        response = requests.patch(url, headers=HEADERS, json=body)
        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        return None

    def enable_entra_account(user_id: str) -> None:
        '''
        Enable the specified user's Entra account.
        
        Args:
            user_id: The ID or UPN of the user to enable the account for.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.    
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}"
        body = {
            'accountEnabled': True
        }

        response = requests.patch(url, headers=HEADERS, json=body)
        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        return None

    def revoke_signin_sessions(user_id: str) -> None:
        '''
        Revoke all sign-in sessions for a user.
        
        Args:
            user_id: The ID or UPN of the user to revoke sign-in sessions for.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.

        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/microsoft.graph.revokeSignInSessions"
        response = requests.post(url, headers=HEADERS)

        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)
        
        return None
    
    def get_user_authentication_methods(user_id: str) -> dict:
        '''
        Get the authentication methods for a user.
        
        Args:
            user_id: The ID or UPN of the user to get authentication methods for.
        
        Returns:
            A dictionary containing the authentication methods for the user.
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/methods"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)
        
        return response.json()

    def get_user_authenticator_app(user_id: str) -> dict:
        '''
        Get the Microsoft authenticator apps for a user.
        
        Args:
            user_id: The ID or UPN of the user to get authentication methods for.
        
        Returns:
            A dictionary containing the authenticator app methods for the user.
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/microsoftAuthenticatorMethods"
        response = requests.get(url, headers=HEADERS)

        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)
        
        return response.json()
    
    def remove_user_authenticator_app(user_id: str, method_id: str) -> None:
        '''
        Remove an authenticator app method for a user.
        
        Args:
            user_id: The ID or UPN of the user to remove the authenticator app method for.
            method_id: The ID of the authenticator app method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.

        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/microsoftAuthenticatorMethods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None
    
    def remove_user_authenticator_phone(user_id: str, method_id: str) -> None:
        '''
        Remove a phone method for a user.

        Args:
            user_id: The ID or UPN of the user to remove the phone method for.
            method_id: The ID of the phone method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/phoneMethods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None
    
    def remove_user_authenticator_fido2(user_id: str, method_id: str) -> None:
        '''
        Remove a FIDO2 method for a user.

        Args:
            user_id: The ID or UPN of the user to remove the FIDO2 method for.
            method_id: The ID of the FIDO2 method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/fido2Methods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None

    def remove_user_authenticator_email(user_id: str, method_id: str) -> None:
        '''
        Remove an email method for a user.

        Args:
            user_id: The ID or UPN of the user to remove the email method for.
            method_id: The ID of the email method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/emailMethods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None
    
    def remove_user_authenticator_softwareoath(user_id: str, method_id: str) -> None:
        '''
        Remove a software OATH method for a user.

        Args:
            user_id: The ID or UPN of the user to remove the software OATH method for.
            method_id: The ID of the software OATH method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/softwareOathMethods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None
    
    def remove_user_authenticator_tap(user_id: str, method_id: str) -> None:
        '''
        Remove a temporary access pass method for a user.

        Args:
            user_id: The ID or UPN of the user to remove the TAP method for.
            method_id: The ID of the TAP method to remove.
        
        Raises:
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        url = f"{BASE_URL}/users/{user_id}/authentication/temporaryAccessPassMethods/{method_id}"
        response = requests.delete(url, headers=HEADERS)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None

class Groups:
    def get_group_users(group_id: str) -> list:
        '''
        Returns the users in a group.

        Args:
            group_id (str): The group's id.

        Returns:
            list: A list of user names in the group.
        '''
        endpoint: str = f'{BASE_URL}/groups/{group_id}/members'
        response = requests.get(endpoint, headers=HEADERS)

        # Check for request success
        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)
        
        # Extract users from response
        response_data = response.json()
        user_names = [user.get('displayName') for user in response_data.get('value', []) if 'displayName' in user]
        return user_names

class IdentityProtection:
    def get_risky_users() -> list[dict]:
        '''
        Get high and medium risky users from the Microsoft Graph API.

        Raises:
            GraphAPIError: If the API call fails or if the response is not as expected.

        Returns:
            A list of dictionaries containing userPrincipalName and riskLastUpdatedDateTime of risky users.
        '''
        url = f"{BASE_URL}/identityProtection/riskyUsers"
        # Filter for high and medium risk users that have a risk state of atRisk or confirmedCompromised
        params = {
            '$filter': "(RiskState eq 'atRisk' or RiskState eq 'confirmedCompromised') and (RiskLevel eq 'high' or RiskLevel eq 'medium')",
            '$select': "RiskLevel,RiskState,UserPrincipalName,RiskLastUpdatedDateTime"
        }
        
        response = requests.get(url, headers=HEADERS, params=params)
        
        if response.status_code != 200:
            raise GraphAPIError(response.status_code, response.text)
        
        risky_users_full = response.json()['value']
        # Create a list of dictionaries with userPrincipalName and riskLastUpdatedDateTime
        risky_users_info = [{'userPrincipalName': user['userPrincipalName'], 'riskLastUpdatedDateTime': user['riskLastUpdatedDateTime']} for user in risky_users_full]
        return risky_users_info
    
    def dismiss_user_risk(user_identifier: str) -> tuple[bool, str]:
        '''
        Dismiss the risk for a user.

        Args:
            user_identifier (str): The UPN or ID of the user to dismiss the risk for.

        Raises:    
            GraphAPIError: If the API call fails or if the user ID cannot be retrieved.
        
        Returns:
            None
        '''
        # If the input is a UPN, retrieve the user ID
        if "@" in user_identifier:  # Assuming UPN contains '@'
            user = Users.get_entra_user(user_identifier)
            user_id = user.get("id")
            if not user_id:
                raise GraphAPIError(400, "Unable to retrieve user ID for the provided UPN.")
        else:
            user_id = user_identifier

        url = f"{BASE_URL}/identityProtection/riskyUsers/dismiss"
        body = {
            "userIds": [user_id]
        }

        response = requests.post(url, headers=HEADERS, json=body)

        if response.status_code != 204:
            raise GraphAPIError(response.status_code, response.text)
        
        return None