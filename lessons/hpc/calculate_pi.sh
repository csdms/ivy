#!/usr/bin/env bash
#SBATCH --job-name=calculate_pi
#SBATCH --output=%x_%j.out
#
# A job script that calls a Python script that approximates pi.
#
# Submit this script to the scheduler with:
#   $ qsub calculate_pi.pbs.sh

module purge
module load anaconda/2022.10

hostname
python --version

echo "Calculating pi with the Bailey-Borwein-Plouffe formula"
echo "Start time:" `date`
python calculate_pi.py 20
echo "End time:" `date`
