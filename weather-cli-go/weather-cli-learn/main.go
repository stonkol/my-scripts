package main

// weather crawler using www.weatherapi.com API -> then print it to the user
// ROADMAP: Air Quality (aqi), wind data, let user input the city name

import (
	"encoding/json" // // decode the JSON response into Go structs
	"fmt"
	"net/http" // send a GET request to the API endpoint with your API key and query parameters (like city name).
	"os"
)

func tempToDo(maxTemp float32, minTemp float32, chanceRain int) { //// change to float32?
	// COLD
	if minTemp < -30.0 {
		fmt.Println("Extrem cold, wear thermal clothes.")
	} else if minTemp < -20.0 {
		fmt.Println("Wear warm clothes.")
	} else if minTemp < -10.0 {
		fmt.Println("Somehow cold.")
	} else if minTemp < 0.0 {
		fmt.Println("Chill cold.")
	} else if minTemp < 10.0 {
		fmt.Println("Not cold at all.")
	}

	// WARM
	if maxTemp >= 50.0 {
		fmt.Println("Extreme heat, don't go out!")
	} else if maxTemp >= 40.0 {
		fmt.Println("Avoid being out too much time.")
	} else if maxTemp >= 30.0 {
		fmt.Println("Today will be a warm.")
	} else if maxTemp >= 20.0 && chanceRain <= 20 {
		fmt.Println("The perfect weather, go out rn!")
	}

	////////// Shorts ////////
	if minTemp >= -6.0 {
		fmt.Println("\nYou can wear shorts!")
	} else {
		fmt.Println("\nWear Trousers :(")
	}

	// RAIN
	if chanceRain > 70 {
		fmt.Println(chanceRain, "It's going to rain a lot, bring an umbrella!")
	} else if chanceRain > 50 {
		fmt.Println(chanceRain, "It's going to rain a bit, bring a raincoat!")
	} else if chanceRain > 30 {
		fmt.Println(chanceRain, "It's going to rain a little, bring a light raincoat!")
	} else if chanceRain > 10 {
		fmt.Println(chanceRain, "It's going to rain a little a grain of salt")
	} else {
		fmt.Println(chanceRain, "It's going to be sunny, enjoy the day!")
	}
}

type WeatherResponse struct {
	Location struct {
		Name    string `json:"name"`
		Country string `json:"country"`
	} `json:"location"`
	Current struct {
		FeelslikeC float32 `json:"feelslike_c"`
	} `json:"current"`
	Forecast struct {
		Forecastday []struct {
			Day struct {
				MaxtempC float32 `json:"maxtemp_c"`
				MintempC float32 `json:"mintemp_c"`
				// Feelslike  float32 `json:"feelslike_c"`
				ChanceRain int `json:"daily_chance_of_rain"`
			} `json:"day"`
		} `json:"forecastday"`
	} `json:"forecast"`
}

func main() {
	apiKey := "YOUR_API_KEY" // replace your own API
	location := "Honolulu"
	if len(os.Args) > 1 {
		location = os.Args[1]
	}

	url := fmt.Sprintf("http://api.weatherapi.com/v1/forecast.json?key=%s&q=%s&days=1", apiKey, location)
	resp, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != 200 {
		panic("Weather API not available")
	}

	var weather WeatherResponse
	if err := json.NewDecoder(resp.Body).Decode(&weather); err != nil {
		panic(err)
	}

	if len(weather.Forecast.Forecastday) == 0 {
		fmt.Println("ERROR: No forecast data available.")
		return
	}

	if len(weather.Forecast.Forecastday) == 0 {
		fmt.Println("ERROR: No forecast data available.")
		return
	}

	locationName := weather.Location.Name
	country := weather.Location.Country

	feelsLike := weather.Current.FeelslikeC
	tempMin := weather.Forecast.Forecastday[0].Day.MintempC
	tempMax := weather.Forecast.Forecastday[0].Day.MaxtempC
	chanceRain := weather.Forecast.Forecastday[0].Day.ChanceRain

	fmt.Printf("Weather in %s, %s: %.1f°C", locationName, country, feelsLike)
	fmt.Printf("\nMin Temp: %.1f°C", tempMin)
	fmt.Printf(" | Max Temp: %.1f°C", tempMax)

	// personalize warnings and reminders
	tempToDo(tempMax, tempMin, chanceRain)
}
