import requests, re

DOMAIN="http://legit_keycloak_1:8080"
USER="admin"
PASSWORD="password"
CLIENT_ID="admin-cli"
GRANT_TYPE="password"

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

def validate_realm_name(realm_name):
    pattern = re.compile(r'^(?!-)[a-zA-Z0-9-]{1,63}(?<!-)$')
    match = pattern.match(realm_name)
    if match:
        return True
    else:
        return False
