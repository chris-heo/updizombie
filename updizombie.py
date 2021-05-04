import updi.link
import updi.constants


def xmega3_regprop(address, length, doc=None):
    def getter(self):
        return self.mcu.reg_read(self.baseaddress + address, length)
    
    def setter(self, value):
        self.mcu.reg_write(self.baseaddress + address, length, value)

    return property(getter, setter, doc=doc)

class Xmega3Debug():
    def __init__(self, link):
        self.link = link

    def attach(self):
        self.link.key(updi.constants.UPDI_KEY_64, b'OCD     ')
        self.link.stcs(4, 0x01)

    def detach(self):
        self.link.stcs(4, 0x02)
        #self.link.stcs(updi.constants.UPDI_CS_CTRLB, 
        #    (1 << updi.constants.UPDI_CTRLB_CCDETDIS_BIT) | 
        #    (1 << updi.constants.UPDI_CTRLB_UPDIDIS_BIT)
        #)

    def reg_write(self, address, length, value):
        if length == 1:
            self.link.st(address, value)
        elif length == 2:
            self.link.st(address, value & 0xFF)
            self.link.st(address + 1, (value >> 8) & 0xFF)
        else:
            raise Exception("value length is not supported")
    
    def reg_read(self, address, length):
        if length == 1:
            return self.link.ld(address)
        elif length == 2:
            result = self.link.ld(address)
            result |= self.link.ld(address + 1) << 8

            return result
        else:
            raise Exception("value length is not supported: %u" % length)
