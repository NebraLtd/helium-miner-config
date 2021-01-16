import dbus

miner_bus = dbus.SystemBus()
miner_object = miner_bus.get_object('com.helium.Miner', '/')
miner_interface = dbus.Interface(miner_object, 'com.helium.Miner')
miner_interface.P2PStatus()
