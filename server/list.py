import yaml
from git import get_remote_yaml, update_remote_yaml


def get_items():
    file = get_remote_yaml("list.yaml")
    items = file["list"]["items"]

    return items


def add_item(new_item):
    file = get_remote_yaml("list.yaml")
    file["list"]["items"] += [new_item]
    new_file = yaml.dump(file, sort_keys=False, default_flow_style=False)
    update_remote_yaml("list.yaml", new_file)

    return file["list"]["items"]


def delete_item(item_id):
    file = get_remote_yaml("list.yaml")
    file["list"]["items"].pop(item_id)
    new_file = yaml.dump(file, sort_keys=False, default_flow_style=False)
    update_remote_yaml("list.yaml", new_file)

    return file["list"]["items"]
