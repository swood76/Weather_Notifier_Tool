# Weather Notifier (WaaS – Weather as a Service)

## What This Project Does
This project is a personal weather notification tool that uses the OpenWeather API to analyze 3-hour forecast data and determine whether rain or snow is expected within the next 12 hours. If precipitation is detected, an automated SMS alert is sent to my phone using Twilio.

## How It Works
The script retrieves forecast data from the OpenWeather API, parses JSON weather conditions and timestamps, converts UTC timestamps to local time, and checks upcoming 3-hour forecast blocks for precipitation. When rain or snow is predicted within the next 12 hours, it sends an SMS notification via Twilio.

## Technologies Used
- Python
- OpenWeather API
- Twilio SMS API
- requests

## Future Improvements
- Integrate with embedded hardware (e.g., microcontroller or SBC) for standalone alerts
- Add additional weather conditions (temperature extremes, wind alerts, etc.)
- Improve notification formatting and scheduling
- Add logging and error handling for long-term operation
- Potential dashboard or IoT integration for real-time monitoring


