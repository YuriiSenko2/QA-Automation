import json

post_object_json = json.dumps({
   "name": "Apple MacBook Pro 37",
   "data": {
      "year": 2023,
      "price": 1949.99,
      "CPU model": "Intel Core i90",
      "Hard disk size": "2 TB"
   }
})

update_object_json = json.dumps({
   "name": "Apple MacBook Pro 37",
   "data": {
      "year": 2023,
      "price": 3949.99,
      "CPU model": "Intel Core i90",
      "Hard disk size": "2 TB",
   }
})