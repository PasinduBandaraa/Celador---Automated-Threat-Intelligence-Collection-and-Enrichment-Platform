import requests
import json
import time

# Function to collect data from AbuseIPDB
def collect_abuseipdb(api_key):
    url = 'https://api.abuseipdb.com/api/v2/blacklist'
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        return data['data'] if 'data' in data else []
    except Exception as e:
        print(f"Error fetching data from AbuseIPDB: {e}")
        return []

# Function to collect data from AlienVault OTX
def collect_alienvault_otx(api_key):
    url = 'https://otx.alienvault.com/api/v1/indicators/export'
    headers = {
        'X-OTX-API-KEY': api_key
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text.splitlines()
        else:
            print(f"Error: {response.status_code}")
            return []
    except Exception as e:
        print(f"Error fetching data from AlienVault OTX: {e}")
        return []

# Function to collect data from PhishTank
def collect_phishtank():
    url = 'http://data.phishtank.com/data/online-valid.json'
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Error fetching data from PhishTank: {e}")
        return []

# Function to store collected data to a JSON file
def store_data(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

def main():
    # Set your API keys
    abuseipdb_api_key = 'e57d1c0473a4830bc4ce79a77cff37861b1bebab020eebd3524aaad013b815023f0e7df3e14542e5'
    alienvault_api_key = 'f66228c953e442298f7d833aa98f48ed5fd00a381edf5b783b6580678c9d9d2a'

    # Collect data from AbuseIPDB
    print("Collecting data from AbuseIPDB...")
    abuseipdb_data = collect_abuseipdb(abuseipdb_api_key)
    store_data(abuseipdb_data, 'abuseipdb_data.json')

    # Collect data from AlienVault OTX
    print("Collecting data from AlienVault OTX...")
    alienvault_data = collect_alienvault_otx(alienvault_api_key)
    store_data(alienvault_data, 'alienvault_otx_data.txt')

    # Collect data from PhishTank
    print("Collecting data from PhishTank...")
    phishtank_data = collect_phishtank()
    store_data(phishtank_data, 'phishtank_data.json')

if __name__ == "__main__":
    main()
