import os
from huggingface_hub import HfApi
from huggingface_hub import get_discussion_details
import requests

dataset_repo = "draco-ai/trial01"

# get access token
# Org permissions -> Repositories -> Read access to contents of all repos in selected organizations
hf_token = os.getenv("HF_TOKEN")

# Initialize the Hugging Face API with access token
#api = HfApi(token='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')
api = HfApi(token=hf_token)

try:
    # Fetch dataset repository information
    dataset_info = api.dataset_info(dataset_repo)
    
    # If successful, print some basic information about the dataset
    print(f"Dataset Name: {dataset_info.id}")
    print(f"Private: {dataset_info.private}")
    print(f"Last Modified: {dataset_info.lastModified}")

except requests.exceptions.HTTPError as http_err:
    # Handle HTTP errors (like 404 Not Found)
    print(f"HTTP error occurred: {http_err}")
except ValueError as value_err:
    # Handle other errors such as incorrect repo format
    print(f"Value error occurred: {value_err}")
except Exception as e:
    # Handle any other exceptions
    print(f"An error occurred: {e}")

# Fetch all discussions for the specified repository
from huggingface_hub import get_repo_discussions
discussions_list = list(get_repo_discussions(repo_id=dataset_repo,
                                             repo_type="dataset",
                                             discussion_type="pull_request",
                                             use_auth_token=hf_token))

# Filter only open pull requests
open_pull_requests = [pr for pr in discussions_list if pr.status == "open"]

# Print details of the open pull requests
for pr in open_pull_requests:
    print(f"PR num: {pr.num}")
    print(f"Title: {pr.title}")
    print(f"Author: {pr.author}")
    print(f"Created at: {pr.created_at}")
    print(f"URL: {pr.url}")
    print("-" * 40)