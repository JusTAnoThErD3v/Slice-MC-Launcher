import platform
import urllib.request
import subprocess
import tkinter as tk
from tkinter import *
import hashlib


######STARTUP (SOUNDS)######


######ON START LOGIC######
def start():
    app_gui.destroy()
######GUI LOGIC######

APP_NAME = "Slice-MC"
app_gui = tk.Tk()
app_gui.title("Slice-MC")
app_gui.config(background="#ffd6b5")
button = Button(app_gui, text="START SERVER", relief="raised", bd=4, padx=20, pady=20)
button.config(command=start)
button.pack()
warning = Label(app_gui, text="PRESSING START WILL CLOSE THIS WINDOW, AFTER TO CONNECT TO YOUR SERVER GO TO MULTIPLAYER AND IP WILL BE: localhost")
warning.pack()
ip = Label(app_gui, text="IP ADDRESS: localhost", font="Arial 20 bold")
ip.pack()
ip.pack()
app_gui.geometry("870x840")
app_gui.mainloop()


######FILE STARTUP######
from pathlib import Path
print("Startup...")
print("Getting system data...")
machine_platform = platform.system()
print("platform"+" "+machine_platform)
machine_architecture = platform.machine()
print("Architecture"+" ")
print("Configuring download...")

######LIBRARY OF DOWNLOAD URLs######
pumpkin_win_url_x64 = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-X64-Windows.exe"
pumpkin_win_url_arm = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-ARM64-Windows.exe"
pumpkin_lin_url_x64 = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-X64-Linux"
pumpkin_lin_url_arm = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-ARM64-Linux"
pumpkin_mac_url_x64 = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-X64-macOS"
pumpkin_mac_url_arm = "https://github.com/Pumpkin-MC/Pumpkin/releases/download/nightly/pumpkin-ARM64-macOS"
print(machine_architecture)

######LIBRARY OF HASHES######
pumpkin_win_hash_x64 = "79626acd2ee34cce8ad49a3fb27030ea22b65a148b61d0990c5de9352b31d275"
pumpkin_win_hash_arm = "e7a9dcb4117e27afd6af6ae63d5b6337500bbf875834f8b0bfa626fd3f4743f1"
pumpkin_lin_hash_x64 = "60f272a8b846759f35d00c147927df7d2482cf341d0a8998ef6f6575fd7747f2"
pumpkin_lin_hash_arm = "6765bd18e1392006eafbbb53f5e4f724a36b1ef11d8cf8b685da03e9b2384a3d"
pumpkin_mac_hash_x64 = "c620a0f65966d108ed4f4f5a1839ad10dc3153e797f23af38c3e64cec6882aab"
pumpkin_mac_hash_arm = "9067d35baab147ca2ed2c3133db4be555e32bccabc7aca779270844595bbba29"
sha256_hash = hashlib.sha256()
######INSTALL CHECKS######
print("Checking if you have already installed pumpkin, make sure it is in the root directory/folder given by this installation file!")
BASE_PATH = Path(__file__).resolve().parent
print("CWD:", Path.cwd())
print("BASE_PATH:", BASE_PATH)

win_x64_path = BASE_PATH / "pumpkin-X64-Windows.exe"
win_arm_path = BASE_PATH / "pumpkin-ARM64-Windows.exe"
lin_x64_path = BASE_PATH / "pumpkin-X64-Linux"
lin_arm_path = BASE_PATH /"pumpkin-ARM64-Linux"
mac_x64_path = BASE_PATH / "pumpkin-X64-macOS"
mac_arm_path = BASE_PATH / "pumpkin-ARM64-macOS"

#note that commands with question marks ("?") at the end will be ones I have not physically tested on real nor virtual hardware and, thus it may not work especially on newer versions.
#macos will deliver arm64 for arm
#macos will deliver x86_64 for x64
#linux will deliver aarch64 for arm?
#linux will deliver x86_64 for x64?
#windows will deliver ARM64 for arm?
#windows will deliver AMD64 for x64



if machine_platform == "Windows" and machine_architecture == "AMD64":
    print("win check...")
    if win_x64_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("pumpkin-X64-Windows.exe")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_win_x64 from locally stored url...")
        urllib.request.urlretrieve(pumpkin_win_url_x64, "pumpkin-X64-Windows.exe")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        win_x64_sha_checksum = hashlib.sha256(open(win_x64_path, "rb").read()).hexdigest()
        if win_x64_sha_checksum == pumpkin_win_hash_x64:
            print("Running...")
            subprocess.Popen("pumpkin-X64-Windows.exe")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")





if machine_platform == "Windows" and machine_architecture == "ARM64":
    print("win check...")
    if win_arm_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("pumpkin-ARM64-Windows.exe")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_win_arm64 from locally stored url...")
        urllib.request.urlretrieve(pumpkin_win_url_arm, "pumpkin-ARM64-Windows.exe")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        win_arm_sha_checksum = hashlib.sha256(open(win_arm_path, "rb").read()).hexdigest()
        if win_arm_sha_checksum == pumpkin_win_hash_arm:
            print("Running...")
            subprocess.Popen("pumpkin-ARM64-Windows.exe")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")



if machine_platform == "Linux" and machine_architecture == "x86_64":
    print("linux check...")
    if lin_x64_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("./pumpkin-X64-Linux")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_lin_x64 from locally stored url...")
        urllib.request.urlretrieve(pumpkin_lin_url_x64, "pumpkin-X64-Linux")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        lin_x64_sha_checksum = hashlib.sha256(open(lin_x64_path, "rb").read()).hexdigest()
        if lin_x64_sha_checksum == pumpkin_lin_hash_x64:
            print("setting up server executable...")
            subprocess.run("chmod +x pumpkin-X64-Linux", shell=True)
            print("completed without errors!")
            print("Running...")
            subprocess.Popen("./pumpkin-X64-Linux")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")

if machine_platform == "Linux" and machine_architecture == "aarch64":
    print("linux check...")
    if lin_arm_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("./pumpkin-ARM64-Linux")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_lin_arm64 from locally stored url...")
        urllib.request.urlretrieve(pumpkin_lin_url_arm, "pumpkin-ARM64-Linux")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        lin_arm_sha_checksum = hashlib.sha256(open(lin_arm_path, "rb").read()).hexdigest()
        if lin_arm_sha_checksum == pumpkin_lin_hash_arm:
            print("setting up server executable...")
            subprocess.run("chmod +x pumpkin-ARM64-Linux", shell=True)
            print("completed without errors!")
            print("Running...")
            subprocess.Popen("./pumpkin-ARM64-Linux")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")

if machine_platform == "Darwin" and machine_architecture == "x86_64":
    print("macos check...")
    if mac_x64_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("./pumpkin-X64-macOS")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_mac_x64 from locally stored url...")
        urllib.request.urlretrieve(pumpkin_mac_url_x64, "pumpkin-X64-macOS")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        mac_x64_sha_checksum = hashlib.sha256(open(mac_x64_path, "rb").read()).hexdigest()
        if mac_x64_sha_checksum == pumpkin_mac_hash_x64:
            print("setting up server executable...")
            subprocess.run("chmod +x pumpkin-X64-macOS", shell=True)
            print("completed without errors!")
            print("Running...")
            subprocess.Popen("./pumpkin-X64-macOS")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")



if machine_platform == "Darwin" and machine_architecture == "arm64":
    print("macos check...")
    if mac_arm_path.is_file():
        print("It seems you have already installed Pumpkin! We will run it for you!")
        subprocess.Popen("./pumpkin-ARM64-macOS")
        print("Pumpkin is running!")
    else:
        print("Downloading pumpkin_mac_arm from locally stored url...")
        urllib.request.urlretrieve(pumpkin_mac_url_arm, "pumpkin-ARM64-macOS")
        print("Download Complete!")
        print("Checking to make sure the hashes match up...")
        mac_arm_sha_checksum = hashlib.sha256(open(mac_arm_path, "rb").read()).hexdigest()
        if mac_arm_sha_checksum == pumpkin_mac_hash_arm:
            print("setting up server executable...")
            subprocess.run("chmod +x pumpkin-ARM64-macOS", shell=True)
            print("completed without errors!")
            print("Running...")
            subprocess.Popen("./pumpkin-ARM64-macOS")
        else:
            print("It seems they dont match... this could be since our file links update dynamically but the checksums dont but the file could also be dangerous!")
            print("Please report this to the main github account: https://github.com/JusTAnoThErD3v")




#note that commands with question marks ("?") at the end will be ones I have not physically tested on real nor virtual hardware and, thus it may not work especially on newer versions.
#macos will deliver arm64 for arm
#macos will deliver x86_64 for x64
#linux will deliver aarch64 for arm?
#linux will deliver x86_64 for x64?
#windows will deliver ARM64 for arm?
#windows will deliver AMD64 for x64

######DOWNLOAD LOGIC######
# if machine_platform == "Windows" and machine_architecture == "AMD64":
#     print("Downloading pumpkin_win_x64 from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_win_url_x64, "pumpkin-X64-Windows.exe")
#     print("Download Complete!")
# if machine_platform == "Windows" and machine_architecture == "ARM64":
#     print("Downloading pumpkin_win_arm64 from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_win_url_arm, "pumpkin-ARM64-Windows.exe")
#     print("Download Complete!")
# if machine_platform == "Linux" and machine_architecture == "x86_64":
#     print("Downloading pumpkin_lin_x64 from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_lin_url_x64, "pumpkin-X64-Linux")
#     print("Download Complete!")
#     print("setting up server executable...")
#     subprocess.run("chmod +x pumpkin-X64-Linux", shell=True)
#     print("completed without errors!")
# if machine_platform == "Linux" and machine_architecture == "aarch64":
#     print("Downloading pumpkin_lin_arm64 from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_lin_url_arm, "pumpkin-ARM64-Linux")
#     print("Download Complete!")
#     print("setting up server executable...")
#     subprocess.run("chmod +x pumpkin-ARM64-Linux", shell=True)
#     print("completed without errors!")
# if machine_platform == "Darwin" and machine_architecture == "x86_64":
#     print("Downloading pumpkin_mac_x64 from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_mac_url_x64, "pumpkin-X64-macOS")
#     print("Download Complete!")
#     print("setting up server executable...")
#     subprocess.run("chmod +x pumpkin-X64-macOS", shell=True)
#     print("completed without errors!")
# if machine_platform == "Darwin" and machine_architecture == "arm64":
#     print("Downloading pumpkin_mac_arm from locally stored url...")
#     urllib.request.urlretrieve(pumpkin_mac_url_arm, "pumpkin-ARM64-macOS")
#     print("Download Complete!")
#     print("setting up server executable...")
#     subprocess.run("chmod +x pumpkin-ARM64-macOS", shell=True)
#     print("completed without errors!")






