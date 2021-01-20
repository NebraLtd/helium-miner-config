import dbus
from time import sleep

miner_bus = dbus.SystemBus()
miner_object = miner_bus.get_object('com.helium.Miner', '/')
sleep(0.1)
miner_interface = dbus.Interface(miner_object, 'com.helium.Miner')
sleep(0.1)
print(miner_interface.P2PStatus())
sleep(0.1)
miner_interface.AddGateway("",1,65000,"14fzfjFcHpDR1rTH8BNPvSi5dKBbgxaDnmsVPbCjuq9ENjpZbxh")
sleep(0.1)
print(miner_interface.AssertLocation())
