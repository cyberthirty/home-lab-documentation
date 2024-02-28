# Kali Linux Installation Guide

Kali Linux is a powerful distribution designed for ethical hacking and penetration testing. It comes pre-packaged with a vast array of tools for IT security professionals. This guide will walk you through the steps to install Kali Linux on your system. Before proceeding, ensure your system meets the minimum requirements for Kali Linux:

- A minimum of 20GB of disk space for installation.
- A minimum of 2GB of RAM for i386 and AMD64 architectures. More RAM is recommended for a smoother experience.
- A USB drive (if you're installing from USB) or a DVD drive (if you're installing from a DVD).
- An internet connection is optional but recommended for updates and upgrades.

## Step 1: Download Kali Linux

1. Visit the official Kali Linux download page at [https://www.kali.org/get-kali/#kali-bare-metal](https://www.kali.org/get-kali/#kali-bare-metal).
2. Choose the version that suits your architecture (e.g., 64-bit).
3. Download the ISO file.

## Step 2: Create a Bootable USB Drive

To install Kali Linux, you need to create a bootable USB drive. You can use software like Rufus (for Windows) or dd (for Linux and macOS).

### Windows:

1. Download Rufus from [https://rufus.ie/](https://rufus.ie/).
2. Insert your USB drive into the computer.
3. Open Rufus and select your USB drive from the 'Device' dropdown.
4. Click 'SELECT' and browse to your downloaded Kali Linux ISO file.
5. Click 'START' and wait for the process to complete.

### Linux/macOS:

1. Open a terminal.
2. Identify your USB drive with `lsblk` or `diskutil list` for macOS.
3. Use the `dd` command to write the ISO to your USB drive. Replace `/dev/sdX` with your USB drive (e.g., `/dev/sdb`). Be very careful to choose the correct device, as this will erase its contents.

   ```bash
   sudo dd if=path/to/kali-linux.iso of=/dev/sdX bs=4M status=progress oflag=sync
   ```

4. Wait for the process to complete.

## Step 3: Boot from USB Drive

1. Insert the bootable USB drive into the target system.
2. Restart the system and enter the BIOS/UEFI settings. This is usually done by pressing a key such as F2, F12, Delete, or Esc immediately after turning on the computer.
3. Navigate to the Boot Menu and select your USB drive as the first boot device.
4. Save changes and exit the BIOS/UEFI. Your computer should now boot from the USB drive into the Kali Linux installer.

## Step 4: Install Kali Linux

1. Once Kali Linux boots up, you'll see a menu with several options. Choose "Graphical Install" for a user-friendly installation process.
2. Follow the on-screen instructions. You'll be asked to select a language, location, and keyboard layout.
3. Set up your network (if available) and hostname for your Kali Linux system.
4. When prompted, create a disk partition. For most users, the guided partitioning method should suffice.
5. Set a password for the root user.
6. The installer will now copy the Kali Linux system to your hard drive. This process may take some time.
7. After the installation is complete, you'll be prompted to install the GRUB bootloader. Select your primary drive (usually `/dev/sda`).
8. Finally, reboot your system. Remove the USB drive when prompted. Kali Linux should boot up, and you can log in with the root account using the password you set during installation.

## Step 5: Post-Installation

After installing Kali Linux, it's a good idea to update your system to get the latest security patches and software updates:

1. Open a terminal.
2. Update your package index:

   ```bash
   sudo apt update
   ```

3. Upgrade your installed packages:

   ```bash
   sudo apt upgrade -y
   ```

4. Reboot your system if prompted.
