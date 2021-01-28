import nmcli
for network in nmcli.device.wifi():
    if(network.ssid != "--"):
        print(network.ssid)
