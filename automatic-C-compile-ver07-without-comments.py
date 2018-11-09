#!/usr/bin/env python3


"""
- Script version: 0.7
- Requires gcc compiler <sudo apt install gcc>
- Valgrind is useful, but not necessary <sudo apt-get install valgrind>

This script is intended to help those out that have recently started to learn C
but don't know how to execute C files. Place the script in the same folder as
your C file before using.

- Version 0.5 allows to re-compile and re-run the same C file.
- Version 0.6 fixed a bug that made the script re-run twice, instead of once.
- Version 0.7 checks if the C file that you want to compile exists.
- This script works for the Ubuntu OS, a Mac OS version might need adjustments.
"""


# Imports.______________________________________________________________________
from subprocess import call
import os.path
from time import sleep


# Compile and run.______________________________________________________________
def compile_and_run(file_name):
    call(["gcc", "-g", file_name, "-o", "binary_version"])
    print("\n")
    call(["./binary_version"])


# Run Valgrind._________________________________________________________________
def run_valgrind():
    print("Analyzing script ...")     
    sleep(3)                           
    call(["valgrind", "--leak-check=yes", "./binary_version"])


# User interface._______________________________________________________________
def select_option():

    user_input = str(raw_input("\n\tRun C file: "))
    user_input_2 = "y"

    if user_input == "n":
        exit(0)

    elif not os.path.exists(user_input):
        print("\nFile doesn't exist.")
        select_option()

    while user_input_2 != "n":
        compile_and_run(user_input)
        user_input_2 = str(raw_input("\n\tRe-run script y/n?: "))

    else:
        user_input_3 = str(raw_input("\n\tRun Valgrind y/n?: "))
        if user_input_3 == "y":
            run_valgrind()
            select_option()

        else:
            user_input_4 = str(raw_input("\n\tExit script? y/n: "))
            if user_input_4 == "y":
                exit(0)

            else:
                select_option()

select_option()
