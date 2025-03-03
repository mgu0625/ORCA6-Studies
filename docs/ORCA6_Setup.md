# ORCA 6 Setup Guide

This guide explains how to install and run ORCA 6 on both a **personal computer** (with a virtual node) and an **HPC cluster** 

(OSC cluster for BGSU students).

---

## ️ **Local Setup (Personal PC)**  
### **System Specifications**
- **CPU**: AMD Ryzen 9 (12 cores)
- **RAM**: 64 GB DDR4
- **Operating System**: Linux (running via VirtualBox on host)
- **Virtual Machine (VM) Settings**:  
  - **Cores allocated**: 4  
  - **Memory allocated**: 32 GB  
  - **Disk space**: 100 GB  
  - **Operating System**: Ubuntu 22.04  
  - **Shared Folder**: `/users/PCON0421/mgutashiro/orca_qc/`

### **Installing ORCA 6** and Running Calculations on Personal PC (Linnux)
1. **Download ORCA 6** from the official ORCA
[ORCA Forum](https://orcaforum.kofo.mpg.de/app.php/portal)

[Instructions](https://www.faccts.de/docs/orca/6.0/tutorials/first_steps/install.html)

Make sure to download **from VirtualMachine** if using VirtualNode (VirtualBox in my case)

2. **Extract ORCA** in a desired directory (bash):
*****Don't move donwloaded files around once directory is decided, can mess up system for calculations from personal experience..*****
`mkdir -p` for making a new directory for ORCA
`tar -xvf orca_6_..._linux_x86-64.tar.xz -C ~/orca` for extracting

3. Setup **environment variables**:
Add this to `~/.bashrc` or `~/.bash_profile`):

`export orca=~/orca`
`export ORCA_EXE=$ORCA/orca`
`export PATH=$ORCA:$PATH`
`export LD_LIBRARY_PATH=$ORCA/lib:$LD_LIBRARY_PATH`

4. Source the file to apply changes:

`source ~/.bashrc`

5. Check if ORCA is installed correctly:

`orca --version`

-----------

# Running ORCA on Virtual Node

### Why I chose to Use Virtual Linux Node on a Linux-based PC for ORCA Calculations.

1. Resource Isolation & Optimization with Minimal Interference.
2. Consistent & Clean Computational Environment.
3. Cluster-like Setup for Scalability & Debugging without having to wait for Cluster Que.

## VirtualBox Configuration
- CPU Cores Allocated: 4 (out of 12 available)
- RAM Allocated: 32 GB (out of 64 GB)
- Disk Space: 100 GB
- OS: Ubuntu 22.04 Jellyfish

### Running ORCA in Virtual Machine
All calculations were run using 1 core (`nprocs 1`)
	- Means ORCA calculations were performed on a **single processor core**, despite the VM having 4 cores available. 

Reason to why only 1 core was used:
- `RIJCOSX` approximation works best with using 1 core for my system (personal experience)
- Prevent excess memory usage and memory bottlenecks in Virtual Machine

### When inputting coordinates.
- Always best practice to link the xyz file instead of copy + pasting coordinates directly to .inp file.
	- Allows the reuse of .inp file without having to manually paste/delete coordinates every single time.
`* xyz 0 1 MAKE/SURE/TO/ALWAYS/LINK/FULL/PATH/FILENAME.xyz`

*** no * at the end and the pathlink does not need quotes around it (will cause error if format is incorrect)

---------

# Running ORCA on an HPC Cluster (OSC for BGSU Students)

For BGSU students, ORCA 6 calculations can be run on the Ohio Supercomputer Center (OSC). 

Make sure to get account and login from advisor. 

### Cluster Setup
1. Login to OSC:
`ssh username@pitzer.osc.edu`

2. Transfering files to/from OSC (separate tab, from personal computer):
***From Personal Experience, ALWAYS Reccommend to Transfer Files to/from Personal Computer Instead of from Cluster***

If Logged into Cluster CTRL+T to open new tab. From the new tab:

	If copying from personal computer to cluster (`scp -r ...` for transfering entire file)
		- `scp /make/sure/to/link/entire/pathname.inp username@pitzer.osc.edu:/link/to/entire/path.inp`
		- paste directly to a new file (`nano filename.inp` or `vi filename.inp`)
	If copying from cluster to personal computer
		- `scp username@pitzer.osc.edu:/link/to/entire/pathname.inp /link/to/path/you/want.inp`
		- paste directly to a new file

3. Make Submission Script for Calculation:
Example Script is located in input_files

4. Submit job to OSC
`sbatch Submissionscript.sh`

5. Check Job Status
`squeue -u username`

6. Cancelling Jobs
`scancel -jobnumner` or `scancel -u username` to cancel all jobs under username

 
