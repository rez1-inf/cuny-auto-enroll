# What is it??

This **python** script will automatically enroll you to any course saved in your shopping cart in CUNYFirst.
It uses image recognition to identify and click in your browser. And it will check if any course opens up every 5 min and then it will automatically enroll you in those courses.
It stops after enrolling **at least one** course.
This way you can sleep, go out, or do whatever you want and not have to constantly check if a class opens up for you to register.


***Update 2***: It finally works in MacOS :)... `PyAutoGUI` is still broken for MacOS but I found a workaround

***Update 1***: ~~MacOS has issues with `PyAutoGUI`. It can locate areas on a screen but the cordinates are off by a factor of 2. It's an issue that the developers haven't fixed yet, so unfortunately it will not work on MacOS. I will update as soon as I find a fix.~~ [You can follow the issue here](https://github.com/asweigart/pyautogui/issues/589#issue-924442603)

***Note***: I did not test this on Windows yet, but I assume it should work fine on Windows.


## Initial Setup Requirements:

**Step 0:**
Make sure the latest python is installed in your computer.

**Step 1:**
Make sure these python packages are installed:

 1. Windows: run in command prompt `pip install pyautogui pillow`
 2. MAC: run in terminal `pip3 install pyobjc-framework-Quartz pyobjc-core pyobjc pyautogui pillow`
 3. Linux: run in terminal `pip3 install python3-xlib pyautogui pillow`
 
 Linux needs additional dependencies: `sudo apt install scrot python3-tk python3-dev`

**Step 2:**
Clone this repository in you computer. Type in terminal:

`git clone https://github.com/rez1-inf/cuny-auto-enroll.git`

**Step 3:**
Login into your CUNYFirst and put some classes in your shopping cart.

**Step 4:**
Run the script (see below how to run). It will check your screen resolution and create a folder inside the samples directory where you can provide your screenshots (explained below). I already provided samples for MacBook 13 inch in the `Samples/1440x900/` directory, so most likely the fonts and stuff will match (for Safari browser) and you can just run this script and have it do its thing, otherwise you will need to take the screenshots.

*Note*: If any sample at some point does not match, the script will tell you which one to update

**Step 5:**
When it reaches the term selection page, check the terminal, it will ask for your input to select which term you want to enroll in. Type in the number corrosponding to the term and press `return`/`enter`... and from then on it will keep trying automatically.

## Screen Shot Samples:
You need to provide some screenshots of specific areas of the CUNYFirst interface in order for the script to know where it should click. Since every display has different screen resolutions, you will need to provide screenshot samples from the computer you will run this on for it to work.

Goto CUNYFirst website and take screenshots of the **red boxes** displayed below, and store them inside the **Samples** directory and name them as `01.png, 02.png ...` or `01.jpg, 02.jpg...` as listed below. Note: png is better since it's lossless, hence it contains accurate color code for each pixel. It might work with jpg, I'm not sure, I didnt test with jpg.

For reference, view the ones I used in my computer inside the samples directory. You can try to see if my samples work for you, but most likely you will need to provide your own. If you do provide your own, make sure to remove/replace mine. Since, there cannot be more or less than 11 sample files inside that directory.

***Note***: ~~MAC creates hidden files when you add/modify something in a directory. Make sure to remove the hidden `.DS_Store` file from Samples directory.~~ The script will automatically delete it

![No.1](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/1.png)
![No.2](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/2.png)
![No.3](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/3.png)
![No.4](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/4.png)
![No.5](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/5.png)
![No.6](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/6.png)
![No.7](https://github.com/rez1-inf/cuny-auto-enroll/blob/main/Required%20Screen%20Shots/7.png)

## To run the script

 1. Open your terminal, then `cd` into the directory this python script is located.
 2. Open CUNYFirst in a browser and login.
 3. Run the script `python autoEnroll.py` OR `python3 autoEnroll.py`

Everytime you run this script, after it reaches the term selection page in CUNYFirst, go back to the terminal and select which term you want to try enrolling to. After that, it will remember the term selection and keep trying until at least one class is succesfully enrolled.

*Note*: This script assumes your browser automatically fills in login information for CUNYFirst. Otherwise just start the script after logging in CUNYFirst, but it may stop if working if for some reason you get logged out.

## Manually stop the script
Open your terminal, press `ctrl` and `c` simultaniously, to terminate.

***Important***: Make sure not to minimize or cover the CUNYFirst interface from your screen, if the script cannot see CUNYFirst, it will stop running soon. You can make the window smaller, but make sure all the buttons and stuff are visible so the script can do its job.

Please let me know if you face any issues. I'll try my best to fix them.
