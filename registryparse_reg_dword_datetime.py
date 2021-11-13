# %%
#######################################
def registryparse_reg_dword_datetime(datetime_int: int):
    """Takes the integer value from a REG_DWORD type datetime stamp from the Windows Registry and converts it to a datetime object.

    Examples:
        >>> from Registry.Registry import Registry\n
        >>> reghive = Registry('SOFTWARE')\n
        >>> key_path_raw = r'Microsoft\Windows NT\CurrentVersion'\n
        >>> regkey = reghive.open(key_path_raw)\n

        >>> install_date_entry = [x for x in regkey.values() if x.name() == 'InstallDate']\n
        >>> install_date_entry\n
        [RegistryValue(name="InstallDate", value="1458039846", type="RegDWord")]

        >>> install_date_entry[0].value()\n
        1458039846

        >>> registryparse_reg_dword_datetime( 1458039846 )\n
        datetime.datetime(2016, 3, 15, 4, 4, 6)\n
        >>> str( registryparse_reg_dword_datetime( 1458039846 ) )\n
        '2016-03-15 04:04:06'

    Args:
        datetime_int (int): Reference a valid datetime stamp from a REG_DWORD type.

    Returns:
        datetime.datetime: returns a datetime object.
    """
    import datetime
    datetime_obj = datetime.datetime.fromtimestamp(datetime_int)
    return datetime_obj

