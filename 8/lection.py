import json
# my_dict = {
#   "first_name": "Джон",
#   "last_name": "Смит",
#   "hobbies": ["кузнечное дело", "программирование", "путешествия"],
#   "age": 35,
#   "children": [
#   {
#     "first_name": "Алиса",
#     "age": 5
#   },
#   {
#     "first_name": "Маруся",
#     "age": 3
#   }
#   ]
# }
# dict_to_json_text = json.dumps(my_dict)
# print(f'{type(dict_to_json_text) = }\n{dict_to_json_text = }')

import json
my_dict = {
  "id": 123,
  "name": "Clementine Bauche",
  "username": "Cleba",
  "email": "cleba@corp.mail.ru",
  "address": {
    "street": "Central",
    "city": "Metropolis",
    "zipcode": "123456"
  },
  "phone": "+7-999-123-45-67"
}
res = json.dumps(my_dict, indent=2, separators=(',', ':'), sort_keys=False)
print(res)