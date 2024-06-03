from datetime import datetime
from os import system as cmd
import json


name = "Malki"
DIRECTORY = r"D:\1337\things\PyChat"

def main():
    while True:
        cmd("title Menu")
        cmd("cls")
        
        print(f"Welcome to the club, {name}\n")
        print("1) Join PyChat")
        print("2) Settings")
        print("3) Exit")
        
        choice = input()
        if choice == "1": chat()
        elif choice == "2":
            cmd("title Settings")
            cmd("cls")
            print("Coming soon")
            cmd("pause")
        elif choice == "3": break
            

def chat():
    cmd("title PyChat")
    cmd("cls")
    cmd('if not exist '+ DIRECTORY + '\\history.json echo {"messages":[{"time": 0,"name":"System","message":"[%date%]"}]}>' + DIRECTORY + "\\history.json")
    while True:
        cmd("cls")
        print("PyChat starting here!\n")
        temp_history = json.load(open(fr"{DIRECTORY}\history.json"))
        for message in temp_history.get("messages"):
            if message.get("name") == "System":
                print(f"{message.get("message")}")
            else:
                print(f"[{datetime.fromtimestamp(float(message.get("time"))).strftime("%H:%M:%S")}] {message.get("name")}: {message.get("message")}")
        print()
        message = input(">>>")
        if message == "/exit": break
        if temp_history.get("messages")[-1].get("time") != 0 and datetime.fromtimestamp(float(datetime.now().timestamp())).strftime("[%d.%m.%Y]") != datetime.fromtimestamp(float(temp_history.get("messages")[-1].get("time"))).strftime("[%d.%m.%Y]"):
            temp_history["messages"].append({"time": datetime.now().timestamp(), "name": "System", "message": datetime.fromtimestamp(float(datetime.now().timestamp())).strftime("[%d.%m.%Y]")})
        temp_history["messages"].append({"time": datetime.now().timestamp(), "name": name, "message": message})
        json.dump(temp_history, open(fr"{DIRECTORY}\history.json", "w"))
        

main()
