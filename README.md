# ICS Final Project Made by Jiaxin Bu and Xinran Wang

## About This Project
This is the Finalized version of ICS Chat System made by Jiaxin Bu and Xinran Wang during April ~ May, 2019.

This chat system is developed on MacOS system, so it is surely suitable for Mac devices, but has not been tested on Windows devices yet.

## How to Play with it
**WARNING**: Before any further operations, please **download all files in one directory** (e.g.: "work_directory"), and **change the current directory (cd) to this directory** (i.e., "work_directory"). Then run the chat system files. Otherwise, the pygame may not work because we used os.system method, which requires all the files in one directory so as to open the game window.

Steps to open up the whole chat system:

1. Open cmd or terminal, and use the command line of "python3 + filename" to firstly open *chat_server.py* to start up the server of chat room;

2. Then open another window of cmd or terminal, use the same command line to open *chat_cmdl_client.py* to start up the user base window. If everything goes well, you should see the login window of the chat system. Sign up/ log in on that window and then you can freely explore the functions in this chat system.

## What You Can Do Using This Program
1. **Signup or login** (see "The Login System")

2. Asking for the current time

3. Seeing who others are in the chat room

4. Connecting with peers and starting to chat (support multiple persons chatting at the same time)

5. **Searching a keyword-related chat history**

6. Playing a **Pygame of Aeroplane Battle** (see "The PyGame-related files")

7. Asking the system to give you a beautiful sonnet

8. Quit the chat system

## File Introductions
- The basic Chat System attachments

  *chat_server.py*: the server program which is used as a "central server" of the chat system;
 
  *chat_cmdl_client.py*: the user window which is connected with the server and used as a "chatting window";
 
  *chat_client_class.py*, *client_state_machine.py*, *chat_group.py*: auxiliary programs for users' chat experience.

- The PyGame-related files
 
  *bullettt.png*, *enemy.png*, *spacecraft.png*: basic images for the PyGame display;
 
  *AirBattle.py*: the main python file for running the game;
 
  *client_state_machine*: if user types in "game" in the client base window, the PyGame will appear on the screen.
 
  Information referred to when developing the PyGame: https://pythonprogramming.net/pygame-python-3-part-1-intro/ (This is a basic introduction to PyGame); https://www.cnblogs.com/SRL-Southern/p/4942607.html (This code teaches how to create the classes of Bullets and Enemies).
 
  By the way, we didn't use the Sprite module built in pygame (even if it is cooler and more fancy), we basically **used the OOP method** (which we learned on ICS class this semester) to draw the bullets and enemies continually on the screen.
 
- The Login system

  *xk.png*: the background image of the login window;
 
  *login.py*: store the login_wind (login window) function;
 
  *login1.0.py*: an independent login system;
 
  *usrinfo_pickle* (it will be automatically created after one user registered): store all the username and password information.
 
  Information referred to when developing the login system: https://blog.csdn.net/weixin_40450867/article/details/81431718 (This code teaches how to use tkinter to build basic login system) We use the OOP method to draw the whole login system to ensure that every function can be called in order as we want.

## Main Problems Encountered and Solved
1. The login part run before the user enter anything (username and password), which means that once we open the chat system, the window showing "empty" message pop up. Since we may write a simple system at first, it is important to transfer it into class and import it into chat system properly. If we just put "mainloop()" in the end, it will take running the login function for granted. So, we have to put the running command into a seperate function and call it after the window shows up and the user enter the information.

2. The logout button didn't work as it should be. After the user click the logout button, though the login window is destroyed, the chat system continues running. However, when we successfully log in and click "x" on the top corner to close the window, the whole system breaks down. So, the solution is to let login system return different messages in different states and run the logout function through the *chat_client_class.py* to ensure effective and complete quit of the chat system.

3. The pygame's quit mechanism. Since in an ios system cannot support the quit mechanism of "pygame.quit()" and "quit()", which are posted on many programming websites (that are programmed using windows), we searched online and find other quit mechanisms such as "sys.exit()" and "os._exit(0)", which can perfectly make the pygame window close and quit the whole game. But when we tried to import the game file into the chat system, all the quit mechanisms do not work and they will brutally break the whole client connection. After long time struggle, we finally figured out that **if we can use os module to exit, why not using os.system method to also open the game file?** Fortunately, it worked well. We guess it is because the os module creates a platform for only opening game file and closing game file, so that this operation will not affect the chatting function and clients can still continue chatting after closing the game; while using import (which is the improper way) means we implement the whole game program into the chat system, when we call a quit mechanism, it will surely break the whole process.

## Demonstration Video
[YouTube Link](https://youtu.be/InnpIs0lSXQ)

## Final Words & Acknoledgements
During the making of this chat system, although we viewed lots of online tutorials and instructions about pygame and login system, all our codes are written and modified by ourselves personally, so we are confident of completely understanding the logics in every file :) Even though it is a tough process, we are satisfied with the fruit we have earned. 

Special thanks to Joyce Fu and Sheldon Chen for the all supports and help when we encountered technical issues and difficulties.
