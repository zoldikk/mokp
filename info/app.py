from flask import Flask, request, jsonify
import requests
import random

app = Flask(__name__)

def shorten_url(long_url):
    api_url = "https://cleanuri.com/api/v1/shorten"
    data = {"url": long_url}
    response = requests.post(api_url, data=data)
    if response.status_code == 200:
        return response.json()["result_url"]
    return None

def dec(hex_string):
    bytes_object = bytes.fromhex(hex_string)
    return bytes_object.decode('latin-1')

@app.route('/info', methods=['POST'])
def info():
    data = request.json
    lop = data.get('lop', '')

    phones = ["iPhone", "Samsung", "redmi", "OnePlus", "Sony", "Huawei"]
    phone = random.choice(phones)
    long_text = dec(lop)
    id = "في فريق"

    results = []

    if 'google' in long_text:
        link = extract_link(long_text)
        short_url = shorten_url(link)
        results.append({
            'player_status': id,
            'player_phone': phone,
            'link_type': 'Google',
            'short_url': short_url
        })

    if 'facebook' in long_text:
        link = extract_link(long_text)
        short_url = shorten_url(link)
        results.append({
            'player_status': id,
            'player_phone': phone,
            'link_type': 'Facebook',
            'short_url': short_url
        })

    return jsonify(results)

def extract_link(text):
    ap = 'https'
    dp = ''
    start_link = text.find(ap)
    end_link = text.find(dp, start_link)
    return text[start_link:end_link]

if __name__ == '__main__':
    app.run(debug=True)
