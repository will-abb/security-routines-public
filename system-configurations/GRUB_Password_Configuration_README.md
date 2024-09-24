# GRUB Password Configuration on Ubuntu

This guide outlines the steps to secure your Ubuntu system by setting up a password for the GRUB bootloader.

## Step 1: Generate a GRUB Password Hash

1. Open a terminal and run:
   ```
   grub-mkpasswd-pbkdf2
   ```
2. Enter your desired password when prompted and note the generated hash, which looks like `grub.pbkdf2.sha512.10000.VERYLONGSTRING`.

## Step 2: Edit the GRUB Configuration

1. Edit `/etc/grub.d/40_custom`:
   ```
   sudo nano /etc/grub.d/40_custom
   ```
2. Add the following, replacing `YOUR_HASHED_PASSWORD` with your generated hash:
   ```
   set superusers="YOUR_USERNAME"
   password_pbkdf2 YOUR_USERNAME YOUR_HASHED_PASSWORD
   ```

## Step 3: Update GRUB

- Apply the changes by running:
  ```
  sudo update-grub
  ```

## Step 4: Testing

- Reboot and try editing the boot parameters. You should be prompted for a username and password.

**Note:** Losing this password can prevent boot parameter modifications. Ensure physical security for full effectiveness.
