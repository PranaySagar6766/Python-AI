import requests as req
import pandas as pd


"Here we fetched the data using .get() from the api"
res = req.get('https://api.restful-api.dev/objects')
print(res.status_code)
"Stored it in a variable in json format"
response = res.json()
product_list = []
"Created an empty list to store the json data in the form of dictionary list"
for item in response:
    data = {'id' : item['id'] , 'name': item['name']}
    "Verified that the data in api is true and appended it at the end of the Product_list"
    if item['data']:
        data.update(item['data'])
    product_list.append(data)

"converted the list into DataFrame of Panda"
df = pd.DataFrame(product_list)
"converted the DF into .CSV to store it in a file"
df.to_csv('product_data.csv')

print('----------------------------------------------------')
"Send query params as list of tuples containing param name-value"
params = [('id',5),('id',7),('id',10)]
res = req.get('https://api.restful-api.dev/objects' , params)
print(res.status_code)
response = res.json()
print(response)

print('----------------------------------------------------')
"path param : to retrieve one resource uniquely"
p_id =7
res = req.get(f'https://api.restful-api.dev/objects/{p_id}')
print(res.status_code)
response = res.json()
print(response)
