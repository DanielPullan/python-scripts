## Post Install Script
## A script to use on Fedora immediately post install.
## Dan Pullan (https://danielpullan.co.uk) 07/06/24

import subprocess
import urllib.request
import os


homepath= os.path.expanduser('~')

confirm_list = ['Yes', 'yes', 'Y', 'y', 'Yarp', 'yarp']
deny_list = ['No', 'no', 'N', 'n', 'Narp', 'narp']
known_devices = ["zig", "zag"]

def name_device(name):
    subprocess.run(["hostnamectl", "set-hostname", name])
    print("Name set to: ", name)
    
def enable_ssh():
    subprocess.run(["sudo", "dnf", "install", "openssh-server", "-y"])
    subprocess.run(["systemctl", "enable", "sshd"])
    subprocess.run(["systemctl", "start", "sshd"])
    print("SSH access enabled.")

def install_updates():
    subprocess.run(["sudo", "dnf", "update", "-y"])
    print("Updates completed.")

def install_cockpit():
    subprocess.run(["sudo", "dnf", "install", "cockpit", "-y"])
    subprocess.run(["systemctl", "enable", "--now", "cockpit.socket"])
    subprocess.run(["firewall-cmd", "--add-service=cockpit"])
    subprocess.run(["firewall-cmd", "--add-service=cockpit", "--permanent"])
    print("Cockpit installed and enabled.")

def install_tailscale():
    subprocess.run(["sudo", "dnf", "config-manager", "--add-repo", "https://pkgs.tailscale.com/stable/fedora/tailscale.repo"])
    subprocess.run(["sudo", "dnf", "install", "tailscale", "-y"])
    subprocess.run(["systemctl", "enable", "--now", "tailscaled"])
    print("Tailscale installed and enabled.")

def dark_mode():
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "color-scheme", "'prefer-dark'"])
    print("Dark mode set.")

def install_xrdp():
    subprocess.run(["dnf", "install", "xrdp", "-y"])
    subprocess.run(["systemctl", "enable", "xrdp"])
    subprocess.run(["systemctl", "start", "xrdp"])
    print("XRDP installed and enabled.")

def download_wallpaper(device_name):
    url = 'https://3264.uk/images/'+device_name+".jpg"
    save_as = homepath+"/Pictures/wallpapertest.jpg"
    urllib.request.urlretrieve(url, save_as)
    subprocess.run(["gsettings","set", "org.gnome.desktop.background", "picture-uri", save_as])
    subprocess.run(["gsettings","set", "org.gnome.desktop.background", "picture-uri-dark", save_as])
    print("Wallpaper set.")

device_name = input("What would you like to call this device? ")

name_device(device_name)

print("Hostname set to: ", device_name)

if device_name in known_devices:
    download_wallpaper(device_name)
    print("Known wallpaper downloaded.")
else:  
    download_wallpaper("tech")
    print("Unknown wallpaper downloaded.")

enable_ssh()

install_updates()

program_installs = input("Would you like to install Cockpit, Tailscale and XRDP? ")

if program_installs in confirm_list:
    install_cockpit()
    install_tailscale()
    install_xrdp()
    print("Installed Cockpit, Tailscale and XRDP")
elif program_installs in deny_list:
    confirmation = input("Would you like to install Cockpit or Tailscale? 1 - Cockpit, 2 - Tailscale, 3 - XRDP ")
    if confirmation in deny_list:
        print("Skipping installs")
    elif confirmation == 1:
        install_cockpit()
        print("Installed cockpit.")
    elif confirmation == 2:
        install_tailscale()
        print("Installed tailscale")
    elif confirmation == 3:
        install_xrdp()
        print("Installed XRDP")
    else:  
        print("I don't understand. If you would like to install Cockpit, Tailscale or XRDP, please install manually.")
else:  
        print("I don't understand. If you would like to install Cockpit, Tailscale or XRDP, please install manually.")

dark_mode_request = input("is this device going to use a GUI? ")

if dark_mode_request in confirm_list:
    dark_mode()
    print("Enabled darkmode.")
elif dark_mode_request in deny_list:
    print("Skipping dark mode.")
else:
    print("I don't understand. If you would like to enable darkmode, please enable manually.")

reboot_confirmation = input("Reboot device?")

if reboot_confirmation in confirm_list:
    print("Rebooting")
    subprocess.run(["sudo", "reboot", "now"])
elif reboot_confirmation in deny_list:
    print("Not rebooting.")
else:
    print("I don't understand. If you would like to reboot, please reboot manually.")

