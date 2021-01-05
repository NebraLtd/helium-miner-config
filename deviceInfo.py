
from service import Application, Service, Characteristic, Descriptor

class DeviceInformationService(Service):
    DEVINFO_SVC_UUID = "180A"

    def __init__(self, index):

        Service.__init__(self, index, self.DEVINFO_SVC_UUID, True)
        self.add_characteristic(ManufactureNameCharacteristic(self))
        self.add_characteristic(FirmwareRevisionCharacteristic(self))
        self.add_characteristic(SerialNumberCharacteristic(self))

class ManufactureNameCharacteristic(Characteristic):
    MANUFACTURE_NAME_CHARACTERISTIC_UUID = "2A29"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.MANUFACTURE_NAME_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "Nebra LTD."
        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value


class FirmwareRevisionCharacteristic(Characteristic):
    FIRMWARE_REVISION_CHARACTERISTIC_UUID = "2A26"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.FIRMWARE_REVISION_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "2021.01.05"
        for c in val:
            value.append(dbus.Byte(c.encode()))

        return value

class SerialNumberCharacteristic(Characteristic):
    SERIAL_NUMBER_CHARACTERISTIC_UUID = "2A25"

    def __init__(self, service):
        Characteristic.__init__(
                self, self.SERIAL_NUMBER_CHARACTERISTIC_UUID,
                ["read"], service)

    def ReadValue(self, options):
        value = []
        val = "F04CD555B5D9"

        for c in val:
            value.append(dbus.Byte(c.encode()))
        return value
