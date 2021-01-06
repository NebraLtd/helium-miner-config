#!/usr/bin/python3

import dbus, uuid

from advertisement import Advertisement
from service import Application, Service, Characteristic, Descriptor
import uuids

GATT_CHRC_IFACE = "org.bluez.GattCharacteristic1"
NOTIFY_TIMEOUT = 5000


class ConfigAdvertisement(Advertisement):
    def __init__(self, index):
        Advertisement.__init__(self, index, "peripheral")
        macAddressTrimmed = open("/sys/class/net/eth0/address").readline().strip().replace(":","")[-4:].upper()
        localName = "Helium Hotspot %s" % (macAddressTrimmed)
        self.add_local_name(localName)
        self.include_tx_power = True
        self.service_uuids = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"

class DeviceInformationService(Service):
    def __init__(self, index):
        Service.__init__(self, index, uuids.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufactureNameCharacteristic(self))
        self.add_characteristic(FirmwareRevisionCharacteristic(self))
        self.add_characteristic(SerialNumberCharacteristic(self))

class ManufactureNameCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.MANUFACTURE_NAME_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "Nebra LTD."
        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class FirmwareRevisionCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.FIRMWARE_REVISION_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        #CHANGE THIS LINE FOR NEW VERSIONS
        val = "2021.01.06.01"
        for c in val:
            value.append(dbus.Byte(c.encode()))

        return value

class SerialNumberCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = open("/sys/class/net/eth0/address").readline().strip().replace(":","")

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class HeliumService(Service):
    DEVINFO_SVC_UUID = "0fda92b2-44a2-4af2-84f5-fa682baa2b8d"

    def __init__(self, index):

        Service.__init__(self, index, self.DEVINFO_SVC_UUID, True)
        self.add_characteristic(OnboardingKeyCharacteristic(self))
        self.add_characteristic(PublicKeyCharacteristic(self))
        self.add_characteristic(WiFiServicesCharacteristic(self))
        self.add_characteristic(DiagnosticsCharacteristic(self))
        self.add_characteristic(MacAddressCharacteristic(self))
        self.add_characteristic(LightsCharacteristic(self))
        self.add_characteristic(WiFiSSIDCharacteristic(self))
        self.add_characteristic(AssertLocationCharacteristic(self))
        self.add_characteristic(AddGatewayCharacteristic(self))
        self.add_characteristic(WiFiConnectCharacteristic(self))
        self.add_characteristic(EthernetOnlineCharacteristic(self))

class OnboardingKeyCharacteristic(Characteristic):
    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.ONBOARDING_KEY_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(OnboardingKeyDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "11TqqVzycXK5k49bXbmcUcSne91krq7v3VSQCfDXr" #PLACEHOLDER

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class OnboardingKeyDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.ONBOARDING_KEY_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class PublicKeyCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.PUBLIC_KEY_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(PublicKeyDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "117ei8D1Bk2kYqWNjSFuLgg3BrtTNSTi2tt14LRUFgt" #PLACEHOLDER

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class PublicKeyDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.PUBLIC_KEY_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiServicesCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.WIFI_SERVICES_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WiFiServicesDescriptor(self))
        self.add_descriptor(utf8Format(self))


    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class WiFiServicesDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.WIFI_SERVICES_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class DiagnosticsCharacteristic(Characteristic):
    #Returns proto of eth, wifi, fw, ip, p2pstatus

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.DIAGNOSTICS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(DiagnosticsDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []

        dbusInterface.P2PStatus()
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class DiagnosticsDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.DIAGNOSTICS_VALUE
        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class MacAddressCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.MAC_ADDRESS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(MacAddressDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = open("/sys/class/net/eth0/address").readline().strip().replace(":","")

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class MacAddressDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.MAC_ADDRESS_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class LightsCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.LIGHTS_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(LightsDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "false"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class LightsDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.LIGHTS_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiSSIDCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.WIFI_SSID_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WiFiSSIDDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class WiFiSSIDDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.WIFI_SSID_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class AssertLocationCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.ASSERT_LOCATION_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(AssertLocationDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class AssertLocationDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.ASSERT_LOCATION_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class AddGatewayCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.ADD_GATEWAY_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(AddGatewayDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class AddGatewayDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.ADD_GATEWAY_KEY_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class WiFiConnectCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.WIFI_CONNECT_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(WiFiConnectDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
class WiFiConnectDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.WIFI_CONNECT_KEY_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class EthernetOnlineCharacteristic(Characteristic):

    def __init__(self, service):
        Characteristic.__init__(
                self, uuids.ETHERNET_ONLINE_CHARACTERISTIC_UUID,
                ["read"], service)
        self.add_descriptor(EthernetOnlineDescriptor(self))
        self.add_descriptor(utf8Format(self))

    def ReadValue(self, options):
        value = []

        val = "false"

        if(open("/sys/class/net/eth0/carrier").readline().strip()== "1" or open("/sys/class/net/wlan0/carrier").readline().strip()== "1"):
            val = "true"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value

class EthernetOnlineDescriptor(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.USER_DESC_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        desc = uuids.ETHERNET_ONLINE_VALUE

        for c in desc:
            value.append(dbus.Byte(c.encode()))
        return value

class utf8Format(Descriptor):

    def __init__(self, characteristic):
        Descriptor.__init__(
                self, uuids.PRESENTATION_FORMAT_DESCRIPTOR_UUID,
                ["read"],
                characteristic)
    def ReadValue(self, options):
        value = []
        value.append(dbus.Byte(0x19))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x01))
        value.append(dbus.Byte(0x00))
        value.append(dbus.Byte(0x00))

        return value

app = Application()
app.add_service(DeviceInformationService(0))
app.add_service(HeliumService(1))
app.register()


adv = ConfigAdvertisement(0)
adv.register()

try:
    app.run()
except KeyboardInterrupt:
    app.quit()
