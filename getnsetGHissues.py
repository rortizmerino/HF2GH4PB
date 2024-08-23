import requests
from requests.auth import HTTPBasicAuth

# Your GitHub personal access token
GITHUB_TOKEN = 'your_personal_access_token'
# The repository to interact with (format: "owner/repo")
REPO = 'your_username/your_repo'

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

# Function to create a new issue
def create_issue(title, body):
    url = f'{GITHUB_API_URL}/repos/{REPO}/issues'
    issue = {'title': title, 'body': body}
    response = requests.post(url, json=issue, auth=HTTPBasicAuth('username', GITHUB_TOKEN))
    if response.status_code == 201:
        print(f'Successfully created issue: {title}')
    else:
        print(f'Failed to create issue: {response.status_code} {response.text}')

# Function to check issues against some conditions
def check_and_create_issues():
    issues = get_issues()

    # Define your condition and logic here
    # Example: check if an issue with a specific title exists, if not, create it
    issue_titles = [issue['title'] for issue in issues]

    # Condition: If there is no issue titled "Check this important thing", create one
    if "Check this important thing" not in issue_titles:
        create_issue("Check this important thing", "This issue needs attention because...")

# Run the check and create process
if __name__ == "__main__":
    check_and_create_issues()
