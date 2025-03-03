#!/bin/bash

#SBATCH --account=ProjectNameUsually
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=8
#SBATCH --mem=32GB
#SBATCH --cpus-per-task=2
#SBATCH --time=0-08:00:00
#SBATCH --job-name=HYQCalculation
#SBATCH --output=HYQCalculation.out
#SBATCH --error=HYQCalculation.err

module load openmpi/4.1.2-hpcx

export ORCA=/full/pathlink/to/where/orca/program/is/saved
export ORCA_EXE=$ORCA/orca
export PATH=$ORCA:$PATH
export LD_LIBRARY_PATH=$ORCA/lib:$LD_LIBRARY_PATH

$ORCA_EXE /full/pathlink/filename.inp > /same/full/pathlink/to/input/filename.out 


