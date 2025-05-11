import requests

#Base URL for the API
BASE_URL = "https://disease.sh/v3/covid-19"

#Get Global Data
def get_global_stats():
    response = requests.get(f"{BASE_URL}/all")
    data = response.json()
    print("\n🌍 Global COVID-19 Statistics:")
    print(f"🦠 Cases: {data['cases']}")
    print(f"💀 Deaths: {data['deaths']}")
    print(f"💊 Recovered: {data['recovered']}")

#Get Country Data
def get_country_stats(country):
    response = requests.get(f"{BASE_URL}/countries/{country}")
    if response.status_code == 200:
        data = response.json()
        print(f"\n📍 COVID-19 Stats for {data['country']}:")
        print(f"🦠 Cases: {data['cases']}")
        print(f"💀 Deaths: {data['deaths']}")
        print(f"💊 Recovered: {data['recovered']}")
    else:
        print("\n❌ Country not found. Please check the name and try again.")

# Main function to run the tracker
def main():
    get_global_stats()
    
    while True:
        country = input("\nEnter a country name (or type 'exit' to quit): ")
        if country.lower() == 'exit':
            print("Exiting COVID-19 Tracker. Stay safe! 😷")
            break
        get_country_stats(country)

if __name__ == "main":
    main()

