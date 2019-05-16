This is the Final Chat System made by Jiaxin Bu and Xinran Wang.

WARNING: Please download all files in one directory (e.g.: "work_directory"), and change the current directory to this directory (i.e., "work_directory"). Then run the chat system files. Otherwise, the pygame may not work because we used os.system method, which calls for all the files in one directory to open the game window.

File introductions:

1. The PyGame-related files
bullettt.png, enemy.png, spacecraft.png: basic images for the PyGame display;
AirBattle.py: the main python file for running the game;
client_state_machine: if user types in "game", the PyGame will start on the screen.

Information referred to when developing the PyGame: https://pythonprogramming.net/pygame-python-3-part-1-intro/ (This is a basic introduction to PyGame); https://www.cnblogs.com/SRL-Southern/p/4942607.html (This code teaches how to create the classes of Bullets and Enemies).
By the way, we didn't use the sprite module built in pygame (even if it is cooler), we basically used the OOP method to draw the bullets and enemies continually on the screen.

2. The Login system
xk.png: the background image of the login window
login.py: store the login_wind function
login1.0.py: independent login system
usrinfo_pickle: store all the username and password information

Information referred to when developing the login system: https://blog.csdn.net/weixin_40450867/article/details/81431718 (This code teaches how to use tkinter to build basic login system)
We use the OOP method to draw the whole login system to ensure that every function can be called in order as we want.
We solve three main problems:
 1) The login part run before the user enter anything(username and password), which means that once we open the chat system, the window showing 'empty' message popup.
 2) The logout button didn't work as it should be. After the user click the logout button, though the login window is destroyed, the chat system continues running.



Since our codes are all written and modified by ourselves personally，we are confident of completely understanding the logics in every file :) Even though it is a rough process, we are satisfied with the fruit we earn.
