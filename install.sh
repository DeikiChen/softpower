
Step 1) Check if root--------------------------------------
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root."
   exit 1
fi

#Step 2) Download Python script-----------------------------
cd /home/pi
sudo mkdir SuperNESPi
cd SuperNESPi

script=softshutdown.py

if [ -e $script ];
	then
		echo "Script softshutdown.py already exists. Doing nothing."
	else
		wget "https://raw.githubusercontent.com/DeikiChen/softpower/master/softshutdown.py"
fi

#

#Step 4) Set sutostart ---------------------------
cd ..
cd .config
sudo mkdir autostart
cd autostart
script=softshutdown.desktop

if [ -e $script ];
	then
		echo "Script softshutdown.desktop already exists. Doing nothing."
	else
		wget "https://raw.githubusercontent.com/DeikiChen/softpower/master/softshutdown.desktop"
fi
#-------------------------------------------------------------
#Step 5) Reboot to apply changes----------------------------
echo "SuperNESPi Case installation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------


