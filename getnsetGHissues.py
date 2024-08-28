import os
import requests
from requests.auth import HTTPBasicAuth

from getHFPRs import get_prs
from getGHissues import get_issues
from setGHissues import create_issue

# Your GitHub personal access token
GITHUB_TOKEN = os.getenv("GH_TOKEN")

# The repository to interact with (format: "owner/repo")
REPO = os.getenv("GH_REPO")

# GitHub API base URL
GITHUB_API_URL = 'https://api.github.com'

# Function to check issues against some conditions
def check_and_create_issues():

    # Step 1: Get open PRs from HuggingFace
    hf_prs = get_prs()
    
    # Step 2: Get existing issues from GitHub
    gh_issues = get_issues()

    for pr_key in hf_prs.keys():
        if pr_key in gh_issues:
            print(f"Issue already exists for PR: {pr_key}")
        else:
            print(f"Creating issue for PR: {pr_key}")
            print(f"By: {hf_prs[pr_key]}")
            create_issue(title=pr_key, body=f"By: {hf_prs[pr_key]}")

# Run the check and create process
if __name__ == "__main__":
    check_and_create_issues()