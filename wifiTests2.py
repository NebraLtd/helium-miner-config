import nmcli
from pprint import pprint

try:
    print(nmcli.connection())
    print(nmcli.device())
    #pprint(nmcli.device.wifi())
    #
    #print(nmcli.general())

    #nmcli.device.wifi_connect('Doge', 'DogeDogeDoge')

    print(nmcli.connection())
    print(nmcli.device.wifi() )

    #nmcli.connection.delete('Doge')
except Exception as e:
    print(e)
