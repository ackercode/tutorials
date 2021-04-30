import psutil

battery = psutil.sensors_battery()

percent = str(battery.percent)

print(f"Sua bateria tem o total de {+percent}% de bateria")