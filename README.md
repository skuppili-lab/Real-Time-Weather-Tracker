# Real-Time-Weather-Tracker
# Weather Dashboard

A simple Python project that fetches real-time weather information for any city using the `requests` library and the wttr.in weather service.

## Features

* Get current weather information by entering a city name.
* Display current temperature in Celsius.
* Display humidity percentage.
* Show weather conditions (Sunny, Cloudy, Rainy, etc.).
* Show observation time.
* No API key required.

## Technologies Used

* Python
* Requests Library
* wttr.in Weather API

## Project Structure

```text
weather-dashboard/
│
├── weather.py
├── README.md
└── requirements.txt
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/weather-dashboard.git
```

Navigate to the project folder:

```bash
cd weather-dashboard
```

Install the required package:

```bash
pip install requests
```

## Usage

Run the program:

```bash
python weather.py
```

Example:

```text
enter your city: Hyderabad

City: Hyderabad
Observation time: 10:30 AM
Temperature: 31
Humidity: 62
Weather conditions: Partly cloudy
```

## How It Works

### Step 1: Get City Name

The user enters a city name.

```python
city = input("enter your city: ")
```

### Step 2: Create Weather URL

A URL is generated dynamically using the entered city.

```python
url = f"https://wttr.in/{city}?format=j1"
```

### Step 3: Send Request

The program sends a GET request to the weather service.

```python
response = requests.get(url).json()
```

### Step 4: Extract Data

The required weather information is extracted from the JSON response.

```python
temp = response["current_condition"][0]["temp_C"]
humidity = response["current_condition"][0]["humidity"]
weather = response["current_condition"][0]["weatherDesc"][0]["value"]
```

### Step 5: Display Results

The weather details are printed to the terminal.

## Sample Output

```text
enter your city: Visakhapatnam

City: Visakhapatnam
Observation time: 12:45 PM
Temperature: 29
Humidity: 78
Weather conditions: Light rain
```

## Learning Outcomes

Through this project, I learned:

* Python Requests Module
* Working with APIs
* JSON Parsing
* Dictionary and List Access
* User Input Handling
* String Formatting using f-strings

## Future Improvements

* Weather forecast for upcoming days
* Wind speed information
* Streamlit web interface
* Weather icons and graphics
* Save weather reports to a file
* Support for multiple cities

## Author

Sravan

Built as a beginner Python project to learn APIs and real-time data fetching.
