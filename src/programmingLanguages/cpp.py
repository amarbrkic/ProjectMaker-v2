import os
import requests


def createCppProject(path, nameOfProject):
    # all subfolders that are needed
    subfolders = ["assets", "headers", "src", "bin"]

    # TODO: Maybe shortener these urls and then convert them when needed (reason: pretty unreadable)
    URLs = ["https://gist.githubusercontent.com/amarbrkic/b00b17fdf7f5ec7327dd35115a8fadd5/raw/0ec5ee0ce54768cc869d62dc9d8b8a6f70c4631a/template.vcxproj",
    "https://gist.githubusercontent.com/amarbrkic/10fde57479ccf8846eefddb4728b8851/raw/bb74f10fdc44918c6e401538b4c021d728d00812/main.cpp"]  # nopep8

    # creating subfolders
    for folder in subfolders:
        subfolderPath = os.path.join(path, nameOfProject, folder)
        os.mkdir(subfolderPath)

    #! creating and filling files with some template code...

    # README.md
    # TODO: will add some TOC template or something []
    with open(os.path.join(path, nameOfProject, "README.md"), "w") as f:
        f.write("# "+nameOfProject+"\n")

    # build.bat
    # TODO: Problem when building project with no changes in it -> "newline hack" []
    with open(os.path.join(path, nameOfProject, "build.bat"), "w") as f:
        f.write("@echo off\n")
        f.write("MSBuild "+nameOfProject +
                ".vcxproj -property:Configuration=Debug -property:Platform=x64\n")
        f.write("bin\\"+nameOfProject+".exe")

    # $nameOfProject$.vcxproj
    # TODO: Custom v142 and v143 build schemes []
    with open(os.path.join(path, nameOfProject, nameOfProject+".vcxproj"), "wb") as f:
        URL = URLs[0]
        response = requests.get(URL)
        f.write(response.content)

    # creating a main.cpp in $nameOfProject$/src
    with open(os.path.join(path, nameOfProject, "src", "main.cpp"), "wb") as f:
        URL = URLs[1]
        response = requests.get(URL)
        f.write(response.content)
