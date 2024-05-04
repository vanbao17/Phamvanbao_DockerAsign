import requests
import json
def fetch_base_menu():
    url = "https://beta-api.waka.vn/super/getBaseMenu"
    response = requests.get(url)
    if response.status_code == 200:
        byte_data =response.content
        decoded_data = byte_data.decode('utf-8')
        json_data = json.loads(decoded_data)
        data = json.dumps(json_data)
        d2 = json.loads(data)
        return d2['data']
    else:
        raise Exception("Failed to fetch posts from API")
def fetch_detail_base_menu(content_type="ebook"):
    url = "https://beta-api.waka.vn/super/listCategoryByPage?page="+content_type
    response = requests.get(url)
    if response.status_code == 200:
        byte_data =response.content
        decoded_data = byte_data.decode('utf-8')
        json_data = json.loads(decoded_data)
        data = json.dumps(json_data)
        d2 = json.loads(data)
        return d2['data']['category']['list']
    else:
        raise Exception("Failed to fetch posts from API")
def fetch_books():
    url = "https://beta-api.waka.vn/super/listContentMajor?os=wap&id=bb4c2e10550e7b78cc543e18f1f8997d&account=guest&major_id=504&content_type=0&page_no=1&page_size=10&secure_code=xfWgENs%2Fs8VwJ5dvW1MQT%2B96em8%3D"
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            byte_data =response.content
            decoded_data = byte_data.decode('utf-8')
            json_data = json.loads(decoded_data)
            data = json.dumps(json_data)
            d2 = json.loads(data) 
            return d2['data']
        else:
            raise Exception("Failed to fetch posts from API")           
    except:
        raise Exception("Failed to fetch posts from API")   


