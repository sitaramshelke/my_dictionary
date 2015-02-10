# my_dictionary
This is "Word a Day" program as a desktop application which runs on startup with a simple window and greets you as well.

In order to run it on startup you need follow a simple step

1.]Create file ~/.config/autostart/MyScript.desktop with

[Desktop Entry]
Encoding=UTF-8
Name=MyScript
Comment=MyScript
Icon=gnome-info
Exec=python /home/your_path/script.py
Terminal=false
Type=Application
Categories=

X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=0


and save it.
2.]That's it just restart your machine :)
