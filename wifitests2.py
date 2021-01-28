import re
import Optional
class Device:
    device: str
    device_type: str
    state: str
    connection: Optional[str]

    def to_json(self):
        return {
            'device': self.device,
            'device_type': self.device_type,
            'state': self.state,
            'connection': self.connection
        }

    @classmethod
    def parse(cls, text: str) -> Device:
        m = re.search(r'^(\S*)\s+(\S*)\s+(\S*)\s+([\S\s]+)\s*$', text)
        if m:
            device, device_type, state, conn = m.groups()
            conn = conn.strip()
            connection = conn if conn != '--' else None
            return Device(device, device_type, state, connection)
        raise ValueError('Parse failed [%s]' % text)
