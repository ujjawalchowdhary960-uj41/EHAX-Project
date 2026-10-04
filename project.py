import json
import time
database = {}

print("In memory Database started:Give commands SET,GET,DEL,EXIST,SAVE,LOAD,EXIT")

while True:
    command = input("command is :").strip()

    if command == "":
        continue

    parts = command.split()
    com = parts[0].upper()

    try:
        if com == "SET":
            key = parts[1]
            value = parts[2]
            database[key] = value
            print("OK")
        elif com == "SETEX":
            key = parts[1]
            seconds = int(parts[2])
            value = parts[3]
            expire_at = time.time() + seconds   
            database[key] = {"value": value, "expire_at": expire_at}
            print("OK")
        elif com == "GET":
            key = parts[1]
            if key in database:
                entry = database[key]
                if isinstance(entry, dict) and "expire_at" in entry:
                    if time.time() > entry["expire_at"]:
                        del database[key]   
                        print("key expired")
                    else:
                        print(entry["value"])
                else:
                    print(entry)  
            else:
                print("Key Not Found")
                
        elif com == "DEL":
            key = parts[1]
            if key in database:
                del database[key]
                print("The element is deleted")
            else:
                print("The element is not found in the database")
        elif com == "EXIST":
            key = parts[1]
            if key in database:
                print("The element exists in the database")
            else:
                print("the element doesn't exists in the database")
        elif com == "SAVE":
            filename = parts[1]
            with open (filename,"w") as f:
                json.dump(database,f)
                print("the data is saved in {filename}")
        elif com == "LOAD":
            filename = parts[1]
            with open (filename,"r") as f:
                database = json.load(f)
                print("the data is loaded from {filename}")
        elif com == "LPUSH":
            key = parts[1]
            value = parts[2]
            if key not in database:
                database[key] = []
            database[key].insert(0, value)
            print("added it to the list")
        elif com == "LPOP":
            key = parts[1]
            if key in database and len(database[key]) > 0:
                popped = database[key].pop(0)  
                print(popped)
            else:
                print("Key Not Found")
        elif com == "EXIT":
            print("Thank You")
            break
        else:
            print("Wrong command input")

    except IndexError:
        print("ERROR;Wrong arguments input")
    except FileNotFoundError:
        print("ERROR:File not found")