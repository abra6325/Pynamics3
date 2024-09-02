import os

def import_parent(name):

    cur = os.getcwd()

    exec(f"import {name}")

    os.chdir(cur)