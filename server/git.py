import base64
import os

import yaml
from dotenv import load_dotenv
from github import Github, InputGitAuthor

load_dotenv()

GH = Github(os.getenv("GH_TOKEN"))
REPO = GH.get_repo(os.getenv("GH_REPO"))
BRANCH = "main"


def get_remote_yaml(file_path):
    try:
        file_contents = REPO.get_contents(file_path, ref=BRANCH)
        content = base64.b64decode(file_contents.content).decode()
        return yaml.safe_load(content)

    except Exception as e:
        print(f"Error getting file: {str(e)}")
        return None


def update_remote_yaml(file_path, new_yaml):
    try:
        file_contents = REPO.get_contents(file_path, ref=BRANCH)
        current_sha = file_contents.sha

        REPO.update_file(
            path=file_path,
            message="Automated file update",
            content=new_yaml,
            sha=current_sha,
            branch=BRANCH,
            committer=InputGitAuthor("Bot User", "bot@example.com"),
        )
        return True

    except Exception as e:
        print(f"Error updating file: {str(e)}")
        return False
