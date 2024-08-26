import os
import requests
from requests.auth import HTTPBasicAuth

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv("GH_TOKEN")

# The repository to interact with (format: "owner/repo")
REPO = 'rortizmerino/HF2GH4PB'

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Function to get all issues from the repository
def get_issues():
    url = f'{GITHUB_API_URL}/repos/{REPO}/issues'
    response = requests.get(url, auth=HTTPBasicAuth('username', GITHUB_TOKEN))
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Failed to fetch issues: {response.status_code} {response.text}')
        return []

# Run the check and create process
if __name__ == "__main__":
#    check_and_create_issues()
    issues = get_issues()

print(issues)