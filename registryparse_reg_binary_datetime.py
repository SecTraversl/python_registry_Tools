# %%
#######################################
def registryparse_reg_binary_datetime(bytes_string: bytes):
    """Takes a Windows Registry REG_BINARY type datetime stamp and converts it to a datetime object.

    Examples:
        >>> date_created = b'\\xe0\\x07\\x06\\x00\\x03\\x00\\x0f\\x00\\x0c\\x00\\x02\\x00%\\x00"\\x01'\n
        >>> registryparse_reg_binary_datetime( date_created )\n
        datetime.datetime(2016, 6, 15, 12, 2, 37, 290000)\n
        
        >>> str( registryparse_reg_binary_datetime( date_created ) )\n
        '2016-06-15 12:02:37.290000'

    Args:
        bytes_string (bytes): Reference a bytes string that is a REG_BINARY datetime stamp.
    """
    import struct
    import datetime
# 
    year,month,day,date,hour,minute,second,micro = struct.unpack('<8H', bytes_string)
    weekday = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    thedatetime_string = "%s, %02d/%02d/%04d %02d:%02d:%02d.%s" % (weekday[day],month,date,year,hour,minute,second,micro)
    datetime_obj = datetime.datetime.strptime(thedatetime_string, "%A, %m/%d/%Y %H:%M:%S.%f")
    return datetime_obj

