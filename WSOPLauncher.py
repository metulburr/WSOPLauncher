#appname
#HKEY_CURRENT_USER > Software > Classes > Extensions > Contractld > Windows.Protocol >Packageld > {APPNAME} > ActivableClassId > CustomProperties > {name value}



import subprocess
name = 'xboxliveapp-1297292137'
start = r'C:\Windows\System32\cmd.exe /c start {}:'.format(name)
kill = r'taskkill /IM WSOP.exe /F'

subprocess.Popen(start.split())


while True:
    ans = raw_input('Press y to kill WSOP. [y/n]')
    if ans.lower() == 'y':
        print()
        subprocess.Popen(kill.split())
        break


