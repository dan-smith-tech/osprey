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
    same_week = last_login.isocalendar()[1] == date.today().isocalendar()[1]

    day_automations = []
    weekday_automations = []
    weekend_automations = []
    monday_automations = []
    tuesday_automations = []
    wednesday_automations = []
    thursday_automations = []
    friday_automations = []
    saturday_automations = []
    sunday_automations = []
    week_automations = []

    if last_login != date.today():
        file_content["login"] = date.today()
        file_content["list"]["day"] = []

        if weekday:
            file_content["list"]["weekday"] = []
        else:
            file_content["list"]["weekend"] = []

        if day == 0:
            file_content["list"]["monday"] = []
        elif day == 1:
            file_content["list"]["tuesday"] = []
        elif day == 2:
            file_content["list"]["wednesday"] = []
        elif day == 3:
            file_content["list"]["thursday"] = []
        elif day == 4:
            file_content["list"]["friday"] = []
        elif day == 5:
            file_content["list"]["saturday"] = []
        elif day == 6:
            file_content["list"]["sunday"] = []

        if not same_week:
            file_content["list"]["week"] = []

        set_file(file_content)

        day_automations = file_content["automations"]["day"]
        weekday_automations = file_content["automations"]["weekday"]
        weekend_automations = file_content["automations"]["weekend"]
        monday_automations = file_content["automations"]["monday"]
        tuesday_automations = file_content["automations"]["tuesday"]
        wednesday_automations = file_content["automations"]["wednesday"]
        thursday_automations = file_content["automations"]["thursday"]
        friday_automations = file_content["automations"]["friday"]
        saturday_automations = file_content["automations"]["saturday"]
        sunday_automations = file_content["automations"]["sunday"]
        week_automations = file_content["automations"]["week"]
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

        if day == 0:
            for automation in file_content["automations"]["monday"]:
                if automation not in file_content["list"]["monday"]:
                    automation["occurence"] = "monday"
                    monday_automations.append(automation)
        elif day == 1:
            for automation in file_content["automations"]["tuesday"]:
                if automation not in file_content["list"]["tuesday"]:
                    automation["occurence"] = "tuesday"
                    tuesday_automations.append(automation)
        elif day == 2:
            for automation in file_content["automations"]["wednesday"]:
                if automation not in file_content["list"]["wednesday"]:
                    automation["occurence"] = "wednesday"
                    wednesday_automations.append(automation)
        elif day == 3:
            for automation in file_content["automations"]["thursday"]:
                if automation not in file_content["list"]["thursday"]:
                    automation["occurence"] = "thursday"
                    thursday_automations.append(automation)
        elif day == 4:
            for automation in file_content["automations"]["friday"]:
                if automation not in file_content["list"]["friday"]:
                    automation["occurence"] = "friday"
                    friday_automations.append(automation)
        elif day == 5:
            for automation in file_content["automations"]["saturday"]:
                if automation not in file_content["list"]["saturday"]:
                    automation["occurence"] = "saturday"
                    saturday_automations.append(automation)
        elif day == 6:
            for automation in file_content["automations"]["sunday"]:
                if automation not in file_content["list"]["sunday"]:
                    automation["occurence"] = "sunday"
                    sunday_automations.append(automation)

        for automation in file_content["automations"]["week"]:
            if automation not in file_content["list"]["week"]:
                automation["occurence"] = "week"
                week_automations.append(automation)

    items += (
        day_automations
        + weekday_automations
        + weekend_automations
        + monday_automations
        + tuesday_automations
        + wednesday_automations
        + thursday_automations
        + friday_automations
        + saturday_automations
        + sunday_automations
        + week_automations
    )

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

    if item_to_delete["occurence"] == "once":
        items = [item for item in items if item["content"] != item_to_delete["content"]]
    else:
        occurence = item_to_delete["occurence"]
        item_to_delete.pop("occurence")
        file_content["list"][occurence].append(item_to_delete)

    file_content["list"]["items"] = items

    return file_content
