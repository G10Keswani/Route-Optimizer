import requests

def get_distance_matrix(addresses, api_key):
    locations = "|".join(addresses)
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={locations}&destinations={locations}&key={api_key}"
    response = requests.get(url)
    data = response.json()

    matrix = []
    for row in data['rows']:
        matrix.append([element['distance']['value'] for element in row['elements']])
    return matrix
