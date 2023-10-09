import re
import csv

def format_number(contact_list):
    phone_pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
    phone_sub = r'+7(\2)-\3-\4-\5 \6\7'
    new_list = list()
    for item in contact_list:
        item_as_string = ','.join(item)
        formatted_item = re.sub(phone_pattern, phone_sub, item_as_string)
        item_as_list = formatted_item.split(',')
        new_list.append(item_as_list)
    return new_list

def format_full_name(contact_list):
    name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                       r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_sub = r'\1\3\10\4\6\9\7\8'
    new_list = list()
    for item in contact_list:
        item_as_string = ','.join(item)
        formatted_item = re.sub(name_pattern, name_sub, item_as_string)
        item_as_list = formatted_item.split(',')
        new_list.append(item_as_list)
    return new_list


def union(contacts):
    for contact in contacts:
        for new_contact in contacts:
            if contact[0] == new_contact[0] and contact[1] == new_contact[1] and contact is not new_contact:
                if contact[2] == "":
                    contact[2] = new_contact[2]
                if contact[3] == "":
                    contact[3] = new_contact[3]
                if contact[4] == "":
                    contact[4] = new_contact[4]
                if contact[5] == "":
                    contact[5] = new_contact[5]
                if contact[6] == "":
                    contact[6] = new_contact[6]
    result_list = list()
    for item in contacts:
        if item not in result_list:
            result_list.append(item)
    return result_list

if __name__ == "__main__":
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)
    contact_list=format_full_name(contact_list)
    contact_list=format_number(contact_list)
    contact_list=union(contact_list)
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contact_list)