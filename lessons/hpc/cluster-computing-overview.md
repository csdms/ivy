![Ivy logo](https://raw.githubusercontent.com/csdms/ivy/main/media/logo.png)

# Overview of cluster computing

A *cluster computer* is a supercomputer
constructed from individual cheap, replaceable computers,
called *nodes*,
that are linked by a fast network.
Each node has its own operating system,
usually a Linux variant.
In a typical setup,
one of the nodes in the cluster
is configured as the *head node*,
which acts as the controller for the cluster.
The remainder of the nodes
are configured as *compute nodes*.
Through the use of specially designed software,
the nodes of a cluster
act as a single computer.

A typical cluster is diagrammed here:

![A typical cluster computer configuration. (Public domain image from https://en.wikipedia.org/wiki/File:Beowulf.png)](https://upload.wikimedia.org/wikipedia/commons/4/40/Beowulf.png)

Note how the outside world can only communicate with the cluster through the server
(i.e., the head node, in the terminology we're using);
the compute nodes are hidden.
The head node is linked to the compute nodes through a local network.
The head node and the compute nodes may also share
a locally networked storage device.

## Head node use

The head (or login) node is only to be used for

* cluster access
* job scheduling
* communication with the compute nodes

Heavy computational use may cause the head node to become unresponsive,
limiting its availability to outside users and impeding job monitoring.
Always use *scheduler commands* (next section!)
to perform computational work on a cluster.

## Workflow

The typical way of working on a cluster
is to submit a *job*
to the *scheduler*
that resides on the head node.
A job is organized as a script,
typically written in bash or in Python,
that contains commands to perform tasks.
If more than one job is scheduled,
they're assigned to a *queue* by the scheduler.
When adequate computing resources become available,
a job is popped off of the queue and run.
After the run completes,
any output can be collected
and transferred from the cluster
to a user's local computer.
