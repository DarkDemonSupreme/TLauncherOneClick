#!/usr/bin/python3.10
import os

def change_directory():
    minecraft_location = "/home/zuppremo/Documents/Minecraft"
    os.chdir(minecraft_location)

def main():
    change_directory()
    command_to_execute = "java -jar "
    tlauncher_name_version = "TLauncher-2.83.jar"
    full_command = command_to_execute + tlauncher_name_version
    os.system(full_command)

if __name__ == "__main__":
    main()
