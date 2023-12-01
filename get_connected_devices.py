import bluetooth

def get_connected_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, device_id=-1, duration=8)
    
    connected_devices = []
    
    for addr, name, in nearby_devices:
        connected_devices.append({"address": addr, "name": name})
    
    return connected_devices

if __name__ == "__main__":
    connected_devices = get_connected_devices()
    
    if connected_devices:
        print("Connected Bluetooth Devices:")
        for device in connected_devices:
            print(f"Address: {device['address']}, Name: {device['name']}")
            print("\n")
    else:
        print("No connected Bluetooth devices found.")
