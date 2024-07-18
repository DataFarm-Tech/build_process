import requests
from key_gen import generate_random_string, generate_sha256_hash

##URL that Host Computer uses (The computer that flashes the firmware to the device)
url = "http://45.79.239.100:8001/bridge/add/device"
ipv4="192.168.1.90"
sn="255.255.255.0"
gw="192.168.1.1"
dns="8.8.8.8"
##data stored in the header of the request
headers = {
    "Content-Type": "application/json"
}

print("Starting flash-env.py script") # debug purposes

isValid = False

while isValid == False:
    print("Enter the bridgeId:")
    ##Get input from stdin (The worker that is flashing firmware on devices)
    bridgeId = input()

    ##Generate random string to then generate a sha256 hash
    random_string = generate_random_string(16)
    api_key = generate_sha256_hash(random_string)

    ##dict to hold bridgeId and apiKey
    data = {
        "bridgeId": bridgeId,
        "apiKey": api_key
    }

    ##Executes the API Post Request
    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 201:
        print("Internal Server Error")

    if bridgeId.isalnum() and len(bridgeId) == 6 and response.status_code == 201:
        isValid = True
    else:
        print("Invalid bridgeId. Please enter a 6-character alphanumeric bridgeId.")


# Define NODE_ID and API_KEY macro for PlatformIO
Import("env")
env.Append(CPPDEFINES=[
    ("BRIDGE_ID", env.StringifyMacro(bridgeId)),
    ("OTA_ENABLED", 1), ##OTA_ENABLED is set to true
    ("API_KEY", env.StringifyMacro(api_key)),
     ("IPV4_ADDRESS", env.StringifyMacro(ipv4)),
    ("SN_ADDRESS", env.StringifyMacro(sn)),
    ("GW_ADDRESS", env.StringifyMacro(gw)),
    ("DNS_ADDRESS", env.StringifyMacro(dns))
])
