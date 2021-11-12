# %%
#######################################
def registryget_values(key_object: RegistryKey):
    """For a given RegistryKey object returns the values (if any are present) for that RegistryKey.

    Examples:
        >>> from Registry.Registry import Registry\n
        >>> reghive = Registry('SOFTWARE')\n
        >>> regkey = reghive.open(r'Microsoft\Windows NT\CurrentVersion\Winlogon')\n
        >>> pprint( registryget_values( regkey ) )\n
        [('RegDWord', 'AutoRestartShell', 1),\n
        ('RegSZ', 'Background', '0 0 0'),\n
        ('RegSZ', 'CachedLogonsCount', '10'),\n
        ('RegSZ', 'DebugServerCommand', 'no'),\n
        ('RegSZ', 'DefaultDomainName', ''),\n
        ('RegSZ', 'DefaultUserName', ''),\n
        ('RegDWord', 'DisableBackButton', 1),\n
        ('RegDWord', 'EnableSIHostIntegration', 1),\n
        ('RegDWord', 'ForceUnlockLogon', 0), ...]\n

    Args:
        key_object (Registry.Registry.RegistryKey): Reference an existing RegistryKey object.

    Returns:
        list: Returns a list of tuples.
    """
    from Registry.Registry import RegistryKey
#
    if isinstance(key_object, RegistryKey):
        results = []
        for eachvalue in key_object.values():
            results.append( ( eachvalue.value_type_str(), eachvalue.name(), eachvalue.value()) )
        return results

