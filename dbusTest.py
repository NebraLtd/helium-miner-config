import dbus

bus = dbus.SystemBus()

objTest = bus.get_object("com.helium.Miner", "/")
intTest = dbus.Interface(objTest, "com.helium.Miner")

print(intTest.AddGateway())
