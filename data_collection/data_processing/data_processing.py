import requests

def get_directions(api_key, origin, destination):
    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': origin,
        'destination': destination,
        'key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    api_key = 'AIzaSyA4s5pt-Kqveb3nlmgUn3JspkCd27TI800'
    origin = 'Donholm,Kenya'
    destination = 'Archives,Kenya'
    
    data = get_directions(api_key, origin, destination)
    print(data)  # Ensure this data matches the expected structure
