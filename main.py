from git import update_remote_file


def init():
    update_remote_file(
        file_path="list.yaml",
        new_content="",
        commit_message="Automated file update",
    )


if __name__ == "__main__":
    init()
