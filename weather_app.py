
import requests

# Store your OpenWeatherMap API key here
API_KEY = 'YOUR_API_KEY_HERE'


# This function gets weather data from the API
def get_weather(city):

    # API URL where we will send the weather request
    url = 'https://api.openweathermap.org/data/2.5/weather'

    # Send city name, API key and temperature unit to the API
    params={
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }

    try:

        # Send request to the weather API
        response = requests.get( url,params=params)

        # Show the status code returned by the server
        print('Status code:', response.status_code)

        # Show the raw response for checking/debugging
        print('response', response.text)


        # Check if the city was not found
        if response.status_code == 404:
            print('\n City not found !')
            return None

        
        # Check if the request was not successfu
        if response.status_code != 200:
            print('\n Something went wrong !')
            return None


        # Convert API response from JSON into Python data
        data= response.json()


        # Send the weather data back from the function
        return data
    
    except requests.exceptions.RequestException:

        # Handle internet or connection problems
        print('\n Internet connection problem !')
        return None


# This function displays the weather data to the user
def show_weather(data):

    # Get required information from the API data
    city = data['name']
    country = data['sys']['country']
    temperature = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']
    wind_speed = data['wind']['speed']

    print('\n' + '='* 40)
    print('Weather Information')
    print('=' * 40)


    # Display weather information
    print(f'Location: {city},{country}')
    print(f'Temperature: {temperature} °C')
    print(f'Feels Like: {feels_like}  °C')
    print(f'Condition: {weather}')
    print(f'Humidity: {humidity} %')
    print(f'Wind Speed: {wind_speed} m/s')

    print('=' * 40)


# This is the main function that controls the whole app
def main():

    # Keep showing the menu until the user chooses Exit
    while True:
        
        print('\n')
        print('=' * 40)
        print('Weather APP')
        print('=' * 40)

        print('1. Search Weather')
        print('2. Exit')


        # Ask the user to choose an option
        choice = input('\nEnter you choice:')


        # If user chooses 1, search for weather
        if choice == '1':

            # Ask the user to enter a city name
            city = input('Enter city name:')


            # Check if the user entered an empty city name
            if city.strip() == '':
                print('Please enter a city name:')
                continue

            # Get weather data for the entered city
            weather_data = get_weather(city)


            # If weather data was received, display it
            if weather_data:
                show_weather(weather_data)


        # If user chooses 2, exit the application
        elif choice == '2':
            print('\n Thank you for using Weather App !')
            break


        # Handle any invalid menu choice
        else:

            print('\n Invalid choice ! Please select 1 or 2. ')

# Start the application
main()
            


