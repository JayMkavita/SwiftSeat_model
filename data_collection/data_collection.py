import requests
import json

def get_traffic_data(api_key, origin, destination):
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    api_key = 'AIzaSyA4s5pt-Kqveb3nlmgUn3JspkCd27TI800'
    origin = 'Donholm,Kenya'
    destination = 'Archives,Kenya'
    traffic_data = get_traffic_data(api_key, origin, destination)
    print(json.dumps(traffic_data, indent=2))
