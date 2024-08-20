import os
from huggingface_hub import HfApi

dataset_repo = "draco-ai/trial01"

# get access token
# Org permissions -> Repositories -> Read access to contents of all repos in selected organizations
hf_token = os.getenv("HF_TOKEN")

# Initialize the Hugging Face API with access token
#api = HfApi(token='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')
api = HfApi(token=hf_token)

from huggingface_hub import get_repo_discussions
discussions_list = list(get_repo_discussions(repo_id=dataset_repo,
                                             repo_type="dataset",
                                             discussion_type="pull_request",
                                             use_auth_token=hf_token))

for discussion in discussions_list:
    print(discussion)

#try:
    # Fetch dataset repository information
#    dataset_info = api.dataset_info(repo_id=dataset_repo, use_auth_token="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")
    
    # If successful, print some basic information about the dataset
#    print(f"Dataset Name: {dataset_info.id}")
#    print(f"Private: {dataset_info.private}")
#    print(f"Last Modified: {dataset_info.lastModified}")
#    print(f"Files: {[file.rfilename for file in dataset_info.siblings]}")

#except RepositoryNotFoundError:
#    print(f"Error: The repository '{dataset_repo}' was not found or you do not have access.")
#except Exception as e:
#    print(f"An error occurred: {e}")