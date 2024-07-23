import requests
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

def flatten_json(data):
    def flatten(x, name=''):
        items = []
        if isinstance(x, dict):
            for k, v in x.items():
                new_key = f"{name}{k}"
                if isinstance(v, dict):
                    items.extend(flatten(v, new_key + '.').items())
                elif isinstance(v, list):
                    items.extend(flatten(v, new_key + '.').items())
                else:
                    items.append((new_key, v))
        elif isinstance(x, list):
            for i, v in enumerate(x):
                items.extend(flatten(v, f"{name}{i}.").items())
        return dict(items)
    return flatten(data)

def fetch_and_flatten_data(api_url):
    response = requests.get(api_url)
    response.raise_for_status()  # Ensure the request was successful
    data = response.json()
    return flatten_json(data)

def extract_route_features(flattened_data):
    distances = []
    durations = []
    
    for key, value in flattened_data.items():
        if key.endswith("legs0.distance.value") or key.endswith("legs1.distance.value") or \
           key.endswith("legs2.distance.value") or key.endswith("legs3.distance.value"):
            distances.append(value)
        elif key.endswith("legs0.duration.value") or key.endswith("legs1.duration.value") or \
             key.endswith("legs2.duration.value") or key.endswith("legs3.duration.value"):
            durations.append(value)

    total_distance = sum(distances)
    total_duration = sum(durations)
    
    return total_distance, total_duration

def train_model():
    data = pd.DataFrame({
        'distance': [10000, 15000, 20000, 25000, 30000],
        'duration': [1200, 1800, 2400, 3000, 3600],
        'duration_in_traffic': [1300, 1900, 2500, 3100, 3700],
        'seats_booked': [10, 15, 20, 25, 30]
    })

    X = data[['distance', 'duration', 'duration_in_traffic']]
    y = data['seats_booked']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model

def predict_seats(model, data):
    distance = data['distance']
    duration = data['duration']
    duration_in_traffic = data['duration_in_traffic']
    
    prediction = model.predict([[distance, duration, duration_in_traffic]])
    return prediction[0]

if __name__ == "__main__":
    api_url = 'https://maps.googleapis.com/maps/api/directions/json?origin=Place1&destination=Place2&key=AIzaSyA4s5pt-Kqveb3nlmgUn3JspkCd27TI800'
    flattened_data = fetch_and_flatten_data(api_url)
    
    distance, duration = extract_route_features(flattened_data)
    duration_in_traffic = duration  # Using duration as duration_in_traffic if not available

    model = train_model()
    
    new_data = {
        'distance': distance,
        'duration': duration,
        'duration_in_traffic': duration_in_traffic
    }
    
    predicted_seats = predict_seats(model, new_data)
    print(f"Predicted seats booked: {predicted_seats}")
