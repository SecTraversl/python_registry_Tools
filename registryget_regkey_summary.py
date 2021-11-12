# %%
#######################################
def registryget_regkey_summary(key_object: RegistryKey):
    from Registry.Registry import RegistryKey
#
    if isinstance(key_object, RegistryKey):
        results = {}
        results['values_num'] = key_object.values_number()
        results['subkeys_num'] = key_object.subkeys_number()
        return results

