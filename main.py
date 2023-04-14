import random  
import tkinter as tk  # Importing tkinter for the GUI
from tkinter import (messagebox)  # Importing messagebox from tkinter for pop-up messages used for inventory show

# player data, such as their name, money, health, and points.
player = {
    "name": input("Enter your name: "),
    "money": random.randint(50, 310),
    "health": 100,
    "points": 0,
}
# a function to read the contents of a file.
def read_file(file_name):
    with open(file_name, "r") as f:  # Open the file for reading.
        content = f.read()  # Read the content of the file
    return content  # return the content.


# a function to write content to a file.
def write_file(file_name, content):
    with open(file_name, "w") as f:  # open the file for writing
        f.write(content)  # Write the content to the file


# function to parse or analyze room data from a string 
def Parsing_room_data(RoomData):
    data = {}  # Creating an empty dictionary.
    lines = RoomData.split("\n")  # Split the input string into lines.
    for line in lines:  # Iterates or goes through each line.
        if ":" in line:  # Check if the line contains a colon.
            key, value = line.split(":")  # if yes split the line into key and value.
            data[
                key.strip()
            ] = value.strip()  # Store the key-value pair in the dictionary.
    return data  # Return the dictionary.


# function that to update the room data file with the given data.
def update_room_file(file_name, RoomData):
    content = ""  # Initialize a empty string.
    for (
        key,
        value,
    ) in (
        RoomData.items()
    ): 
        content += f"{key}: {value}\n"  # Add the key value pair to the content string.
    write_file(file_name, content)  # Writes the updated content to the file.


# Function that will to calculate damage and determine if the player can defeat the enemy.
def calculate_damage(WeaponDamage, EnemyDamage, ArmourDurability):
    EnemyDamage = (
        EnemyDamage / ArmourDurability if ArmourDurability else EnemyDamage
    )  # Calculate the enemy damage based on the players armor durability.
    return (WeaponDamage >= EnemyDamage)  # Return True if the players weapon damage is enough to defeat the enemy using less then qual sign


# Function that will clear specific lines from the room data file.
def clear_RoomData(room_file):
    with open(room_file, "r") as file:  
        lines = file.readlines()  # Read all lines in the file.

    with open(room_file, "w") as file:  # Open the room data file for writing.
        for line in lines:  # Iterate through each line.
            if (
                "Weapon description:" not in line
                and "Money description:" not in line
                and "Treasure description:" not in line
                and "HealingPad description:" not in line
            ):  # Checks if the line doesn't contain specific keywords.
                file.write(line)  # Writes the line to the file.


# Function to update a specific key-value pair in the room data file.
def update_RoomData(room_file, key, value):
    with open(room_file, "r") as file: 
        lines = file.readlines()  

    updated = (
        False  # Initializing a flag to track if the key value pair was updated
    )
    with open(room_file, "w") as file: 
        for line in lines: 
            if key in line:  # Check if the line contains the specified key.
                file.write(
                    f"{key}: {value}\n"
                )  # Write the updated key and value to the file.
                updated = True  # Set the updated flag to True.
            else:
                file.write(line)  # Write the original line to the file.

        if not updated:  # Check if the key and value was not updated.
            file.write(
                f"{key}: {value}\n"
            )  # Add the new key value pair to the file.

