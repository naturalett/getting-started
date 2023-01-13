import requests, json
from flask import Flask, request, render_template

DOMAIN="http://legit_keycloak_1:8080"
USER="admin"
PASSWORD="password"
CLIENT_ID="admin-cli"
GRANT_TYPE="password"
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def get_post_data():
    user_input = request.form['input_data']
    url = f"{DOMAIN}/auth/admin/realms"
    YOUR_AUTH_TOKEN=token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {YOUR_AUTH_TOKEN}"
    }
    data = {
        "realm": f"{user_input}"
    }
    print(user_input)
    print(YOUR_AUTH_TOKEN)
    print(data)
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(response)
    return render_template('result.html', result=response.text)

@app.route('/')
def index():
    return render_template('form.html')

def token():
    url = f"{DOMAIN}/auth/realms/master/protocol/openid-connect/token"
    data = {
        "client_id": f"{CLIENT_ID}",
        "username": f"{USER}",
        "password": f"{PASSWORD}",
        "grant_type": f"{GRANT_TYPE}" 
    }
    response = requests.post(url, data=data)
    access_token = response.json()['access_token']
    print(access_token)
    return access_token

if __name__ == '__main__':
    app.run(host='0.0.0.0')
