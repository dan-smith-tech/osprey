import yaml
from git import get_remote_yaml, update_remote_yaml


def get_file():
    file = get_remote_yaml("list.yaml")

    return file


def set_file(file_content):
    new_file = yaml.dump(file_content, sort_keys=False, default_flow_style=False)
    update_remote_yaml("list.yaml", new_file)

    return file_content


def get_items():
    file_content = get_file()
    items = file_content["list"]["items"]

    return items


def add_items(file_content, new_items):
    file_content["list"]["items"] += new_items

    return file_content


def delete_items(file_content, item_ids):
    items = file_content["list"]["items"]
    file_content["list"]["items"] = [
        item for i, item in enumerate(items) if i not in item_ids
    ]

    return file_content
