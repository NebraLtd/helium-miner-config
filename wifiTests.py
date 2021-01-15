import nmcli
from pprint import pprint

try:
    #print(nmcli.connection())
    print(nmcli.device.show('wlan0')['GENERAL.STATE'].split(" ")[0])
    #pprint(nmcli.device.wifi() )

    #nmcli.connection.delete('Doge')
except Exception as e:
    print(e)
