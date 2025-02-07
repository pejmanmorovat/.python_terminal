import requests
import socket

# Function to get private IP
def get_private_ip():
    try:
        hostname = socket.gethostname()
        private_ip = socket.gethostbyname(hostname)
        return private_ip
    except Exception as e:
        return f"Error: {e}"

# Get public IP and location info using ip-api.com
response = requests.get("http://ip-api.com/json/")
if response.status_code == 200:
    data = response.json()
    print("== Public IP and Location Details ==")
    print(f"Public IP: {data.get('query', 'N/A')}")
    print(f"City: {data.get('city', 'N/A')}")
    print(f"Region: {data.get('regionName', 'N/A')}")
    print(f"Country: {data.get('country', 'N/A')}")
    print(f"Latitude: {data.get('lat', 'N/A')}")
    print(f"Longitude: {data.get('lon', 'N/A')}")
    print(f"ISP: {data.get('isp', 'N/A')}")
    print(f"Organization: {data.get('org', 'N/A')}")
    print(f"Timezone: {data.get('timezone', 'N/A')}")

    # Generate Google Maps link
    latitude = data.get('lat', 'N/A')
    longitude = data.get('lon', 'N/A')
    if latitude != 'N/A' and longitude != 'N/A':
        google_maps_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        print(f"Google Maps Location: {google_maps_link}")
else:
    print("Failed to fetch public IP details. Please check your internet connection.")

# Display private IP
private_ip = get_private_ip()
print("\n== Private IP Details ==")
print(f"Private IP: {private_ip}")
