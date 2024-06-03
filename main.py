from datetime import datetime
from os import system as cmd
import json
from threading import Thread
import time


name = "Malki"
turn = False
pause = False
DIRECTORY = r"D:\1337\things\PyChat"

def message_check():
    cmd("cls")
    cmd('if not exist '+ DIRECTORY + '\\history.json echo {"messages":[{"time": 0,"name":"System","message":"[%date%]"}]}>' + DIRECTORY + "\\history.json")
    global temp_history
    global temp_history1
    global pause
    temp_history = json.load(open(fr"{DIRECTORY}\history.json"))
    temp_history1 = json.load(open(fr"{DIRECTORY}\history.json"))
    print("PyChat starting here!\n")
    for message in temp_history.get("messages"):
        if message.get("name") == "System":
            print(f"{message.get("message")}")
        else:
            print(f"[{datetime.fromtimestamp(float(message.get("time"))).strftime("%H:%M:%S")}] {message.get("name")}: {message.get("message")}")
    print()
    cmd('<nul set /p .=">>>"')
    while True:
        if pause == False:
            if json.load(open(fr"{DIRECTORY}\history.json")) != temp_history1:
                cmd("cls")
                print("PyChat starting here!\n")
                for message in temp_history.get("messages"):
                    if message.get("name") == "System":
                        print(f"{message.get("message")}")
                    else:
                        print(f"[{datetime.fromtimestamp(float(message.get("time"))).strftime("%H:%M:%S")}] {message.get("name")}: {message.get("message")}")
                print()
                cmd('<nul set /p .=">>>"')
                temp_history1 = temp_history
            if turn == False: break
        

def chat():
    cmd("title PyChat")
    global temp_history
    global pause
    global turn
    while True:
        message = input()
        if message == "/exit":
            turn = False
            break
        pause = True
        temp_history = json.load(open(fr"{DIRECTORY}\history.json"))
        if temp_history.get("messages")[-1].get("time") != 0 and datetime.fromtimestamp(float(datetime.now().timestamp())).strftime("[%d.%m.%Y]") != datetime.fromtimestamp(float(temp_history.get("messages")[-1].get("time"))).strftime("[%d.%m.%Y]"):
            temp_history["messages"].append({"time": datetime.now().timestamp(), "name": "System", "message": datetime.fromtimestamp(float(datetime.now().timestamp())).strftime("[%d.%m.%Y]")})
        temp_history["messages"].append({"time": datetime.now().timestamp(), "name": name, "message": message})
        json.dump(temp_history, open(fr"{DIRECTORY}\history.json", "w"))
        pause = False
        
def main():
    global turn
    while True:
        cmd("title Menu")
        cmd("cls")
        
        print(f"Welcome to the club, {name}\n")
        print("1) Join PyChat")
        print("2) Settings")
        print("3) Exit")
        
        choice = input()
        if choice == "1":
            turn = True
            task1 = Thread(target=message_check)
            task2 = Thread(target=chat)
            task1.start()
            task2.start()
            task1.join()
            task2.join()
        elif choice == "2":
            cmd("title Settings")
            cmd("cls")
            print("Coming soon")
            cmd("pause")
        elif choice == "3": break

main()
