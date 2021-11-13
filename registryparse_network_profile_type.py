# %%
#######################################
def registryparse_network_profile_type(hive_object: object, profile_guid: str):
    key_path_raw = r"Microsoft\Windows NT\CurrentVersion\NetworkList\Profiles\{}".format(profile_guid)
    regkey = hive_object.open(key_path_raw)
#
    # We look up the value of the "NameType" field, and convert that int value with .format() to be shown as the equivalent value in hexadecimal using string characters
    nametype_value_as_hex_str = "{:02x}".format( regkey.value('NameType').value() )
    network_nametypes = {"06": "Wired", "17": "Broadband", "47": "Wireless"}
    network_type = network_nametypes.get(nametype_value_as_hex_str, "Unknown network type: " + nametype_value_as_hex_str)
#
    first_connected = registryparse_reg_binary_datetime( regkey.value('DateCreated').value() )
    first_connected = str( first_connected )
    last_connected = registryparse_reg_binary_datetime( regkey.value('DateLastConnected').value() )
    last_connected = str( last_connected )
    return network_type, first_connected, last_connected

