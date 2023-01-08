import requests
response = requests.get('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
print(response)
request = response.request
print(request)
print(request.url)
print(request.path_url)
print(request.method)
print(request.headers)
print(response.headers)
print(response.status_code)
print(response.reason)
response1 = requests.get('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131/gfhfghgjrt')
print(response1.status_code)
print(response1.reason)
print(response.json())
print(response.headers.get('Content-Type'))
print(requests.get('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
)
print(requests.post('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
)
print(requests.put('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
)
print(requests.delete('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
)

response = requests.get('https://api.vk.com/method/users.get?user_id=235356920&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131')
endpoint ='https://api.vk.com/method/photos.get?album_id=profile&access_token=vk1.a.-D4mp5PD5T0VEtl6LYBrNlpYrMLDRoe8C2Pfn9_VZWrzrT3xSMvXa6Nyt6uNat3O-62AXvbY4OXTNSDdYwGj6vTK1wD7B9W-XESYVHYVX6AqpRqhyqQMPBJYGBBDiVleHOGri9Www4yYhDxkIBhnEyLwnbC1qQC0h26rxSEULvSqoQA2PaMesCp0dXk3XpDKlwnuYKu-B3byDCkaCGyCYA&expires_in=86400&user_id=235356920&v=5.131';
print(response.json())
api_key = 'DEMO_KEY'
query_params = {"api_key":api_key, 'date': '1486793614'}
response = requests.get(endpoint,params =query_params)
photos = response.json()['response']['items']
url_photos = photos[4]
url_photos = url_photos['sizes']
url_photos = url_photos[3]
print(url_photos['url'])


