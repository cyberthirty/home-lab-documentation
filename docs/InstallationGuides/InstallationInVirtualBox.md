# Installing Kali Linux in VirtualBox

Before you start, make sure you have the following:
- The latest version of VirtualBox installed on your host machine. Download it from [https://www.virtualbox.org/](https://www.virtualbox.org/).
- The Kali Linux ISO file. Download the appropriate version for your system from [https://www.kali.org/get-kali/#kali-bare-metal](https://www.kali.org/get-kali/#kali-bare-metal).

## Step 1: Create a New Virtual Machine

1. Open VirtualBox and click "New" to create a new VM.
2. Enter a name for your VM (e.g., "Kali Linux") and select "Linux" as the type and "Debian (64-bit)" as the version. Click "Next".
3. Allocate RAM to the VM. A minimum of 2048 MB (2 GB) is recommended. Click "Next".
4. Choose "Create a virtual hard disk now" and click "Create".
5. Select "VDI (VirtualBox Disk Image)" as the hard disk file type. Click "Next".
6. Choose whether the virtual disk should grow as it is used (dynamically allocated) or if it should be created at its maximum size (fixed size). Dynamically allocated is recommended. Click "Next".
7. Specify the size of your virtual hard disk. A minimum of 20 GB is recommended for Kali Linux. Click "Create".

## Step 2: Configure VM Settings

1. With the newly created VM selected, click "Settings".
2. Go to the "System" section. Under the "Motherboard" tab, ensure the boot order is set with "Hard Disk" as the first priority. You might also want to increase the number of processors under the "Processor" tab for better performance, depending on your host system's capabilities.
3. Navigate to the "Storage" section. Next to "Controller: SATA", click the empty optical disk icon, then click "Choose a disk file". Select the Kali Linux ISO you downloaded earlier. Click "OK" to close the settings dialog.

## Step 3: Install Kali Linux

1. Start the VM by selecting it and clicking "Start".
2. The VM will boot from the Kali Linux ISO. Select "Graphical Install" from the menu.
3. Follow the on-screen instructions to choose your language, location, keyboard layout, and network settings.
4. When prompted for disk partitioning, select "Guided - use entire disk". Kali Linux does not need a lot of space for a basic installation, but ensure you allocate enough based on your intended use.
5. Continue following the prompts to set your timezone, root password, and username for your non-root user.
6. The installer will then copy the files to your virtual hard disk. This process can take some time.
7. Once the installation is complete, you'll be prompted to install the GRUB bootloader. Confirm the installation and select the disk to which it should be installed (there will typically be only one choice).
8. After the installation completes, the VM will reboot. You might need to remove the ISO from the virtual CD drive through the VM settings to prevent the installer from booting again.

## Step 4: Post-Installation Setup

Once Kali Linux boots up, log in with the credentials you created during the installation process.

1. It's a good practice to update your system. Open a terminal and run the following commands:
    ```bash
    sudo apt update && sudo apt full-upgrade -y
    ```
2. Restart your VM if prompted after the updates.

3. Install VirtualBox Guest Additions for better integration between the host and guest systems (e.g., shared folders, clipboard, etc.). In the VM window's menu, go to "Devices" > "Insert Guest Additions CD image" and follow the on-screen instructions.
