import requests,json
import time

def addRanges(access_token, ENVIRONMENT, StartDID, EndDID):
    request_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    request_body = json.dumps({
    "startPhoneNumber": StartDID,
    "endPhoneNumber": EndDID,
    "description": "",
    "comments": "IPI"
    })

    response = requests.post(f"https://api.{ENVIRONMENT}/api/v2/telephony/providers/edges/didpools", data=request_body, headers=request_headers)
    response_json = response.json()
    time.sleep(0.5)
    return response_json