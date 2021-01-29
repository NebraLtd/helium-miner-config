import nmcli

nmcli.disable_use_sudo()

for network in nmcli.device.wifi():
    if(network.ssid != "--"):
        print(network.ssid)
