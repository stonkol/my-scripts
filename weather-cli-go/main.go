// based on [scrduc tutorial](https://www.youtube.com/watch?v=zPYjfgxYO7k)
package main

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type Weather struct {
	Location struct {
		Name    string `json:"name"`
		Country string `json:"country"`
	} `json:"location"`
	Current struct {
		TempC     float64 `json:"temp_c"`
		Condition struct {
			Text string `json:"text"`
		} `json:"condition"`
	} `json:"current"`
	Forescast struct {
		Forecastday []struct {
			Hour []struct {
				TimeEpoch int64   `json:"time_epoch"`
				TempC     float64 `json:"temp_c"`
				Condition struct {
					Text string `json:"text"`
				}
			} `json:"forecast"`
			ChanceOfRain float64 `json:"chance_of_rain"`
		} `json:"forecast"`
	}
}

func main() {
	res, err := http.Get("")
	if err != nil {
		panic(err)
	}
	defer res.Body.Close()

	if res.StatusCode != 200 {
		panic("Weather API not available")
	}

	body, err := io.ReadAll(res.Body)
	if err != nil {
		panic(err)
	}

	var weather Weather
	// will convert the body into what is passed in `weather`
	err = json.Unmarshal(body, &weather)
	if err != nil {
		panic(err)
	}
	fmt.Println(weather)
}
