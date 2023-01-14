import requests, json, utils
from flask import Flask, request, render_template

DOMAIN="http://legit_keycloak_1:8080"
app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def get_post_data():
    user_input = request.form['input_data']
    if utils.validate_realm_name(user_input):
        return render_template('result.html', result="Realm names should be dns compatible. i.e. www.example.com")
    url = f"{DOMAIN}/auth/admin/realms"
    YOUR_AUTH_TOKEN=utils.token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {YOUR_AUTH_TOKEN}"
    }
    data = {
        "realm": f"{user_input}"
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return render_template('result.html', result=response.text)

@app.route('/')
def index():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
