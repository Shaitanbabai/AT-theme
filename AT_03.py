import requests

def get_random_cat_image(api_key):
    url = 'https://api.thecatapi.com/v1/images/search'
    headers = {'x-api-key': api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['url']
    return None