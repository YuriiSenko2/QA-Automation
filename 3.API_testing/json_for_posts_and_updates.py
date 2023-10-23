import json

post_object_json = json.dumps({
   "name": "Apple MacBook Pro 26",
   "data": {
      "year": 2018,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})

update_object_json = json.dumps({
   "name": "Apple MacBook Pro 27",
   "data": {
      "year": 2022,
      "price": 3949.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB",
      "Availability": "No"
   }
})

patch_object_json = json.dumps({
   "name": "Apple MacBook SuperPro 2023"
})

wrong_patch_object_json = json.dumps({
   "trillo": "Apple MacBook SuperPro 2023"
})