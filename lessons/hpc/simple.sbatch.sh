#!/usr/bin/env bash
#SBATCH --nodes=1               # Number of requested nodes
#SBATCH --time=0:01:00          # Max walltime
#SBATCH --job-name=simple       # Job name in queue
#SBATCH --output=simple_%j.out  # Output file name
#
# A simple SBATCH script. Submit this script with:
#
#  $ sbatch simple.sbatch.sh

hostname
whoami
