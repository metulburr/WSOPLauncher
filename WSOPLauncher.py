
#appname
#HKEY_CURRENT_USER > Software > Classes > Extensions > Contractld > Windows.Protocol >Packageld > ActivableClassId > {APPNAME} > CustomProperties > {name value}



import ctypes
import subprocess
import sys
import os

if sys.version[0] == '2':
    input = raw_input
    import _winreg as wreg
else:
    import winreg as wreg


def as_string(lister):
    return r'\\'.join(lister)
    
def get_key(path):
    return wreg.OpenKey(wreg.HKEY_CURRENT_USER, as_string(path), 0, wreg.KEY_ALL_ACCESS)
    
def search_for_subkey(path, search):
    key = get_key(path)
    try:
        i = 0;
        while True:
            subkey = wreg.EnumKey(key, i)
            if search in subkey:
                return subkey
            i += 1
    except WindowsError:
        pass
        
def regkey_value(path, name="", start_key = None):
    if isinstance(path, str):
        path = path.split("\\")
    if start_key is None:
        start_key = getattr(wreg, path[0])
        return regkey_value(path[1:], name, start_key)
    else:
        subkey = path.pop(0)
    with wreg.OpenKey(start_key, subkey) as handle:
        assert handle
        if path:
            return regkey_value(path, name, handle)
        else:
            desc, i = None, 0
            while not desc or desc[0] != name:
                desc = wreg.EnumValue(handle, i)
                i += 1
            return desc[1]


path = ['Software', 'Classes', 'Extensions', 'ContractId', 'Windows.Protocol', 'PackageId']
subkey1 = search_for_subkey(path, 'WSOPFullHousePro')
path.append(subkey1)
path.append('ActivatableClassId')
subkey2 = search_for_subkey(path, 'App.App')
path.append(subkey2)
path.append('CustomProperties')

name = regkey_value(as_string(['HKEY_CURRENT_USER'] + path), "Name")



#name = 'xboxliveapp-1297292137'
start = r'C:\Windows\System32\cmd.exe /c start {}:'.format(name)
kill = r'taskkill /IM WSOP.exe /F'

subprocess.Popen(start.split())


while True:
    ans = raw_input('Press y to kill WSOP. [y/n]')
    if ans.lower() == 'y':
        print()
        subprocess.Popen(kill.split())
        break


