"""
Display detailed information about currently active connections.
"""
import NetworkManager
from pprint import pprint


for conn in NetworkManager.NetworkManager.ActiveConnections:
    settings = conn.Connection.GetSettings()

    devices = ""
    if conn.Devices:
        for x in conn.Devices:
            print(x.Interface)

            print(settings['connection']['id'])
