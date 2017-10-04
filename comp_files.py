#!/usr/bin/env python 
'''
code to compare files 
print first line in which there is difference

command to use :
    python3 comp_files.py file1 file2

a script by srbcheema1
'''
from sys import argv,exit
import os
if(len(argv) != 3):
    print('require 3 arguments')
    exit()

if(not os.path.exists(argv[1])):
    print('no file of name '+argv[1])
    exit()
if(not os.path.exists(argv[2])):
    print('no file of name '+argv[2])
    exit()

#begin the code
f1 = open(argv[1])
f2 = open(argv[2])

l1 = sum(1 for line in f1)
l2 = sum(1 for line in f2)

if(l1 != l2):
    print('files differ in size '+str(l1)+' '+str(l2))

l = min(l1,l2)

f1.seek(0,0)
f2.seek(0,0)

f1 = f1.readlines()
f2 = f2.readlines()

for i in range(l):
    if(f1[i] != f2[i]):
        print("diff in line "+str(i+1))
        print("line in file 1 :\n"+f1[i])
        print("line in file 2 :\n"+f2[i])
        exit()

print("files are identical")
