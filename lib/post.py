import requests

headers = {
    "Content-Type": "application/json"
}



"""
Posts data to a specified URL using HTTP POST method with JSON payload.

Args:
- data (dict): A dictionary containing the data to be posted. It should include 'bridgeId'
    and 'apiKey' keys for ADD_BRIDGE URL, or 'nodeId' key for ADD_NODE URL.
- url (avl_url): An avl_url Enum value representing the URL where the POST request will be sent.

Returns:
- bool: True if the data was successfully posted and the response status code was 201.
    False otherwise.

Prints:
- "Invalid bridgeId. Please enter a 6-character alphanumeric bridgeId." if the 'bridgeId' or 'nodeId'
    does not meet validation criteria.
- "Internal Server Error" if the POST request returns status code 500.
- "Validation Error" if the POST request returns status code 422.
- An error message with the actual status code for any other response status code.
"""
def post(data: dict, url: str) -> bool:

    id = ""

    if url == "http://45.79.239.100:8001/bridge/add/device":
        id = data.get("bridgeId", "")
    elif url == "http://45.79.239.100:8001/user/add/node":
        id = data.get("nodeId", "")

    print(id)


    if not (id.isalnum() and len(id) == 6):
        print("Invalid bridgeId. Please enter a 6-character alphanumeric bridgeId.")
        return False

    response = requests.post(url, json=data, headers=headers)

    return validateResponseCode(response.status_code)

"""
Validates the HTTP response status code and prints corresponding messages.

Args:
- response_code (int): The HTTP response status code to be validated.

Returns:
- bool: True if the response code indicates success (201), False otherwise.

Prints:
- "Internal Server Error" if the response code is 500.
- "Validation Error" if the response code is 422.
- An error message with the actual status code for any other response status code.
"""
def validateResponseCode(response_code: int) -> bool:
    if response_code == 201:
        return True
    elif response_code == 500:
        print("Internal Server Error")
    elif response_code == 422:
        print("Validation Error")
    else:
        print(f"Unexpected error occurred: {response_code}")
    return False