import bluetooth

def get_connected_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True, device_id=-1, lookup_oui=True, device_class=0, duration=8, lookup_oui_in_name=True, lookup_oui_in_class=True)
    
    connected_devices = []
    
    for addr, name, _ in nearby_devices:
        services = bluetooth.find_service(address=addr)
        if services:
            connected_devices.append({"address": addr, "name": name, "services": services})
    
    return connected_devices

if __name__ == "__main__":
    connected_devices = get_connected_devices()
    
    if connected_devices:
        print("Connected Bluetooth Devices:")
        for device in connected_devices:
            print(f"Address: {device['address']}, Name: {device['name']}")
            if device['services']:
                print("Services:")
                for service in device['services']:
                    print(f"  - {service['name']} ({service['host']}:{service['port']})")
            print("\n")
    else:
        print("No connected Bluetooth devices found.")
