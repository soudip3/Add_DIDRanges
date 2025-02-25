import requests,json
import time

def addDIDs(access_token, body, ENVIRONMENT, callRoutingId):
    request_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    request_body = json.dumps(body)
    
    response = requests.put(f"https://api.{ENVIRONMENT}/api/v2/architect/ivrs/{callRoutingId}", data=request_body, headers=request_headers)
    response_json = response.json()
    time.sleep(60)
    return response_json