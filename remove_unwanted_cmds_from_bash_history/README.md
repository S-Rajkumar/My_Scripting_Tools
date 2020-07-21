# Remove unwanted commands from `.bash_history`

**Purpose of This Tool**

>In Linux our commands are stored in .bash_history as history for our recall but it stored all of our commands like `cd`, `ls`,
>`mkdir`, `mv`, `rm` and etc... these commands are junks for mine so i want to remove these commands (junks) from .bash_history.
>First i do it in manually but it needs more time and i thought i am wasting my time so i created a script to remove those junks 
>data from `.bash_history` file. I put it on my `.bashrc` file ( end of `.bashrc` file `python3 /opt/clear_junk_history.py` ),
>so when ever i open the Terminal this script run to remove the junk history from .bash_history file

>This tools save time and reduced size of `.bash_history` file

>you can also edit [this](https://raw.githubusercontent.com/S-Rajkumar/My_Scripting_Tools/master/remove_unwanted_cmds_from_bash_history/clear_junk_history.py) script for your convinent to remove junk history
