import time
import random

def get_gps_coordinates():
    latitude = round(random.uniform(51.1200, 51.1300), 6)
    longitude = round(random.uniform(71.4200, 71.4300), 6)
    return latitude, longitude

def analyze_frame_with_ai():
    statuses = ["Healthy", "Healthy", "Dry", "Healthy", "Disease_Pest"]
    return random.choice(statuses)

def send_radio_data(message):
    print(f"[RADIO] Transmitting data packet: {message}")

print("[START] Mobile camera box activated.")

try:
    while True:
        lat, lon = get_gps_coordinates()
        plant_health = analyze_frame_with_ai()
        
        if plant_health != "Healthy":
            data_packet = f"{plant_health};{lat};{lon}"
            send_radio_data(data_packet)
            
        time.sleep(5)

except KeyboardInterrupt:
    print("[STOP] Mobile camera box deactivated.")
