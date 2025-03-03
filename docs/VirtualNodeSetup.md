# Step-by-Step Guide: Setting Up a Linux Virtual Machine for Running ORCA Calculations
### This Guide will walk through setting up a **virtual node** on PC system using **Ubuntu 22.04 LTS (Jammy Jellyfish)** with **VirtualBox**.
#### The goal is to provide a stable Linux environment for running computational chemistry software and testing changes before applying them to real mechanics.

### Setup overall takes 1-3 hours depending on expertise. 

### My PC Setup
- **CPU**: AMD Ryzen 9 7900X (12 cores, 24 threads)
- **RAM**: 64GB DDR5
- **Storage**: 1TB + SSD
- **Host OS**: Ubuntu 22.04 LTS
- **Virtualization Software**: VirtualBox
--------------------------------------
### Guide Initially Written from Dr. David Zigler (July 2023) and Dr. A.J. Kinsella-Johnson (August 2023), adapted by Monica Utashiro (January 2025).
**Disclaimer**: This guide is written, maintained and updated by people who are not experts with computers. This is knowledge collected over many weeks of research reading the Ubuntu manuals, forms and trial and error. 
It takes time to learn about file systems, directory structure, paths, permissions, and working with Linux systems in general. Along the way you can expect that:
- **You will be extremely frustrated**
- **You will find lots of resources**
- **You will feel unconfident and ignorant**
- **You will learn to question everything**

--------
## Prerequisite:
Download Ubuntu 22.40 ISO LTS (64-bit) for VM beforehand from Ubuntu's website. 
 [Ubuntu](ubuntu.com/download/desktop)

or:

`wget http://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso'

Another option: `curl -0 http://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso`

Make sure to save the downloaded ISO in a **known** directory.

--------------------------------------
## Step 1: ALWAYS START WITH SOFTWARE UPDATE

`sudo apt update`

`sudo apt upgrade`

Generally, once the system is updated, should avoide changes to the OS. Any operating system changes can affect dependencies that other programs on your computer rely on. 

You can dry-run OS updates on the VM by creating snapshots immediately before. 

Information on backing up the machine and rsync:

  - [Backing Up System](https://help.ubuntu.com/community/BackupYourSystem)

  - [rsync](https://help.ubuntu.com/community/rsync)


## Step 2: Install VirtualBox on Ubuntu

Since hostOS is Ubuntu, VirtualBox can be installed directly on the terminal:

`sudo apt update && sudo apt install -y virtualbox virtualbox-ext-pack`

Check if VirtualBox is installed:

`virtualbox --help`

------------------
## Step 3: Setup VM, Upload Ubuntu

** There will be lots of trial and error on this step, I worked with Ubuntu manual + AI chat to help navigate any errors encountered. 

#### 1.Navigate to directory where you have the ISO saved.

`cd /home/../..` 

#### 2. Verify ISO (optional but recommended)

`sha256sum ubuntu-24.04-desktop-amd64.iso`

Compare output with checksum provided on Ubuntu website.
[UbuntuRelease](https://releases.ubuntu.com/)

#### 3. Upload ISO to VirtualBox

##### a. Open VirtualBox (`virtualbox`)

##### b. Click "New" and choose (setting up VM details):

  - Name: Can Choose Anything (ex: Linux-Compute-Node1)
    
  - Type: Linux
    
  - Version: Ubuntu (64-bit)
    
##### c. Adjust Resources:

  - Memory: 16GB RAM (can be adjusted lated based on workload)

  - CPUs: 6 (or more for better performance).

##### d. Create a virtual hard disk (minimum 20 GB recommended).

  - In Settings > Storage, select **empty optical drive**.

  - Select "Create a virtual hard disk now".

  - Choose **VMDK (Virtual Machine Disk)**.

  - Set **Storage** to 100GB+ (Dynamic Allocation).


---- 

## Step.4 Update System and Install Essential Tools

`sudo apt update && sudo apt upgrade -y`


- Installing the essential system utilities.

  `sudo apt install -y build-essential curl git unzip net-tools`

- Installing ssh server for headless mode (no GUI):

  `sudo apt install -y openssh-server`

---

## Step 5: Configure Network Settings for VM

#### 1. Open Virualbox -> Seettings -> Network:
     - Adapter 1: NAT (for internet access)
     - Adapter 2: Host-Only Adapter ('vboxnet0' for local access).
     - Adapter 3: Internal Network ('intnet' for VM-to-VM communication).
2. Inside the VM, check IP settings:

`ip a`

#### 3. Assign a static IP to the internal network:
  - Open **Settings** -> **Network** -> **Wired Connection 3**.
  - **IPv4 Settings** -> **Manual**:
    - **Address**: 192.###.###.##
    - **Netmask**: 255.###.###.#
    - **Gateway**: 192.###.###.#
  - **IPv6**: Set to **Disabled**.

-------

## Step 7: Install ORCA from VM
#### 1. Can download directly from [Orca Forum](https://orcaforum.kofo.mpg.de/app.php/dlext/)
#### 2. Extract ORCA:

   `tar -xvf orca_5_0_4_linux_x86-64_shared_openmpi411.tar.xz`

#### 3. Move ORCA to known directory

   `sudo mv orca_5_0_4_linux_x86-64_shared_openmpi411 /LINK/TO/DIRECTORY`

4. Setting Up ORCA Paaths

- Add ORCA to environment variable:

    `echo 'export PATH=/opt/orca:$PATH' >> ~/.bashrc`

    `source ~/.bashrc`

- Test ORCA installation (should receive orca version information in return):
    `orca` 

------

## Step 8: Enable SSH for Remote Access (Optional)

1. Install SSH server:

   `sudo apt install -y openssh-server`

2. Enable SSH:
   `sudo systemctl enable ssh`
   `sudo systemctl start ssh`

3. Allow SSH connections through firewall:

   `sudo ufw allow 22/tcp`

4. Connect to host Ubuntu system:

   `ssh username@192.###.###.##`

## Step 9: Optimize Virtual Machine Performance (Optional but Recommended)

  - Increase CPU Allocation:
      - Open **Virtual Box** -> Settings -> Processor.
      - Increase CPU cores to 4+ for better performance (depending on PC availability)
    - Enable Shared Clipboard and Drag-and-Drop:
      - Device -> Shared Clipboard -> Birectional
      - Device -> Drag & Drop -> Bidirectional
    - Boost Display Performance:
      - Settings -> Display -> Video Memory -> Set to Max (128MB)


