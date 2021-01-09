import wifi_services_pb2
from pprint import pprint
import dbus

wifiSsids = wifi_services_pb2.wifi_services_v1()

wifiSsids.services.append("RTK")
wifiSsids.services.append("RTK2")
wifiSsids.services.append("SKYXTWIW")

pprint(wifiSsids.SerializeToString().hex())

value = []
val = wifiSsids.SerializeToString()

for c in val:
    value.append(dbus.Byte(c))

pprint(value)