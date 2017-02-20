# Pidude
Visual status monitor for Mikrotik Dude using a Raspberry Pi and a BlinkT RBG led strip


PiDude for blinkt - works with Mikrotik "the dude" network monitor.
copy and paste save as pidude.py

vague instructions in python comments below - LOL sorry

this network status montitor pulls status from a free program from Mikrotik "The Dude" V3.6
a company that makes excellent routers with very powerfull features usually
only found in very expensive network equipment.


this is just a simple wget of the dude web pages served by the program,
then the script opens the file and counts the lines. if no devices are down
there is a certain amount of lines of html code (255),
if any device is down only one will create about 10 more lines of code.

simple if/else statements determine the output of the lights on a blinkt strip.


set a read-only user in dude that is only accessible from the ip of the raspberri pi.

change ip address and credentials in the wget.sh file included with the py script.
(i put the wget's in a shell to bash,
i'm new to python and got this method working easier than shell commands directly from py on the pi)


i plan on adding a few more inquiries to the wget.sh for monitoring in more detail,
like ping with 32 and 1500 bytes, high latency, separate monitoring for backhaul links,
line power status, battery voltage, and other SNMP values.
which can be done by getting a url from your browser on what you want to monitor.


DISCLAIMER------WARNING!!!!! --
I would also recommend setting up a tmpfs ramdrive on the pi
to avoid the constant writes and reads to the memory card=
here is a link with perfectly good instructions for setting up a persistent ramdisk, thought the persistent part isn't needed.
http://www.observium.org/docs/persistent_ramdisk/

check here to get the Blinkt strip installed and functional and test with example scripts
https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt

SET - "time.sleep(300)" to the amount of time you want between updates. KEEP THIS HIGH IF YOU ARE NOT USING ABOVE RAMDRIVE

if the wget.sh file doesn't get in with the py file, here it is below,

the first wget is to get a cookie, the second I am not sure will work with your installation of the dude.
if not go to the devices, and select down for status, copy and paste that url into the code between the quotes

to run at startup edit crontab with  "crontab -e" and enter follow line at the end
@reboot python /home/pi/Pimoroni/blinkt/examples/pidude2.py &

you will need to add a new user to dude, set that user to "read-only" and only accessible from the IP address of the pi

tested and working on Pi3 and Pi zero.


