#!/usr/bin/env python3

#paraller runnig 
from subprocess import Popen

commands = ['./bot1.py', './bot2.py']
procs = [ Popen(i) for i in commands ]
for p in procs:
   p.wait()