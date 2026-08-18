# Smart Agrobot: Precision Agriculture System

An AI-powered IoT system for real-time field monitoring, localized watering control, and instant Telegram notifications.

## System Architecture
1. **Mobile Camera Box**: Mounted on a tractor or operator, captures field frames, runs edge AI anomaly detection, and transmits GPS-tagged failure nodes over LoRa.
2. **Watering Station Server**: Receives radio signals, calculates specific vector angles and distances for directional water jets, and dispatches real-time alerts.
3. **Telegram Bot API**: Delivers detailed diagnostic messages to the farm owner.

## Repository Structure
* `mobile_box/camera_processor.py` - Script for edge camera capture, AI analysis emulation, and LoRa data transport.
* `server_and_bot/main_server.py` - Script for processing radio packets, ballistic watering calculations, and Telegram alerts.
* `requirements.txt` - System dependencies.
