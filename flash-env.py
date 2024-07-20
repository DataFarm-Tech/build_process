import requests
from lib.key_gen import generate_random_string, generate_sha256_hash
from lib.post import post
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

isValid = False

while isValid == False:
    print("Enter the bridgeId:")
    bridgeId = input()

    ##Generate random string to then generate a sha256 hash
    random_string = generate_random_string(16)
    api_key = generate_sha256_hash(random_string)

    ##dict to hold bridgeId and apiKey
    data = {
        "bridgeId": bridgeId,
        "apiKey": api_key
    }

    isValid = post(data=data, url="http://45.79.239.100:8001/bridge/add/device")


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
