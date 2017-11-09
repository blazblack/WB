# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:16:20 2017

@author: ict
"""

import subprocess

def main():
        filename = "data.txt"
        check = subprocess.run(("gcc test2.c"), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        print(check.args)
        print(check.returncode)
        print(check.stdout)
        print(check.stderr)
        
        f = open(filename,'r', encoding="utf-8")
        exe = subprocess.run('a.exe', stdin = f, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        #exe = subprocess.run(('a.exe < data.txt'), stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        print(f)
        print(exe.args)
        print(exe.stdout)
        print(exe.returncode)
        print(exe.stderr)
                #line = f.readline()
if __name__ == '__main__':
    main()