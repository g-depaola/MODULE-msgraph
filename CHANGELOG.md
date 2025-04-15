# Changelog
Please follow best practices for updating the changelog.
- Reference a DevOps card, ticket or request number, or commit for each line item.
- Include an author name after each reference.

## VERSION - DATE (1.5.3 - 04/09/2025)

### Fixed
- Changed output type of `get_user_authentication_methods` and `get_user_authenticator_app` from `list` to `dict`

## VERSION - DATE (1.5.2 - 04/09/2025)

### Fixed
- Typo in phone methods function where thhere was an extra 'h'

## VERSION - DATE (1.5.1 - 04/09/2025)

### Fixed
- Standardized naming convention where a couple removal methods were named authenticator and some were named authentication. The standard is 'authentication'

## VERSION - DATE (1.5.0 - 04/09/2025)

### Feature
- Added `get_user_authentication_methods(user_id)` to the `Users` class to retrieve all authentication methods for a user. (Author: Gianni DePaola)
- Added `remove_user_authenticator_phone(user_id, method_id)` to the `Users` class to allow removal of phone authentication methods. (Author: Gianni DePaola)
- Added `remove_user_authenticator_fido2(user_id, method_id)` to the `Users` class to allow removal of FIDO2 authentication methods. (Author: Gianni DePaola)
- Added `remove_user_authentication_email(user_id, method_id)` to the `Users` class to allow removal of email authentication methods. (Author: Gianni DePaola)
- Added `remove_user_authentication_softwareoath(user_id, method_id)` to the `Users` class to allow removal of software OATH authentication methods. (Author: Gianni DePaola)
- Added `remove_user_authentication_tap(user_id, method_id)` to the `Users` class to allow removal of temporary access pass (TAP) authentication methods. (Author: Gianni DePaola)

## VERSION - DATE (1.4.0 - 04/03/2025)

### Feature
- Added `get_user_authenticator_app(user_id)` to the `Users` class to retrieve Microsoft authenticator apps for a user. (DevOps Card: 175810, Author: Gianni DePaola)
- Added `remove_user_authenticator_app(user_id, method_id)` to the `Users` class to allow removal of specific authenticator app methods. (DevOps Card: 175810, Author: Gianni DePaola)

## VERSION - DATE (1.3.1 - 03/31/2025)

### Fix
- Fixed `dismiss_user_risk(user_identifier)` to properly handle UPNs by retrieving the user ID before making the API call. (Author: Gianni DePaola)

## VERSION - DATE (1.3.0 - 03/31/2025)

### Feature
- Added `IdentityProtection` class with method:
  - `dismiss_user_risk(user_id)`: Dismisses the risk for a user.

## VERSION - DATE (1.2.0 - 03/31/2025)

### Feature
- Added `Users` class with methods:
  - `disable_entra_account(user_id)`
  - `enable_entra_account(user_id)`
  - `revoke_signin_sessions(user_id)`
- Added `Groups` class with method:
  - `get_group_users(group_id)`
- Added `IdentityProtection` class with method:
  - `get_risky_users()`

## VERSION - DATE (1.1.2 - 03/19/2025)

### Fix
- Add try/except to ```authenticate()``` function where ```get_graph_headers()``` is called.

## VERSION - DATE (1.1.1 - 03/18/2025)

### Fix
- Add ```GraphAPIError``` class to the ```__init__.py file```

## VERSION - DATE (1.1.0 - 03/18/2025)

### Feature
- Improved error checking, created a custom class for raising exceptions for Graph API errors.
- New function ```get_group_users(group_id)```: Returns a list of users within a group for a given group ID.

## VERSION - DATE (1.0.1 - 03/04/2025)

### Fixed
- File structure minor changes
- Corrected version number in setup.py
- Updated README with Graph API permission requirements

## VERSION - DATE (1.0.0 - 01/06/2025)

### Fixed
- N/A

### New Feature
- Added notes to functions
- Version 1.0 release

### Known Issues
- N/A

## VERSION - DATE (0.2.0 - 01/06/2025)

### Fixed
- Removed secrets (oops)

### New Feature
- Added new authenticate() function to allow setting global variables for tenant id, client id, and client secret.
    - Added function to init file.
- Added arg and return definitions.

### Known Issues
- N/A

## VERSION - DATE (0.1.0 - 01/03/2025)

### Fixed
- N/A

### New Feature
- Initial commit.

### Known Issues
- N/A