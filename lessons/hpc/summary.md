![ESPIn logo](https://raw.githubusercontent.com/csdms/espin/main/media/logo.png)

# Summary

* A cluster computer is a supercomputer assembled from cheap, replaceable nodes linked by a fast network.
* Work to be performed on a cluster -- a "job" -- is organized as a script, typically in bash or in Python.
* Jobs are scheduled on the head node of a cluster, while work is performed on the compute nodes.
* Slurm commands are used to submit and monitor jobs on a cluster.


## Key commands

* `squeue` shows the status of jobs
* `sbatch` submits a job to the queue
* `sinteractive` creates an interactive job on a compute node


## Glossary

compute node
:   A single computer in a cluster where computations are performed.

head node
:   The entry point in a cluster computing system, where the job scheduler resides.

job
:   A unit of work encapsulated in a script on a cluster computer.

job queue
:   An ordered list of job assembled by the scheduling software on
    a cluster computer.

node
:   An individual computer in a cluster.

scheduler
:   Software that controls when and where a job is run on a cluster.
