# %%
#######################################
def registryget_regkey_field_values(key_object: RegistryKey):
    """For a given RegistryKey object, returns a list of field values within that key.
    
    Examples:
        >>> import Registry\n
        >>> reghive = Registry.Registry.Registry('SOFTWARE')\n
        >>> # Below, because our registry key's path already contains escaped '\\' backslashes we are not using a raw string ( r'' ) when we use .open()\n
        >>> regkey = reghive.open('Microsoft\\\Windows NT\\\CurrentVersion\\\Winlogon')\n
        >>> field_names = registryget_regkey_field_names(regkey)\n

        There are 32 fields in this registry key. The names of the fields are returned in the list below.\n

        >>> field_values = registryget_regkey_field_values(regkey)\n

        There are 32 fields in this registry key. The values of the fields are returned in the list below.\n

        >>> field_namevalue_pairs = list(zip(field_names, field_values)\n
        >>> field_namevalue_pairs\n
        [('AutoRestartShell', 1), ('Background', '0 0 0'), ('CachedLogonsCount', '10'), ('DebugServerCommand', 'no'), ('DefaultDomainName', ''), ('DefaultUserName', ''), ('DisableBackButton', 1), ('EnableSIHostIntegration', 1), ('ForceUnlockLogon', 0), ('LegalNoticeCaption', ''), ('LegalNoticeText', ''), ('PasswordExpiryWarning', 5), ('PowerdownAfterShutdown', '0'), ('PreCreateKnownFolders', '{A520A1A4-1780-4FF6-BD18-167343C5AF16}'), ('ReportBootOk', '1'), ('Shell', 'explorer.exe'), ('ShellCritical', 0), ('ShellInfrastructure', 'sihost.exe'), ('SiHostCritical', 0), ('SiHostReadyTimeOut', 0), ('SiHostRestartCountLimit', 0), ('SiHostRestartTimeGap', 0), ('VMApplet', 'SystemPropertiesPerformance.exe /pagefile'), ('WinStationsDisabled', '0'), ('ShutdownStartTime', 131119717638508921), ('UserSessionShutdownStopTime', 131117046648689456), ('ShutdownFlags', 2147483687), ('Userinit', 'C:\\Windows\\system32\\userinit.exe,'), ('scremoveoption', '0'), ('ShutdownWithoutLogon', '0'), ('DisableCad', 1), ('EnableFirstLogonAnimation', 1)]

    Args:
        key_object (Registry.Registry.RegistryKey): Reference an existing RegistryKey object.

    Returns:
        list: Returns a list of field values.
    """
    from Registry.Registry import RegistryKey
#    
    if isinstance(key_object, RegistryKey):
        field_count = key_object.values_number()
        print(f"\nThere are {field_count} fields in this registry key. The values of the fields are returned in the list below.\n")
        regkey_field_values_list = list(map(lambda x:x.value() , key_object.values()) )
        return regkey_field_values_list
    else:
        print("\nThe object type given to the 'key_object' parameter is not:  <class 'Registry.Registry.RegistryKey'>")
        obj_type = type(key_object)
        print(f"The object type is:  {obj_type}\n")

