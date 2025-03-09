from datetime import date

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
    for item in items:
        item["occurance"] = "once"

    last_login = file_content["login"]

    day_automations = []
    if last_login != date.today():
        file_content["login"] = date.today()
        file_content["list"]["day"] = []
        set_file(file_content)
        day_automations = file_content["automations"]["day"]
    else:
        for automation in file_content["automations"]["day"]:
            if automation not in file_content["list"]["day"]:
                automation["occurance"] = "day"
                day_automations.append(automation)

    items += day_automations

    tags = file_content["tags"]

    return items, tags


def add_items(file_content, new_items):
    file_content["list"]["items"] += new_items

    return file_content


def delete_items(file_content, items_to_remove):
    items = file_content["list"]["items"]

    for item in items:
        if item["content"] in [
            item_to_remove["content"] for item_to_remove in items_to_remove
        ]:
            items.remove(item)
            items_to_remove.remove(item)

    for item_to_remove in items_to_remove:
        occurance = item_to_remove["occurance"]
        item_to_remove.pop("occurance")
        file_content["list"][occurance].append(item_to_remove)

    return file_content
