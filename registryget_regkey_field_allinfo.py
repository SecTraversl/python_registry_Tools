# %%
#######################################
def registryget_regkey_field_allinfo(key_object: RegistryKey):
    """For a given RegistryKey object, returns a dictionary of all fields within that RegistryKey; such that for k,v in the dictionary, k = the field name and v = all of thr info pertinent to that field name (value, raw data, value type, etc.).

    Examples:
        >>> import Registry\n
        >>> from pprint import pprint\n
        >>> reghive = Registry.Registry.Registry('SOFTWARE')\n
        >>> # Below, because our registry key's path already contains escaped '\\' backslashes we are not using a raw string ( r'' ) when we use .open()\n
        >>> regkey = reghive.open('Microsoft\\\Windows NT\\\CurrentVersion\\\Winlogon')\n
        >>> pprint( registryget_regkey_field_allinfo(regkey) )\n
        {'AutoRestartShell': OrderedDict([('value', 1),\n
                                        ('rawdata', b'\\x01\\x00\\x00\\x00'),\n
                                        ('valuetypestr', 'RegDWord'),\n
                                        ('valuetype', 4),\n
                                        ('timestamp', '')]),\n
        'Background': OrderedDict([('value', '0 0 0'),\n
                                    ('rawdata', b'0\\x00 \\x000\\x00 \\x000\\x00\\x00\\x00'),\n
                                    ('valuetypestr', 'RegSZ'),\n
                                    ('valuetype', 1),\n
                                    ('timestamp', '')]),\n
        'CachedLogonsCount': OrderedDict([('value', '10'),\n
                                        ('rawdata', b'1\\x000\\x00\\x00\\x00'),\n
                                        ('valuetypestr', 'RegSZ'),\n
                                        ('valuetype', 1),\n
                                        ('timestamp', '')]), ... }\n

    Args:
        key_object (Registry.Registry.RegistryKey): Reference and existing RegistryKey object.

    Returns:
        dict: Returns a dictionary.
    """
    from Registry.Registry import RegistryKey
    from collections import OrderedDict
#
    if isinstance(key_object, RegistryKey):
        results_dict = {}
        for eachfield in key_object.values():
            try:
                field_timestamp = str(eachfield.timestamp())
            except ValueError:
                field_timestamp = ''
            temp_ord_dict = OrderedDict({
                # 'name' : eachfield.name(), # using this as the key in the results_dict
                'value' : eachfield.value(),
                'rawdata' : eachfield.raw_data(),
                'valuetypestr' : eachfield.value_type_str(),
                'valuetype' : eachfield.value_type(),
                'timestamp' : field_timestamp
            })
            results_dict.update({eachfield.name(): temp_ord_dict})   
        return results_dict
    else:
        print("\nThe object type given to the 'key_object' parameter is not:  <class 'Registry.Registry.RegistryKey'>")
        obj_type = type(key_object)
        print(f"The object type is:  {obj_type}\n")

