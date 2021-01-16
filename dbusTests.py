import dbus

miner_bus = dbus.SystemBus()
miner_object = miner_bus.get_object('org.freedesktop.NetworkManager',
                       '/org/freedesktop/NetworkManager/Devices/eth0')
