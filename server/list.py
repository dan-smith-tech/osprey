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
        item["occurence"] = "once"

    last_login = file_content["login"]

    day = date.today().weekday()
    weekday = day < 5

    day_automations = []
    weekday_automations = []
    weekend_automations = []
    if last_login != date.today():
        file_content["login"] = date.today()
        file_content["list"]["day"] = []

        if weekday:
            file_content["list"]["weekday"] = []
        else:
            file_content["list"]["weekend"] = []

        set_file(file_content)
        day_automations = file_content["automations"]["day"]
        weekday_automations = file_content["automations"]["weekday"]
        weekend_automations = file_content["automations"]["weekend"]
    else:
        for automation in file_content["automations"]["day"]:
            if automation not in file_content["list"]["day"]:
                automation["occurence"] = "day"
                day_automations.append(automation)
        if weekday:
            for automation in file_content["automations"]["weekday"]:
                if automation not in file_content["list"]["weekday"]:
                    automation["occurence"] = "weekday"
                    weekday_automations.append(automation)
        else:
            for automation in file_content["automations"]["weekend"]:
                if automation not in file_content["list"]["weekend"]:
                    automation["occurence"] = "weekend"
                    weekend_automations.append(automation)

    items += day_automations + weekday_automations + weekend_automations

    tags = file_content["tags"]

    return items, tags


def add_item(file_content, new_item):
    if new_item["content"] not in [
        item["content"] for item in file_content["list"]["items"]
    ]:
        file_content["list"]["items"].append(new_item)

    return file_content


def delete_item(file_content, item_to_delete):
    items = file_content["list"]["items"]

    print(item_to_delete)

    if item_to_delete["occurence"] == "once":
        items = [item for item in items if item["content"] != item_to_delete["content"]]
    else:
        occurence = item_to_delete["occurence"]
        item_to_delete.pop("occurence")
        file_content["list"][occurence].append(item_to_delete)

    file_content["list"]["items"] = items

    return file_content
