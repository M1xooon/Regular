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
    repeated_list=list()
    for contact in range(len(contacts)-1):
        for new_contact in range(contact+1,len(contacts)):
            if contacts[contact][0] == contacts[new_contact][0] and contacts[contact][1] == contacts[new_contact][1]:
                if contacts[contact][2] == "":
                    contacts[contact][2] = contacts[new_contact][2]
                if contacts[contact][3] == "":
                    contacts[contact][3] = contacts[new_contact][3]
                if contacts[contact][4] == "":
                    contacts[contact][4] = contacts[new_contact][4]
                if contacts[contact][5] == "":
                    contacts[contact][5] = contacts[new_contact][5]
                if contacts[contact][6] == "":
                    contacts[contact][6] = contacts[new_contact][6]
                repeated_list.append(contacts[new_contact])
    result_list = list()
    for item in contacts:
        if item not in result_list and item not in repeated_list:
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