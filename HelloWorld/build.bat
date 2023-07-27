@echo off
MSBuild HelloWorld.vcxproj -property:Configuration=Debug -property:Platform=x64
bin\HelloWorld.exe