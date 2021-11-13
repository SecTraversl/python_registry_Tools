# %%
#######################################
def registryparse_network_conn_unmanaged(software_hive_file: str, output_dataframe=True):
    from Registry.Registry import Registry
    import codecs
    import pandas
#
    reghive = Registry(software_hive_file)
    regkey = reghive.open(r'Microsoft\Windows NT\CurrentVersion\NetworkList\Signatures\Unmanaged')
    # network_connection_info = list(map(lambda x:x.values(), regkey.subkeys()))
    subkeys_list = regkey.subkeys()
#
    results_list = []
    for eachsubkey in subkeys_list:
        profile_guid = eachsubkey.value('ProfileGuid').value()
        description = eachsubkey.value('Description').value()
        dns_suffix = eachsubkey.value('DnsSuffix').value()
        network_name_or_ssid = eachsubkey.value('FirstNetwork').value()
#
        # Formatting the MAC Address
        default_gateway_mac = eachsubkey.value('DefaultGatewayMac').value()
        default_gateway_mac = codecs.encode(default_gateway_mac, 'hex').decode()
        default_gateway_mac_or_bssid = ':'.join([default_gateway_mac[i:i+2] for i in range(0, len(default_gateway_mac), 2)])
        network_type, first_connected, last_connected = registryparse_network_profile_type(reghive, profile_guid)
#
        results_list.append( (network_type, network_name_or_ssid, description, dns_suffix, default_gateway_mac_or_bssid, first_connected, last_connected) )
#
    if output_dataframe:
        column_headers = ['network_type', 'name_or_ssid', 'description', 'dns_suffix', 'gateway_or_bssid', 'first_connected', 'last_connected' ]
        results_df = pandas.DataFrame(results_list, columns=column_headers)
        return results_df
    else:
        return results_list

