# Copyright 2022 Amar Brkic

# TODO: Orient more toward template files rather than doing heavy lifting myself
# TODO: or just a suggestion => more local files, or make local files option if there is no internet connection []
# TODO: Parse it yourself... []
# TODO: OPTIONAL -> Add .gitignore []
# TODO: Interaction (through print() after process is done) []
# TODO: Creating process / Wizard(-thing) / (At first run only) []
# TODO: Adding support for flags (like for example: --silent) (probably adding some terminal app framework) []
# TODO: If any of flags is not recognized, abort the proccess and print the error []
# TODO: Rather abort than create "junk" []
# TODO: MadLibs for README  <- from MAKE PROCESS []
# TODO: Initialize a git repository via GIT INIT, use a system command or find a better suitable solution because of the cross-platform(ing) []
# TODO: Make some templates, like for example SFML, SDL2, WebServer and so on []
# TODO: Add support for other programming languages []
# TODO: Different building systems (even C++, like for example we have MSBuild system, but could benefit from GNU Make, Ninja, and especially CMake) []
# TODO: Still keep some sort of default settings, to speed up things for non-thinker []
# TODO: Ease use of VCPKG (with CMake or else) []

#! DOING:
# TODO: Parse code in segments (functions, after that possible OOP implementation) [1/5]

#! DONE:
# TODO: Useful names ADVERB+NOUN (still programming related) [✔]
# TODO: Timing [✔]
# TODO: Check if there is (usable) internet connection [✔]
# TODO: OPTIONAL -> Start managing VC via GIT [✔]

# Python built-in modules
import os
import sys
import time
import random

# Installed modules
import colorama
import click
from prompt_toolkit import prompt
import urllib

# Starting Timer
start = time.perf_counter()


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


# test
if not connect():
    print(
        f"{colorama.Fore.RED}{colorama.Style.BRIGHT}No stable internet connection!")
    exit()

#! Starting script
# gets the full path from where is script been called
path = os.getcwd()

# gets the name of Projects
# index is 1 because the 0th index is name of script itself(path+name)
if len(sys.argv) > 1 and sys.argv[1][:2] != "--":
    nameOfProject = sys.argv[1]
else:
    nameOfProject = "RandomName" + str(random.randint(100, 999))

# creating root project dir
rootProjectPath = os.path.join(path, nameOfProject)
os.mkdir(rootProjectPath)

# TODO: To be considered...
# if "--cpp" in sys.argv:
#    createCppProject(path, nameOfProject)

print("Time = ", round(time.perf_counter()-start, 3), "s", sep="")
