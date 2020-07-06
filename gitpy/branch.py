from os import system

illegal = ["~","^",":","*","?", "\\"] # https://stackoverflow.com/a/3651867/10199319

def createBranch(name, checkout=True):
    for c in name:
        if c in illegal:
            raise ValueError(f"The character '{c}' cannot be part of a name of a branch")
    """ Description
        :param name: - name of branch to create
        :param checkout:
        :type bool: whether to checkout to the branch upon creation
    
    """
    name.replace(" ", "-")
    system(f"git branch {name}")
    if checkout:
        system(f"git checkout {name}")