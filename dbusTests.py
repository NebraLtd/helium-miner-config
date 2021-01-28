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
dbusArrayTest = 

addMinerRequest = miner_interface.AddGateway(addGatewayDetails.owner,
addGatewayDetails.amount,addGatewayDetails.fee,addGatewayDetails.payer)

print(addMinerRequest)
