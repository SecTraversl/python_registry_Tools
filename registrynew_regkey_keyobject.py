# %%
#######################################
def registrynew_regkey_keyobject(key_path: str, hive_object: Registry):
    """For a given key path string, and Registry class hive object, returns a RegistryKey object.

    Examples:
        >>> regkey = registrynew_regkey_keyobject( '7-zip', reghive )\n
        >>> regkey\n
        <Registry.Registry.RegistryKey object at 0x7fe7a6c38af0>
        >>> regkey.values()\n
        [<Registry.Registry.RegistryValue object at 0x7fe7a6c2a610>, <Registry.Registry.RegistryValue object at 0x7fe7a6c2adf0>]

    Args:
        key_path (str): Reference an existing registry path and key name.
        hive_object (Registry.Registry.Registry): Reference a Registery class hive object.

    Returns:
        Registry.Registry.RegistryKey: Returns a RegistryKey object.
    """
    from Registry.Registry import Registry
#
    if isinstance(hive_object, Registry):
        regkey = hive_object.open(rf"{key_path}")
        return regkey

