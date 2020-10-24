import os
import sys
import argparse
from github import Github

token = os.getenv("GITHUB_TOKEN")
g = Github(token)


user = g.get_user()

parser = argparse.ArgumentParser()
parser.add_argument('repo_name', type=str, help="A name for new repo")
parser.add_argument('-private', type=bool, default=False,
                    help="Set private to True for private repo")

args = parser.parse_args()
name = args.repo_name
is_private = args.private

# Current location
curr = os.getcwd()


try:
    repo = user.create_repo(name, private=is_private)
    print(repo)
    commands = [f'echo # {repo.name} >> README.md',
                'git init',
                'git add README.md',
                'git commit -m "first commit"',
                f'git remote add origin https://github.com/{user.login}/{repo.name}.git',
                'git push -u origin master']

    # Create folder with repo name
    os.mkdir(repo.name)

    # Change directory
    os.chdir(repo.name)

    for command in commands:
        os.system(command)

    print(f"Repo {repo.name} created sucessfully...")
    print("Happy coding!")

    # To start coding in vsc
    os.system('code .')

except:
    print("Repo already exists or Invalid token")
