from envirophat import light, weather, leds
import requests

leds.off()

lux = light.light()
temp = weather.temperature()
press = weather.pressure(unit='hPa')

# Switches Domo
# Lux: 22
# Temp: 23
# Baro: 24

payload1 = {'svalue': lux}
payload2 = {'svalue': int(temp)}
payload3 = {'svalue': int(press)}

requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=22', params=payload1)
requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=23', params=payload2)
requests.get('http://192.168.1.101:8080/json.htm?type=command&param=udevice&idx=24', params=payload3)

