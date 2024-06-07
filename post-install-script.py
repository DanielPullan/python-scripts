### Post-install script for Cyber Laptops

import subprocess

confirm_list = ['Yes', 'yes', 'Y', 'y', 'Yarp', 'yarp']
deny_list = ['No', 'no', 'N', 'n', 'Narp', 'narp'] 

def name_device(name):
    subprocess.run(["hostnamectl", "set-hostname", name])
    
def enable_ssh():
    subprocess.run(["dnf", "install", "openssh-server", "-y"])
    subprocess.run(["systemctl", "enable", "sshd"])
    subprocess.run(["systemctl", "start", "sshd"])

def install_updates():
    subprocess.run(["dnf", "update", "-y"])

def install_cockpit():
    subprocess.run(["dnf", "install", "cockpit", "-y"])
    subprocess.run(["firewall-cmd", "--add-service=cockpit"])
    subprocess.run(["firewall-cmd", "--add-service=cockpit", "--permanent"])

def install_tailscale():
    subprocess.run(["dnf", "config-manager", "--add-repo", "https://pkgs.tailscale.com/stable/fedora/tailscale.repo"])
    subprocess.run(["dnf", "install", "tailscale", "-y"])
    subprocess.run(["systemctl", "enable", "--now", "tailscaled"])

def dark_mode():
    subprocess.run(["gsettings", "set", "org.gnome.desktop.interface", "color-scheme", "'prefer-dark'"])

# def device_details()
#     hostname
#     ip addresses
#     disk free
#     memory free
#     number of cpu cores
#     operating system

device_name = input("What would you like to call this device? ")

name_device(device_name)

print("Hostname set to: ", device_name)

enable_ssh()

install_updates()

program_installs = input("Would you like to install Cockpit and Tailscale? ")

if program_installs in confirm_list:
    install_cockpit()
    install_tailscale()
    print("Installed Cockpit and Tailscale")
elif program_installs in deny_list:
    confirmation = input("Would you like to install Cockpit or Tailscale? 1 - Cockpit, 2 - Tailscale ")
    if confirmation in deny_list:
        print("Skipping installs")
    elif confirmation == 1:
        install_cockpit()
        print("Installed cockpit.")
    elif confirmation == 2:
        install_tailscale()
        print("Installed tailscale")
    else:  
        print("I don't understand. If you would like to install Cockpit or Tailscale, please install manually.")
else:  
        print("I don't understand. If you would like to install Cockpit or Tailscale, please install manually.")

dark_mode_request = input("is this device going to use a GUI? ")

if dark_mode_request in confirm_list:
    dark_mode()
    print("Enabled darkmode.")
elif dark_mode_request in deny_list:
    print("Skipping dark mode.")
else:
    print("I don't understand. If you would like to enable darkmode, please enable manually.")

# device_details()

