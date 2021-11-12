# %%
#######################################
def registryget_subkeys(key_object: RegistryKey):
    """For a given RegistryKey object, returns a dictionary of dictionaries where in k,v the k = the name of the Registry subkey and v = contains number of subkeys, the number of values, and the last modified timestamp.

    Examples:
        >>> from Registry.Registry import Registry\n
        >>> reghive = Registry('SOFTWARE')\n
        >>> regkey = reghive.root()\n
        >>> regkey\n
        <Registry.Registry.RegistryKey object at 0x7fe7a6c2a6a0>
        >>> pprint( registryget_subkeys( regkey ) )\n
        {'7-Zip': {'subkeys_num': 0,\n
                'timestamp': '2016-06-29 16:01:48.884266',\n
                'values_num': 2},\n
        'Apple Computer, Inc.': {'subkeys_num': 2,\n
                                'timestamp': '2016-06-17 10:51:29.912756',\n
                                'values_num': 0},\n
        'Apple Inc.': {'subkeys_num': 5,\n
                        'timestamp': '2016-06-17 10:51:30.007332',\n
                        'values_num': 0},\n
        'Classes': {'subkeys_num': 4916,\n
                    'timestamp': '2016-06-29 16:04:03.408039',\n
                    'values_num': 0}, ... }\n

    Args:
        key_object (Registry.Registry.RegistryKey): Reference and existing RegistryKey object.

    Returns:
        dict: Returns a dictionary of dictionaries.
    """
    from Registry.Registry import RegistryKey
#
    if isinstance(key_object, RegistryKey):
        results = {}
        for eachsubkey in key_object.subkeys():
            temp_dict = { 'values_num': eachsubkey.values_number(),
            'subkeys_num': eachsubkey.subkeys_number(),
            'timestamp': str(eachsubkey.timestamp()) }
            results[eachsubkey.name()] = temp_dict
        return results

