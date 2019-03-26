import dynamixel_sdk as sdk
import glob

def get_ports():
    a = glob.glob("/dev/ttyUSB*") + glob.gob("/dev/ttyusbserial*")
    return a[0]

class Connection:
    def __init__(self, port: str = None], baudrate: int = 1_000_000):
        self.port = port
        self.port_handler = sdk.PortHandler(port)
        self.baudrate = baudrate
        self.opened = False
        if port == None:
            self.ports = get_ports()

    def open_port(self) -> bool:
        ret = self.port_handler.openPort()
        self.opened = ret
        return ret

    def set_baud_rate(self, baud_rate: int) -> bool:
        ret = self.port_handler.setBaudRate(self.baudrate)
        self.opened = ret
        return ret
