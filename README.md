Project Name: In Memory Database


Objectiive: The simple objective of this project was to make a in-memory database without using any external database or caching libraries.


Overview: An in-memory database stored data directly into RAM instead of on disk, which makes the process of READ and WRITE faster but this data is volatile as it gets lost when the program stops running,so we save it to the disk.This project implements a Command-Line Interface (CLI) that mimics this behavior on a smaller scale.


Features Implemented:
1.SET <key> <value> — stores a key-value pair in memory
2.GET <key> — retrieves the value associated with a key
3.DEL <key> — deletes a key from the database
4.EXISTS <key> — checks whether a key is present
5.SAVE <filename> — persists the current state of the database to a file
6.LOAD <filename> — restores the database state from a saved file
7.SETEX <key> <seconds> <value> — sets a key with a time-to-live (TTL), after which it automatically expires.
8.LPUSH <key> <value> / LPOP <key> — supports list-type values within the database.


Tech Stack:
Language: Python 3
1.Core data structure: Python dictionary (hash table)
2.Persistence format: JSON (via Python's built-in json module)
3.Editor: VS Code


How the project works:
The database is implemented as a REPL (Read-Eval-Print-Loop) that continuously accepts user commands through the terminal. User input is parsed by splitting it on whitespace to extract the command, key, and value. The core data is stored in a Python dictionary, which internally uses a hash table, giving SET and GET operations an average time complexity of O(1), regardless of the number of entries. For persistence, the SAVE command serializes the dictionary into JSON format and writes it to a file, while LOAD deserializes it back into memory. Robust error handling using try/except blocks ensures the program does not crash on malformed input, such as missing arguments or references to non-existent files.

Constraints Followed:
No external database or caching libraries (such as SQLite, TinyDB, or Redis-py) were used. All storage logic — including SET, GET, DEL, and persistence — was implemented manually using only Python's standard built-in modules.

Conclusion:
This project provided hands-on understanding of how key-value databases operate internally, including hash-based storage, command parsing, and data persistence — concepts that are foundational and used widely in production environments.
