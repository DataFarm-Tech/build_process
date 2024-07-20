from build_process.lib.key_gen import generate_random_string, generate_sha256_hash
Import("env")

bridgeId="branch"
ipv4="192.168.1.90"
sn="255.255.255.0"
gw="192.168.1.1"
dns="8.8.8.8"

random_string = generate_random_string(16)
api_key = generate_sha256_hash(random_string)


env.Append(CPPDEFINES=[
    ("OTA_ENABLED", 0),
    ("IPV4_ADDRESS", env.StringifyMacro(ipv4)),
    ("SN_ADDRESS", env.StringifyMacro(sn)),
    ("GW_ADDRESS", env.StringifyMacro(gw)),
    ("DNS_ADDRESS", env.StringifyMacro(dns)),
    ("BRIDGE_ID", env.StringifyMacro(bridgeId)),
    ("API_KEY", env.StringifyMacro(api_key))
])
