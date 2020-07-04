# Inspired by Kalle Hallden

import os
import sys
from github import Github

path = os.getenv("FILEPATH")
username = os.getenv("USER")
password = os.getenv("PASS")

# Github instance
g = Github(username, password)
user = g.get_user()

name = sys.argv[1]
loc = path + name


try:
    repo = user.create_repo(name)
    commands = [f'echo # {repo.name} >> README.md',
                'git init',
                'git add README.md',
                'git commit -m "first commit"',
                f'git remote add origin https://github.com/{username}/{repo.name}.git',
                'git push -u origin master']

    # Create folder with repo name
    os.mkdir(loc)

    # Change directory
    os.chdir(loc)

    for command in commands:
        os.system(command)

    print(f"{name} created sucessfully...")
    print("Happy coding!")

    # To start coding in vsc
    os.system('code .')

except:
    print("Repo already exists...")
