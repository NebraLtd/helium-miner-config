"""
Add a connection to NetworkManager. You do this by sending a dict to
AddConnection. The dict below was generated with n-m dump on an existing
connection and then anonymised
"""



import NetworkManager
import uuid
from pprint import pprint


example_connection = {
     '802-11-wireless': {'mode': 'infrastructure',
                         'security': '802-11-wireless-security',
                         'ssid': 'Doge'},
     '802-11-wireless-security': {'auth-alg': 'open', 'key-mgmt': 'wpa-psk', "psk": "DogeDoge"},
     'connection': {'id': 'Doge',
                    'type': '802-11-wireless',
                    'uuid': str(uuid.uuid4())},
     'ipv4': {'method': 'auto'},
     'ipv6': {'method': 'auto'}
}

NetworkManager.Settings.AddConnection(example_connection)
