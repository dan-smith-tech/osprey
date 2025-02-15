import base64
import os

import yaml
from dotenv import load_dotenv
from github import Github, InputGitAuthor

load_dotenv()

GH = Github(os.getenv("GH_TOKEN"))
REPO = GH.get_repo(os.getenv("GH_REPO"))
BRANCH = "main"


def update_remote_file(file_path, new_content, commit_message):

    try:
        file_contents = REPO.get_contents(file_path, ref=BRANCH)
        current_content = base64.b64decode(file_contents.content).decode()
        current_sha = file_contents.sha

        data = yaml.safe_load(current_content)
        data["list"]["items"].append("This is a new item added from my Python script!")
        updated_content = yaml.dump(data, sort_keys=False, default_flow_style=False)

        REPO.update_file(
            path=file_path,
            message=commit_message,
            content=updated_content,
            sha=current_sha,
            branch=BRANCH,
            committer=InputGitAuthor("Bot User", "bot@example.com"),
        )
        return True

    except Exception as e:
        print(f"Error updating file: {str(e)}")
        return False
