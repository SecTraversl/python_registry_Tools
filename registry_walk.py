# %%
#######################################
def registry_walk(hive_object: object, key_path_raw: str):
    """Creates a generator that returns the current registry key's path, along with its subkeys and values.  Each call to next() returns the next nested set of information as you "walk" through the nested layers of the given registry hive starting at the given key path.

    Example:
        >>> ##### EXAMPLE 1 ######
        >>> from Registry.Registry import Registry\n
        >>> from Registry.Registry import RegistryKey\n
        >>> reghive = Registry('SOFTWARE')\n
        >>> some_key_path = r'Microsoft\Windows NT\CurrentVersion\Winlogon'\n
        >>> test = registry_walk(reghive, some_key_path)\n

        >>> next(test)\n
        ('ROOT\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon', [RegistryKey(name="AlternateShells", path="ROOT\Microsoft\Windows NT\CurrentVersion\Winlogon\AlternateShells"), RegistryKey(name="GPExtensions", path="ROOT\Microsoft\Windows NT\CurrentVersion\Winlogon\GPExtensions")], [RegistryValue(name="AutoRestartShell", value="1", type="RegDWord"), RegistryValue(name="Background", value="0 0 0", type="RegSZ"), RegistryValue(name="CachedLogonsCount", value="10", type="RegSZ"), RegistryValue(name="DebugServerCommand", value="no", type="RegSZ"), RegistryValue(name="DefaultDomainName", value="", type="RegSZ"), RegistryValue(name="DefaultUserName", value="", type="RegSZ"), ... ])\n

        >>> next(test)\n
        ('ROOT\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\AlternateShells', [], [])\n

        >>> ##### EXAMPLE 2 ######\n
        >>> newtest = registry_walk(reghive, '7-Zip')\n
        >>> next(newtest)\n
        ('ROOT\\7-Zip', [], [RegistryValue(name="Path64", value="C:\Program Files\7-Zip\", type="RegSZ"), RegistryValue(name="Path", value="C:\Program Files\7-Zip\", type="RegSZ")])\n
        >>> next(newtest)\n
        Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        StopIteration

    Args:
        hive_object (Registry.Registry.Registry): Reference an existing Registry hive object.
        key_path_raw (str): Reference a valid key path.

    Yields:
        tuple: Yields a tuple.
    """
    regkey = hive_object.open(rf'{key_path_raw}')
    yield regkey.path(), regkey.subkeys(), regkey.values()
    for subkey in regkey.subkeys():
        for currentkeypath, currentsubkeys, currentvalues in registry_walk(hive_object, subkey.path()[5:]):
            yield currentkeypath, currentsubkeys, currentvalues

