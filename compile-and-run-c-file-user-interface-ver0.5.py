"""
Python script that automatically compiles and runs C code.
The idea behind the script is that it allows for quasi-dynamic typing.
Version 0.5 allows to re-compile and re-run the same C file.
OS - Ubuntu
Version - 0.5
"""

from subprocess import call


def compile_and_run(file_name):
    # The following command will compile C code.
    call(["gcc", "-g", file_name, "-o", "binary_version"])
    # The following command will run C code.
    call(["./binary_version"])


def select_option():
    # Asks the user what C source code file to compile and run.
    user_input = str(raw_input("\n\tRun C file: "))

    while user_input != "q":
        compile_and_run(user_input)
        # Asks the user to re-compile and re-run the C file.
        # This is handy when you have made changes.
        user_input_2 = str(raw_input("\n\tRe-run script y/n?: "))

        if user_input_2 == "y":
            compile_and_run(user_input)

        else:
            user_input_2 = str(raw_input("\n\tRun Valgrind y/n?: "))
            if user_input_2 == "y":
                # The following command will execute Valgind.
                call(["valgrind", "--leak-check=yes", "./binary_version"])

            else:
                select_option()

    exit(0)

select_option()
