from os import system

def createBranch(name, checkout=True):
    """ Description
        :param name: - name of branch to create
        :param checkout:
        :type bool: whether to checkout to the branch upon creation
    
    """
    name.replace(" ", "-")
    system(f"git branch {name}")
    if checkout:
        system(f"git checkout {name}")