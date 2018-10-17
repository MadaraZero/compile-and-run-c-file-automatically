"""
Python script that automatically compiles and runs C code.
The idea behind the script is that it allows for quasi-dynamic typing.
OS - Ubuntu
Version - 0.3
"""

from subprocess import call

def compile_and_run_cfile():

    file_name = str(raw_input("Run C file: "))

    while file_name != "q": # Exit script with 'q' to avoid cluttered Terminal.

        call(["gcc", file_name, "-o", "binary_version"])
        call(["./binary_version"])

        compile_and_run_cfile()


    exit(0)


compile_and_run_cfile()
