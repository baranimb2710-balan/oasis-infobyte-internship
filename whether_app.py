import requests   # Command: import requests library for API calls

API_KEY = "d128399847615ffca3059529d18765fd"   # Command: store your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" # Command: base API endpoint

def get_weather(city):   # Command: define function to fetch weather
    if not city.strip():   # Command: input validation
        print("City name cannot be empty.")
        return
    
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"   # Command: build API request URL
    try:
        response = requests.get(url, timeout=5)   # Command: make API call
        data = response.json()   # Command: parse JSON response
        
        if response.status_code == 200:   # Command: check if API call succeeded
            temp_c = data["main"]["temp"]   # Command: extract temperature in Celsius
            temp_f = (temp_c * 9/5) + 32   # Command: convert to Fahrenheit
            humidity = data["main"]["humidity"]   # Command: extract humidity
            condition = data["weather"][0]["description"].title()   # Command: extract condition
            wind_speed = data["wind"]["speed"]   # Command: extract wind speed
            
            # Command: print results
            print(f"Weather in {city}:")
            print(f"Temperature: {temp_c:.1f}°C / {temp_f:.1f}°F")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")
            print(f"Wind Speed: {wind_speed} m/s")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather')}")   # Command: handle API error
    except requests.exceptions.RequestException:
        print("Network error. Please try again later.")   # Command: handle network error

if __name__ == "__main__":   # Command: entry point of program
    city = input("Enter city name: ")   # Command: prompt user input
    get_weather(city)   # Command: call function
