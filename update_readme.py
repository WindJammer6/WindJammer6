import os
import re
import requests

# GitHub API endpoint for listing user repositories
github_api_url = 'https://api.github.com/users/WindJammer6/repos'

start_of_readme = '''# My GitHub Repositories :octocat:
Here are some of my GitHub repositories. This README is automatically generated and will be updated whenever a new repository is added.

'''

print(start_of_readme)

def get_repository_data():
    response = requests.get(github_api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve repository data: {response.status_code}")

def generate_table(repository_data):
    table = '| Repository | Description |\n'
    table += '| --- | --- |\n'

    for repo in repository_data:
        repo_name = repo['name']
        repo_description = repo['description'] or '-'
        table += f'| [{repo_name}]({repo["html_url"]}) | {repo_description} |\n'

    return table

def update_readme(readme_content):
    with open('README.md', 'w') as readme_file:
        readme_file.write(readme_content)

repository_data = get_repository_data()
repository_table = generate_table(repository_data)
update_readme(start_of_readme + repository_table)
