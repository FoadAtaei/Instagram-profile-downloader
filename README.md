Instagram profile downloader
In this project, I plan to use two application packages tkinter and instaloader in the Python programming language to view and download the profile picture of each Instagram account.
I have written the detailed description of the project for you in the commits, but if I want to tell you how this program works in general, it is that we use tkinter to create a very simple and basic graphic environment for our program, which includes a box. It is to get a username and a button that will be displayed for you as soon as you select that profile picture.
This command is via a function that I named get_image. In this function, by taking the username of each account, we first receive the url of profile picture and through the io package, we receive the image from this link and display it to the user.
Trick: If you want this program to be more practical and cool, we can make the output of this program in the form of an executable file using the pyinstaller package.
If you want to do this, first install the pyinstaller package and then enter the following code in the terminal:
pyinstaller --onefile -w (name of your project)
Another cool trick: Create an installation file of your project by installing NSIS, It makes you feel good :)
Change and expand the program in any way you like. Share with me the bugs of the program or ways to improve it and anything else through social media.
FoadAtaei
