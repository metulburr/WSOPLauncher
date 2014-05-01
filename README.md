[![Logo](http://i.imgur.com/iA5nuPy.jpg)](http://i.imgur.com)
[![Logo](http://i.imgur.com/7u7stuq.png)](http://i.imgur.com/7u7stuq.png)

WSOPLauncher
============
Since windows 8 will not allow you to run windows 8 store games from within Steam. 
This launcher runs WSOP FUll House Pro and kills it upon console quit. 
Currenlty this code only launches WSOP from windows 8 store. 
However the appname can be changed to launch other programs from the windows 8 store theoretically (although untested). 

###How to
link dist/WSOPLauncher.exe in steam and run game from steam's game list, close out of console to kill the game

In Steam go to Games > Add Non-Steam Game to My Library > Browse > navigate to dist/WSOPLauncher.exe > Add selected Programs

###Problems
Currently the program seeks out the WSOP appname from registry keys assuming the game is installed. 
If this fails the launcher will fail too. 
You can override the registry keys by searching out the appname yourself and changing it in code to the appname. 
Uncomment the line in WSOPLauncher.py

    #name = 'xboxliveapp-1297292137'
and change the string to the appname. The appname can be found in registry path (open regedit)

    HKEY_CURRENT_USER > Software > Classes > Extensions > Contractld > Windows.Protocol >Packageld > {APPNAME} > ActivableClassId > CustomProperties > {name's value}
Delete build and dist directories and recompile the exe with python using the setup.py file (requires py2exe), and start the game from within steam. 
If you still have problems please make an issue for the repo. 
