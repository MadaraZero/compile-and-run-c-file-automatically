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
# Imports a module that allows to execute terminal commands through Python.
from subprocess import call
# A module used for making sure that the file you want to compile exists.
import os.path
# sleep module from time to add a dramatic effect in the run_valgrind() function
# Feel free to remove this aesthetic descision.
from time import sleep


# Compile and run.______________________________________________________________
def compile_and_run(file_name):
    # The following command will compile C code.
    call(["gcc", "-g", file_name, "-o", "binary_version"])
    # The following command will run the compiled file.
    print("\n")
    call(["./binary_version"])


# Run Valgrind._________________________________________________________________
def run_valgrind():
    print("Analyzing script ...")      # <--- Feel free to delete.
    sleep(3)                           # <--- Feel free to delete.
    # The following command will execute Valgind.
    call(["valgrind", "--leak-check=yes", "./binary_version"])


# User interface._______________________________________________________________
def select_option():
    # Asks the user which C file to run. For example: addition.c
    # If you don't want to continue the script insert n.
    user_input = str(raw_input("\n\tRun C file: "))
    user_input_2 = "y"

    # Checking whether the user wants to exit the script.
    if user_input == "n":
        exit(0)

    # Checking whether the file you want to compile exists.
    elif not os.path.exists(user_input):
        print("\nFile doesn't exist.")
        select_option()

    while user_input_2 != "n":
        compile_and_run(user_input)
        # You can safely re-run the script after having made changes.
        user_input_2 = str(raw_input("\n\tRe-run script y/n?: "))

    else:
        # Asks the user if they want to run Valgrind on their script.
        user_input_3 = str(raw_input("\n\tRun Valgrind y/n?: "))
        if user_input_3 == "y":
            run_valgrind()
            select_option()

        else:
            # Asks user whether they want to exit script or not.
            user_input_4 = str(raw_input("\n\tExit script? y/n: "))
            if user_input_4 == "y":
                # Exit script.
                exit(0)

            else:
                # Restarts the script.
                select_option()


select_option()
