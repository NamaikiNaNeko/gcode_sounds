# gcode_sounds
gcode_sounds is a collection of voice notifications for your printer. Provided .wav and .mp3 format files include 37 different voice notifications of varying usefulness depending on your setup. You will need to pick and choose which sounds you want, or you are always free to change, add, or remove whatever you want to suit your needs. For a printer running klipper, a configuration file and file generator is provided to automatically populate gcode macros in the gcode_sounds.cfg file.
Hopefully you will find this as helpful as I have if your printer is in another room and it takes a while before you notice the absence of stepper motor sounds during a filament runout.
Demonstration (unmute video to hear sound):

https://github.com/NamaikiNaNeko/gcode_sounds/assets/16394540/d6f92f35-99d0-4ed8-85a8-8bbbbb04e2e7



# Hardware
To play audio files, you will need an a device with an audio output (3.5mm audio jack, HDMI, etc.), an amplifier, and speakers. If your printer already has a 5V power supply, a handy little 10W amplifier such as what's linked below would be a perfect addition, and is what I used on my printers. There's also an amp bracket .stl provided for this particular amp in the repository. 
![el cheapo audio amp](https://m.media-amazon.com/images/I/71c2h8H69YL._AC_SX679_.jpg)
I used some cheap sealed speakers but they sound pretty bad; they work alright for voice but music is right out. Look around for something else if you want high fidelity audio, but remember it's just a printer.
If you're adding an amp to your 5V supply, make sure your it provides enough power. You don't want to accidentally brownout your pi in the middle of a print because you a 10W amp to your system on top of your pi, fans, LED strips, or whatever else you have on 5V.
Links:
https://www.amazon.com/dp/B08RDN58SZ
https://www.amazon.com/dp/B0BHST51PQ


# Setup
1. You need to be able to play sounds from the command line. Install aplay and mpg321 on the device running klipper.
2. Add gcode shell command capability by running KIAUH and installing G-Code Shell Command under Advanced.
3. Create a new directory on your klipper device /pi/home/gcode_sounds and copy the contents of the wav directory there.
4. Copy over gcode_sounds.cfg to your printer's configuration directory.
5. Add [gcode_sounds.cfg] to your printer.cfg file.
6. Add the appropriate __gs_play_* macros to your printer's config file where appropriate. An example would be configuring a filament runout sensor with:

		[filament_switch_sensor my_sensor]
		pause_on_runout: True
		runout_gcode: _gs_play_filament_runout_detected
		switch_pin: !P1.24
	You can also add in a delayed gcode macro to let you know when startup is complete:

		[delayed_gcode welcome]
		initial_duration: 5.
		gcode: _gs_play_printer_ready
	
	
# Licenses:
Audio files were recorded by Olivia Warren and are licensed under [Creative Commons Attribution-NonCommercial 4.0 International Public License](https://creativecommons.org/licenses/by-nc/4.0/legalcode) 
The rest of the project (.stl, .cfg, .cfg generator) are all released under [WTFPL – Do What the Fuck You Want to Public License](http://www.wtfpl.net/)
