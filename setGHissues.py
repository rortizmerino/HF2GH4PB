import os
import requests
from requests.auth import HTTPBasicAuth

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv("GH_TOKEN")

# The repository to interact with (format: "owner/repo")
REPO = 'rortizmerino/HF2GH4PB'

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Function to create a new issue
def create_issue(title, body):
    url = f'{GITHUB_API_URL}/repos/{REPO}/issues'
    issue = {'title': title, 'body': body}
    response = requests.post(url, json=issue, auth=HTTPBasicAuth('username', GITHUB_TOKEN))
    if response.status_code == 201:
        print(f'Successfully created issue: {title}')
    else:
        print(f'Failed to create issue: {response.status_code} {response.text}')

# Run the check and create process
if __name__ == "__main__":
    #create_issue("CLI open issue test, automation to project board test", "check check")
    create_issue()