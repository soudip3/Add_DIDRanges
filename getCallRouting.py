import requests,json
import time

def callRouting(access_token,callRoutingId, ENVIRONMENT):
    request_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"https://api.{ENVIRONMENT}/api/v2/architect/ivrs/{callRoutingId}", headers=request_headers)
    response_json = response.json()
    result = {
        "id": response_json["id"],
        "name": response_json["name"],
        "division": {
            "id": response_json["division"]["id"],
            "name": response_json["division"]["name"]
        },
        "state": "active",
        "dnis": response_json["dnis"],
        "openHoursFlow": {
            "id": response_json["openHoursFlow"]["id"]
        }
    }
    time.sleep(0.3)
    return result