from os import system

def commitAdd(message, file="."):
    system(f"git add {file}")
    system(f'git commit -m "{message}"')