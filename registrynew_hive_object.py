# %%
#######################################
def registrynew_hive_object(hive_file: str):
    """Returns a Registry class object handle for the referenced hive file.

    Examples:
        >>> reghive = registrynew_hive_object('SOFTWARE')\n
        >>> reghive\n
        <Registry.Registry.Registry object at 0x7f57e804acd0>    
        >>> reghive.hive_name()\n
        'emRoot\\System32\\Config\\SOFTWARE'
        >>> reghive.hive_type()\n
        <HiveType.SOFTWARE: 'software'>
        >>> reghive.root()\n
        <Registry.Registry.RegistryKey object at 0x7f57b665a070>

    Args:
        hive_file (str): Reference the path/name of a given registry hive file.

    Returns:
        Registry.Registry.Registry: Returns a Registry class object.
    """
    from Registry.Registry import Registry
#
    reghive = Registry(hive_file)
    return reghive

