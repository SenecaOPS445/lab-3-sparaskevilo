#!/usr/bin/env python3
#Author ID: sparaskevilo
import subprocess

disk_space = subprocess.Popen(["df -h grep '/$' awk '{print $4}'"], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output = disk_space.communicate()

def free_space():
    stdout = output.decode('utf-8').strip()
    return stdout


