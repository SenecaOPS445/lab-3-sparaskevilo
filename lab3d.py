#!/usr/bin/env python3
#Author ID: sparaskevilo
import subprocess

#Calling and capturing the command to use in the function
disk_space = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = disk_space.communicate()

#Using function to strip command of new lines
def free_space():
    stdout = output[0].decode('utf-8').strip()
    return stdout

print(free_space())

