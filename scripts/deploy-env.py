from key_gen import generate_random_string, generate_sha256_hash
Import("env")

##Replace network credentials with appropriate values depending on your LAN
ipv4="192.168.1.90"
sn="255.255.255.0"
gw="192.168.1.1"
dns="8.8.8.8"

env.Append(CPPDEFINES=[
    ("OTA_ENABLED", 1), ##enable OTA
    ("IPV4_ADDRESS", env.StringifyMacro(ipv4)),
    ("SN_ADDRESS", env.StringifyMacro(sn)),
    ("GW_ADDRESS", env.StringifyMacro(gw)),
    ("DNS_ADDRESS", env.StringifyMacro(dns))
])
