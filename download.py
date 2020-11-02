import os
import sys
import argparse
from github import Github

BASE_PATH = 'C:/Users/ctrla/Desktop'
os.chdir(BASE_PATH)


token = os.getenv("GITHUB_TOKEN")
g = Github(token)


user = g.get_user()

if not os.path.exists('./repos'):
    os.mkdir('repos')

os.chdir('repos')

for repo in user.get_repos():
    url = f'https://github.com/{user.login}/{repo.name}'

    if os.path.exists(repo.name):
        os.system(command=f'rd /s /q {repo.name}')

    os.system(command=f'git clone {url}')

print('All repos cloned sucessfully!')
