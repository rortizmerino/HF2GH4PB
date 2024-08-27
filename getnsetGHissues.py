import os
import requests
from requests.auth import HTTPBasicAuth

from getHFPRs import get_prs
from getGHissues import get_issues
from setGHissues import create_issue

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv("GH_TOKEN")

# The repository to interact with (format: "owner/repo")
REPO = 'rortizmerino/HF2GH4PB'

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Function to check issues against some conditions
def check_and_create_issues():

    # Step 1: Get open PRs from HuggingFace
    hf_prs = get_prs()
    
    # Step 2: Get existing issues from GitHub
    gh_issues = get_issues()

    # Extract PR titles or identifiers from the existing issues
    existing_pr_titles = {issue['title'] for issue in gh_issues}

    # Step 3: Compare and create issues for new PRs
    for pr in hf_prs:
        if pr['title'] not in existing_pr_titles:
            # If the PR is not represented, create a new GitHub issue
            create_gh_issue(title=pr['title'], body=pr['body'])

# Run the check and create process
if __name__ == "__main__":
    check_and_create_issues()