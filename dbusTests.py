import dbus
from time import sleep
import add_gateway_pb2, assert_location_pb2, diagnostics_pb2, wifi_connect_pb2, wifi_remove_pb2, wifi_services_pb2


miner_bus = dbus.SystemBus()
miner_object = miner_bus.get_object('com.helium.Miner', '/')
sleep(0.1)
miner_interface = dbus.Interface(miner_object, 'com.helium.Miner')
sleep(0.1)
addGatewayDetails = add_gateway_pb2.add_gateway_v1()

#miner_interface.AddGateway("",1,65000,"14fzfjFcHpDR1rTH8BNPvSi5dKBbgxaDnmsVPbCjuq9ENjpZbxh")
dbusArrayTest = dbus.Array([dbus.Byte(10), dbus.Byte(51), dbus.Byte(49), dbus.Byte(51), dbus.Byte(109), dbus.Byte(118), dbus.Byte(105), dbus.Byte(111), dbus.Byte(51), dbus.Byte(55), dbus.Byte(71), dbus.Byte(103), dbus.Byte(90), dbus.Byte(75), dbus.Byte(110), dbus.Byte(68), dbus.Byte(70), dbus.Byte(67), dbus.Byte(110), dbus.Byte(109), dbus.Byte(119), dbus.Byte(85), dbus.Byte(80), dbus.Byte(103), dbus.Byte(66), dbus.Byte(51), dbus.Byte(66), dbus.Byte(52), dbus.Byte(112), dbus.Byte(66), dbus.Byte(98), dbus.Byte(114), dbus.Byte(117), dbus.Byte(84), dbus.Byte(70), dbus.Byte(88), dbus.Byte(104), dbus.Byte(67), dbus.Byte(100), dbus.Byte(86), dbus.Byte(107), dbus.Byte(85), dbus.Byte(57), dbus.Byte(111), dbus.Byte(77), dbus.Byte(82), dbus.Byte(99), dbus.Byte(112), dbus.Byte(105), dbus.Byte(88), dbus.Byte(84), dbus.Byte(103), dbus.Byte(81), dbus.Byte(16), dbus.Byte(1), dbus.Byte(24), dbus.Byte(232), dbus.Byte(251), dbus.Byte(3), dbus.Byte(34), dbus.Byte(51), dbus.Byte(49), dbus.Byte(52), dbus.Byte(102), dbus.Byte(122), dbus.Byte(102), dbus.Byte(106), dbus.Byte(70), dbus.Byte(99), dbus.Byte(72), dbus.Byte(112), dbus.Byte(68), dbus.Byte(82), dbus.Byte(49), dbus.Byte(114), dbus.Byte(84), dbus.Byte(72), dbus.Byte(56), dbus.Byte(66), dbus.Byte(78), dbus.Byte(80), dbus.Byte(118), dbus.Byte(83), dbus.Byte(105), dbus.Byte(53), dbus.Byte(100), dbus.Byte(75), dbus.Byte(66), dbus.Byte(98), dbus.Byte(103), dbus.Byte(120), dbus.Byte(97), dbus.Byte(68), dbus.Byte(110), dbus.Byte(109), dbus.Byte(115), dbus.Byte(86), dbus.Byte(80), dbus.Byte(98), dbus.Byte(67), dbus.Byte(106), dbus.Byte(117), dbus.Byte(113), dbus.Byte(57), dbus.Byte(69), dbus.Byte(78), dbus.Byte(106), dbus.Byte(112), dbus.Byte(90), dbus.Byte(98), dbus.Byte(120), dbus.Byte(104)], signature=dbus.Signature('y'))
addGatewayDetails.ParseFromString(bytes(dbusArrayTest))
print(str(addGatewayDetails[0]))

addMinerRequest = miner_interface.AddGateway(addGatewayDetails["owner"],
addGatewayDetails["amount"],addGatewayDetails["fee"],addGatewayDetails["payer"])

print(addMinerRequest)
