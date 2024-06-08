import urllib.request
import os
import subprocess

print("test2")

homepath= os.path.expanduser('~')

known_devices = ["Zig", "zig", "Zag", "zag"]

device_name = "Zig"

def download_wallpaper(device_name):
    url = 'https://3264.uk/images/'+device_name+".jpg"
    save_as = homepath+"/Pictures/wallpapertest.jpg"
    print(save_as)
    urllib.request.urlretrieve(url, save_as)
    subprocess.run(["gsettings","set", "org.gnome.desktop.background", "picture-uri", save_as])
    subprocess.run(["gsettings","set", "org.gnome.desktop.background", "picture-uri-dark", save_as])

download_wallpaper(device_name)



