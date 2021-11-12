# %%
#######################################
def registryget_regkey_field_names(key_object: RegistryKey):
    """For a given RegistryKey object, returns a list of field names within that key.

    Examples:
        >>> import Registry\n
        >>> reghive = Registry.Registry.Registry('SOFTWARE')\n
        >>> # Below, because our registry key's path already contains escaped '\\' backslashes we are not using a raw string ( r'' ) when we use .open()\n
        >>> regkey = reghive.open('Microsoft\\\Windows NT\\\CurrentVersion\\\Winlogon')\n
        >>> registryget_regkey_field_names(regkey)\n

        There are 32 fields in this registry key. The names of the fields are returned in the list below.\n

        ['AutoRestartShell', 'Background', 'CachedLogonsCount', 'DebugServerCommand', 'DefaultDomainName', 'DefaultUserName', 'DisableBackButton', 'EnableSIHostIntegration', 'ForceUnlockLogon', 'LegalNoticeCaption', 'LegalNoticeText', 'PasswordExpiryWarning', 'PowerdownAfterShutdown', 'PreCreateKnownFolders', 'ReportBootOk', 'Shell', 'ShellCritical', 'ShellInfrastructure', 'SiHostCritical', 'SiHostReadyTimeOut', 'SiHostRestartCountLimit', 'SiHostRestartTimeGap', 'VMApplet', 'WinStationsDisabled', 'ShutdownStartTime', 'UserSessionShutdownStopTime', 'ShutdownFlags', 'Userinit', 'scremoveoption', 'ShutdownWithoutLogon', 'DisableCad', 'EnableFirstLogonAnimation']

        >>> registryget_regkey_field_names(reghive)\n

        The object type given to the 'key_object' parameter is not:  <class 'Registry.Registry.RegistryKey'>\n
        The object type is:  <class 'Registry.Registry.Registry'>\n

    Args:
        key_object (Registry.Registry.RegistryKey): Reference an existing RegistryKey object.

    Returns:
        list: Returns a list of field names.
    """
    from Registry.Registry import RegistryKey
#    
    if isinstance(key_object, RegistryKey):
        field_count = key_object.values_number()
        print(f"\nThere are {field_count} fields in this registry key. The names of the fields are returned in the list below.\n")
        regkey_field_names_list = list(map(lambda x:x.name() , key_object.values()) )
        return regkey_field_names_list
    else:
        print("\nThe object type given to the 'key_object' parameter is not:  <class 'Registry.Registry.RegistryKey'>")
        obj_type = type(key_object)
        print(f"The object type is:  {obj_type}\n")

