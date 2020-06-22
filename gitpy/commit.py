from os import system

def commit(message):
    system(f"git commit -m '{message}'")