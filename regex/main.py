import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

# -- 1, 2
for ind, items in enumerate(contacts_list[1:]):
  name = ' '.join(' '.join(items[:3]).split()).split()
  contacts_list[ind+1][:3] = name
  string_for_search = items[-2] # ' '.join([item[5] for item in contacts_list[1:]])
  pattern = re.compile(r"(\+7|8)+\s*\(?(\d{3})\)?[\s-]*(\d{3})-?(\d{2})-?(\d{2})\s*\(?(доб\.)*\s*(\d*)\)?")
  sub_pattern = r"+7(\2)\3-\4-\5 \6\7"
  result_string = pattern.sub(sub_pattern, string_for_search)
  contacts_list[ind+1][-2] = result_string.rstrip()

# -- 3
mydict = {}
for ind, items in enumerate(contacts_list[1:]):
  lastname = items[0]
  first_name = items[1]
  surname = items[2]
  organization = items[3]
  position = ''.join(items[4:-2])
  phone = items[-2]
  email = items[-1]
  almost_full_name = first_name + ' ' + lastname
  new_items = [lastname, first_name, surname, organization, position, phone, email]
  if almost_full_name in mydict:
    new_res = [el1 if el1 else el2 for el1, el2 in zip(mydict[almost_full_name], new_items)]
    mydict[almost_full_name] = new_res
  else:
    mydict[almost_full_name] = new_items

# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(mydict.values())
  