from datetime import datetime
from os import system as cmd
import json


name = "Malki"
DIRECTORY = r"D:\1337\things\PyChat"

def main():
    while True:
        cmd("cls")
        
        print(f"Welcome to the club, {name}\n")
        print("1) Join PyChat")
        print("2) Settings")
        print("3) Exit")
        
        choice = input()
        if choice == "1": chat()
        elif choice == "2":
            cmd("cls")
            print("Coming soon")
            break
        elif choice == "3": break
            

def chat():
    cmd("cls")
    cmd('if not exist '+ DIRECTORY + '\\history.json echo {"messages":[]}>' + DIRECTORY + "\\history.json")
    while True:
        cmd("cls")
        print("PyChat starting here!\n")
        temp_history = json.load(open(fr"{DIRECTORY}\history.json"))
        # print(temp_history.get("messages")[-1])
        for message in temp_history.get("messages"):
            print(f"[{datetime.fromtimestamp(float(message.get("time"))).strftime("%H:%M:%S")}] {message.get("name")}: {message.get("message")}")
        print()
        message = input(">>>")
        if message == "/exit": break
        temp_history["messages"].append({"time": datetime.now().timestamp(), "name": name, "message": message})
        json.dump(temp_history, open(fr"{DIRECTORY}\history.json", "w"))
        

main()
cmd("pause")