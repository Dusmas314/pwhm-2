import csv
import re


def read_file(file_name):
    with open(file_name, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_phone(contacts_list):
    number_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})' \
                     r'(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d{4})*(\)*)'
    number_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
    contacts_list_updated = []
    for phone in contacts_list:
        phone_string = ','.join(phone)
        formatted_phone = re.sub(number_pattern, number_pattern_new, phone_string)
        phone_list = formatted_phone.split(',')
        contacts_list_updated.append(phone_list)
    return contacts_list_updated


def format_name(contacts_list):
    name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    name_pattern_new = r'\1\3\10\4\6\9\7\8'
    contacts_list_updated = []
    for name in contacts_list:
        name_string = ','.join(name)
        formatted_name = re.sub(name_pattern, name_pattern_new, name_string)
        name_list = formatted_name.split(',')
        contacts_list_updated.append(name_list)
    return contacts_list_updated


def duplicates(contacts_list):
    for i in contacts_list:
        for j in contacts_list:
            if i[0] == j[0] and i[1] == j[1] and i != j:
                if i[2] == '':
                    i[2] = j[2]
                if i[3] == '':
                    i[3] = j[3]
                if i[4] == '':
                    i[4] = j[4]
                if i[5] == '':
                    i[5] = j[5]
                if i[6] == '':
                    i[6] = j[6]
    contacts_list_updated = list()
    for info in contacts_list:
        match = False
        for info_2 in contacts_list_updated:
            if info[0] == info_2[0]:
                match = True
        if not match:
            contacts_list_updated.append(info)
    return contacts_list_updated

def write_file(contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)
    return contacts_list


if __name__ == '__main__':
    contacts = read_file("phonebook_raw.csv")
    contacts = format_phone(contacts)
    contacts = format_name(contacts)
    contacts = duplicates(contacts)
    write_file(contacts)

