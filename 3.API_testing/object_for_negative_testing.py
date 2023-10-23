import requests
import json

post_product_url = 'https://api.restful-api.dev/objects'

product_headers = {
   "content-type": "application/json"
}
product_json = json.dumps({
   "name": "Apple MacBook Pro 26",
   "data": {
      "year": 2018,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
})

post_product = requests.post(post_product_url, data=product_json, headers=product_headers)
print(post_product.json())
identification = 'ff8081818905fd0e0189204a31ba0fec'

