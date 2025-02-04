# Step-by-Step Guide: Setting Up a Linux Virtual Machine for Running ORCA Calculations
### This Guide will walk through setting up a **virtual node** on PC system using **Ubuntu 22.04 LTS (Jammy Jellyfish)** with **VirtualBox**.
#### The goal is to provide a stable Linux environment for running computational chemistry software and testing changes before applying them to real mechanics.

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
--------------------------------------
## Step 1: ALWAYS START WITH SOFTWARE UPDATE

`sudo apt update`

`sudo apt upgrade`

Generally, once the system is updated, should avoide changes to the OS. Any operating system changes can affect dependencies that other programs on your computer rely on. 

You can dry-run OS updates on VM by creating snapshots immediately before. 

Information on backing up machine and rsync:

  - [Backing Up System](https://help.ubuntu.com/community/BackupYourSystem)

  - [rsync](https://help.ubuntu.com/community/rsync)


## Step 2: Install VirtualBox on Ubuntu
Since hostOS is Ubuntu, VirtualBox can be installed directly on the terminal:

`sudo apt update && sudo apt install -y virtualbox virtualbox-ext-pack`

Check if VirtualBox is installed:

`virtualbox --help`

------------------
## Step 2: Download Ubuntu 22.04 ISO for the VM

#### 1.Navigate to directory where you want the ISO saved.

#### 2. Download **Ubuntu 22.04 LTS (64-bit) Desktop ISO** from Ubuntu's Website, either download directly from website or download from terminal once in desired directory (Make sure to get latest version).
  [Ubuntu](ubuntu.com/download/desktop)

`wget http://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso' 

Another option: `curl -0 http://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso`

#### 3. Verify ISO (optional but recommended)

`sha256sum ubuntu-24.04-desktop-amd64.iso`

Compare output with checksum provided on Ubuntu website.

#### 4. Upload ISO to VirtualBox

a. Open VirtualBox (`virtualbox`)

b. Click "New" and choose (setting up VM details):

  - Name: Can Choose Anything (ex: Linux-Compute-Node1)
    
  - Type: Linux
    
  - Version: Ubuntu (64-bit)
    
c. Adjust Resources:

  - Memory: 16GB RAM (can be adjusted lated based on workload)

  - CPUs: 6 (or more for better performance).

d. Create a virtual hard disk (minimum 20 GB recommended).

  - In Settings > Storage, select empty optical drive.

  - Select "Create a virtual hard disk now".

  - Choose **VMDK (Virtual Machine Disk)**.

  - Set **Storage** to 100GB+ (Dynamic Allocation).









