# Weather Notifier (WaaS – Weather as a Service)

## What This Project Does
This project is a weather notification tool that uses the OpenWeather API to analyze 3-hour forecast data and determine whether rain or snow is expected within the next 12 hours. If precipitation is detected, an automated SMS alert is sent to my personal phone using Twilio. The design is intentionally flexible to allow future expansion to multiple users or locations.

## How It Works
The script retrieves forecast data from the OpenWeather API, parses JSON weather conditions and timestamps, converts UTC timestamps to local time, and checks upcoming 3-hour forecast blocks for precipitation. When rain or snow is predicted within the next 12 hours, it sends an SMS notification via Twilio.

## Technologies Used
- Python
- OpenWeather API
- Twilio SMS API

## Future Improvements
- Integrate with low-power embedded hardware (e.g., Seeed XIAO ESP32, Nordic nRF BLE devices, or an SBC like Orange/Raspberry Pi) for standalone weather alert system
- Add additional weather conditions (temperature extremes, wind alerts, etc.)
- Add logging and error handling for long-term operation
- Potential dashboard or IoT integration for real-time monitoring
- Ultimately, evolve this project toward a self-hosted “Weather as a Service” (WaaS) platform with continuous deployment, multi-location monitoring, and optional user-configurable alerts


