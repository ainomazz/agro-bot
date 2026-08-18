import math

STATION_LAT = 51.1250
STATION_LON = 71.4250

def calculate_watering_angle_and_distance(plant_lat, plant_lon):
    dx = (plant_lon - STATION_LON) * 40000000 * math.cos(math.radians(STATION_LAT)) / 360
    dy = (plant_lat - STATION_LAT) * 40000000 / 360
    
    distance = round(math.sqrt(dx**2 + dy**2), 1)
    angle = round(math.degrees(math.atan2(dy, dx)), 1)
    
    if angle < 0:
        angle += 360
    return angle, distance

def send_telegram_notification(problem_type, lat, lon, action_taken):
    print("\n--- TELEGRAM BOT NOTIFICATION ---")
    if problem_type == "Dry":
        text = "Anomaly: Dehydration detected. Wilting leaves."
    else:
        text = "Anomaly: Pathogen/Pest signature detected. Leaf discoloration."
        
    print(f"Status: Alert")
    print(f"Diagnostics: {text}")
    print(f"Target GPS: {lat}, {lon}")
    print(f"Execution: {action_taken}")
    print("---------------------------------\n")

def process_incoming_radio_signal(radio_packet):
    problem_type, lat_str, lon_str = radio_packet.split(";")
    plant_lat = float(lat_str)
    plant_lon = float(lon_str)
    
    angle, distance = calculate_watering_angle_and_distance(plant_lat, plant_lon)
    
    if problem_type == "Dry":
        action = f"Actuators aligned to {angle} degrees. Target distance {distance} meters. Localized irrigation completed."
    else:
        action = "Irrigation suppressed due to adequate soil moisture. Manual agronomist inspection required."
        
    send_telegram_notification(problem_type, plant_lat, plant_lon, action)

print("[START] Watering station control server activated.")

test_packet_1 = "Dry;51.126200;71.427100"
process_incoming_radio_signal(test_packet_1)

test_packet_2 = "Disease_Pest;51.123100;71.421500"
process_incoming_radio_signal(test_packet_2)
