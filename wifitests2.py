import re

text = "        SilverSurfers   Infra  3     195 Mbit/s  100     ****  WPA2    "

m = re.search(r'^(\S*)\s+(\S*)\s+(\S*)\s+([\S\s]+)\s*$', text)
print(m)
if m:
    device, device_type, state, conn = m.groups()
    conn = conn.strip()
    connection = conn if conn != '--' else None
    print(connection)

#text = "        Virgin Media    Infra  6     130 Mbit/s  39      **    WPA2 802.1X "

text = "        Virgin Media                    Infra  1     130 Mbit/s  59      ▂▄▆_  WPA2 802.1X "

m = re.search(r'^(\S*)\s+(\S*)\s+(\S*)\s+([\S\s]+)\s*$', text)
print(m)
if m:
    device, device_type, state, conn = m.groups()
    conn = conn.strip()
    connection = conn if conn != '--' else None
    print(connection)
