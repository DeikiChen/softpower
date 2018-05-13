
Step 1) Check if root--------------------------------------
if [[ $EUID -ne 0 ]]; then
   echo "Please execute script as root."
   exit 1
fi

#Step 2) Remove Python script-----------------------------
echo "Remove Python script...Done!"
cd /home/pi
sudo rm -rf SuperNESPi


#Step 2) Remove Autostart script-----------------------------
echo "Remove Autostart script...Done!"
cd /home/pi/.config/autostart
sudo rm -f softshutdown.desktop

#-------------------------------------------------------------
#Step 3) Reboot to apply changes----------------------------
echo "SuperNESPi Case uninstallation done. Will now reboot after 3 seconds."
sleep 3
sudo reboot
#-----------------------------------------------------------


