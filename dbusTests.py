import dbus

miner_bus = dbus.SystemBus()
miner_object = bus.get_object('org.freedesktop.NetworkManager',
                       '/org/freedesktop/NetworkManager/Devices/eth0')
