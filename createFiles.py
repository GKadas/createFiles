import os
import random
import string

# urandom returns a string which represents random bytes suitable for cryptographic use.
# E.g. 5 elements -> [b'\xe2\xaf\xbc:\xdd']

# TO-DO: Add errors checks for input. e.g. Min < Max always
# TO-DO: Add GUI
# TO-DO: Add option for alternate name scheme

def generate_big_random_bin_file(num, sizeMin, sizeMax, filetype='bin'):
    numbers = int(num)
    path = input(
        "Your current working directory: {0}.\nIf you want to change it enter a path, else hit Enter\n".format(os.getcwd()))

    if path == "":
        print("Using the current path")
    else:
        change_dir(path)

    for i in range(numbers):
        name = ''.join(random.choices(string.ascii_letters, k=8))
        filename = name + '.' + filetype[0]
        with open('%s' % filename, 'wb') as fout:
            fout.write(os.urandom(random.randrange(sizeMin * 1000000, sizeMax * 1000000)))
            print('!', end=" ")


def generate_big_random_letters(num, sizeMin, sizeMax, filetype):
    numbers = int(num)

    for i in range(numbers):
        name = ''.join(random.choices(string.ascii_letters, k=8))
        filename = name + '.' + filetype
        with open('%s' %filename, 'wb') as fout:
            fout.write(''.join([random.choice(string.letters) for i in random.randrange(sizeMin * 1000000, sizeMax * 1000000)]))


def change_dir(path):
    try:
        os.chdir(path)
        print("Directory changed successfully. Current working directory: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Directory: {0} does not exist".format(path))
    except NotADirectoryError:
        print("{0} is not a directory".format(path))
    except PermissionError:
        print("You do not have permissions to change to {0}".format(path))


def input_prompt():
    ans = True
    while ans:
        num, sizeMin, sizeMax, *filetype = input(
            "*******************\n"
            "Input the number of files you want, the minimum size and the maximum size in MB, in that order.\n"
            "You can optionally define an extension for the files. The default extension is .bin \n"
            "*******************\n").split()
        if not num.isdigit() or not sizeMin.isdigit() or not sizeMax.isdigit():
            print("one of the values is not numeric")
        else:
            ans = False
            break

    if filetype:
        generate_big_random_bin_file(int(num), int(sizeMin), int(sizeMax), filetype)
    else:
        generate_big_random_bin_file(int(num), int(sizeMin), int(sizeMax))



if __name__ == "__main__":
    input_prompt()
