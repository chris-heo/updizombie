from updizombie import xmega3_regprop, Xmega3Debug

"""Analog Comparator"""
class Xmega3_AC():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    DACREF = xmega3_regprop(0x4, 1, "Referance scale control")
    INTCTRL = xmega3_regprop(0x6, 1, "Interrupt Control")
    MUXCTRLA = xmega3_regprop(0x2, 1, "Mux Control A")
    STATUS = xmega3_regprop(0x7, 1, "Status")

"""Analog to Digital Converter"""
class Xmega3_ADC():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CALIB = xmega3_regprop(0x16, 1, "Calibration")
    COMMAND = xmega3_regprop(0x08, 1, "Command")
    CTRLA = xmega3_regprop(0x00, 1, "Control A")
    CTRLB = xmega3_regprop(0x01, 1, "Control B")
    CTRLC = xmega3_regprop(0x02, 1, "Control C")
    CTRLD = xmega3_regprop(0x03, 1, "Control D")
    CTRLE = xmega3_regprop(0x04, 1, "Control E")
    DBGCTRL = xmega3_regprop(0x0C, 1, "Debug Control")
    EVCTRL = xmega3_regprop(0x09, 1, "Event Control")
    INTCTRL = xmega3_regprop(0x0A, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x0B, 1, "Interrupt Flags")
    MUXPOS = xmega3_regprop(0x06, 1, "Positive mux input")
    RES = xmega3_regprop(0x10, 2, "ADC Accumulator Result")
    SAMPCTRL = xmega3_regprop(0x05, 1, "Sample Control")
    TEMP = xmega3_regprop(0x0D, 1, "Temporary Data")
    WINHT = xmega3_regprop(0x14, 2, "Window comparator high threshold")
    WINLT = xmega3_regprop(0x12, 2, "Window comparator low threshold")

"""Bod interface"""
class Xmega3_BOD():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control B")
    INTCTRL = xmega3_regprop(0x9, 1, "Voltage level monitor interrupt Control")
    INTFLAGS = xmega3_regprop(0xA, 1, "Voltage level monitor interrupt Flags")
    STATUS = xmega3_regprop(0xB, 1, "Voltage level monitor status")
    VLMCTRLA = xmega3_regprop(0x8, 1, "Voltage level monitor Control")

"""Configurable Custom Logic"""
class Xmega3_CCL():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x00, 1, "Control Register A")
    INTCTRL0 = xmega3_regprop(0x05, 1, "Interrupt Control 0")
    INTFLAGS = xmega3_regprop(0x07, 1, "Interrupt Flags")
    LUT0CTRLA = xmega3_regprop(0x08, 1, "LUT Control 0 A")
    LUT0CTRLB = xmega3_regprop(0x09, 1, "LUT Control 0 B")
    LUT0CTRLC = xmega3_regprop(0x0A, 1, "LUT Control 0 C")
    LUT1CTRLA = xmega3_regprop(0x0C, 1, "LUT Control 1 A")
    LUT1CTRLB = xmega3_regprop(0x0D, 1, "LUT Control 1 B")
    LUT1CTRLC = xmega3_regprop(0x0E, 1, "LUT Control 1 C")
    LUT2CTRLA = xmega3_regprop(0x10, 1, "LUT Control 2 A")
    LUT2CTRLB = xmega3_regprop(0x11, 1, "LUT Control 2 B")
    LUT2CTRLC = xmega3_regprop(0x12, 1, "LUT Control 2 C")
    LUT3CTRLA = xmega3_regprop(0x14, 1, "LUT Control 3 A")
    LUT3CTRLB = xmega3_regprop(0x15, 1, "LUT Control 3 B")
    LUT3CTRLC = xmega3_regprop(0x16, 1, "LUT Control 3 C")
    SEQCTRL0 = xmega3_regprop(0x01, 1, "Sequential Control 0")
    SEQCTRL1 = xmega3_regprop(0x02, 1, "Sequential Control 1")
    TRUTH0 = xmega3_regprop(0x0B, 1, "Truth 0")
    TRUTH1 = xmega3_regprop(0x0F, 1, "Truth 1")
    TRUTH2 = xmega3_regprop(0x13, 1, "Truth 2")
    TRUTH3 = xmega3_regprop(0x17, 1, "Truth 3")

"""Clock controller"""
class Xmega3_CLKCTRL():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    MCLKCTRLA = xmega3_regprop(0x00, 1, "MCLK Control A")
    MCLKCTRLB = xmega3_regprop(0x01, 1, "MCLK Control B")
    MCLKLOCK = xmega3_regprop(0x02, 1, "MCLK Lock")
    MCLKSTATUS = xmega3_regprop(0x03, 1, "MCLK Status")
    OSC20MCALIBA = xmega3_regprop(0x11, 1, "OSC20M Calibration A")
    OSC20MCALIBB = xmega3_regprop(0x12, 1, "OSC20M Calibration B")
    OSC20MCTRLA = xmega3_regprop(0x10, 1, "OSC20M Control A")
    OSC32KCTRLA = xmega3_regprop(0x18, 1, "OSC32K Control A")
    XOSC32KCTRLA = xmega3_regprop(0x1C, 1, "XOSC32K Control A")

"""CPU"""
class Xmega3_CPU():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CCP = xmega3_regprop(0x4, 1, "Configuration Change Protection")
    SPH = xmega3_regprop(0xE, 1, "Stack Pointer High")
    SPL = xmega3_regprop(0xD, 1, "Stack Pointer Low")
    SREG = xmega3_regprop(0xF, 1, "Status Register")

"""Interrupt Controller"""
class Xmega3_CPUINT():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    LVL0PRI = xmega3_regprop(0x2, 1, "Interrupt Level 0 Priority")
    LVL1VEC = xmega3_regprop(0x3, 1, "Interrupt Level 1 Priority Vector")
    STATUS = xmega3_regprop(0x1, 1, "Status")

"""CRCSCAN"""
class Xmega3_CRCSCAN():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control B")
    STATUS = xmega3_regprop(0x2, 1, "Status")

"""Event System"""
class Xmega3_EVSYS():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CHANNEL0 = xmega3_regprop(0x10, 1, "Multiplexer Channel 0")
    CHANNEL1 = xmega3_regprop(0x11, 1, "Multiplexer Channel 1")
    CHANNEL2 = xmega3_regprop(0x12, 1, "Multiplexer Channel 2")
    CHANNEL3 = xmega3_regprop(0x13, 1, "Multiplexer Channel 3")
    CHANNEL4 = xmega3_regprop(0x14, 1, "Multiplexer Channel 4")
    CHANNEL5 = xmega3_regprop(0x15, 1, "Multiplexer Channel 5")
    STROBE = xmega3_regprop(0x00, 1, "Channel Strobe")
    USERADC0 = xmega3_regprop(0x28, 1, "User ADC0")
    USERCCLLUT0A = xmega3_regprop(0x20, 1, "User CCL LUT0 Event A")
    USERCCLLUT0B = xmega3_regprop(0x21, 1, "User CCL LUT0 Event B")
    USERCCLLUT1A = xmega3_regprop(0x22, 1, "User CCL LUT1 Event A")
    USERCCLLUT1B = xmega3_regprop(0x23, 1, "User CCL LUT1 Event B")
    USERCCLLUT2A = xmega3_regprop(0x24, 1, "User CCL LUT2 Event A")
    USERCCLLUT2B = xmega3_regprop(0x25, 1, "User CCL LUT2 Event B")
    USERCCLLUT3A = xmega3_regprop(0x26, 1, "User CCL LUT3 Event A")
    USERCCLLUT3B = xmega3_regprop(0x27, 1, "User CCL LUT3 Event B")
    USEREVOUTA = xmega3_regprop(0x29, 1, "User EVOUT Port A")
    USEREVOUTB = xmega3_regprop(0x2A, 1, "User EVOUT Port B")
    USEREVOUTC = xmega3_regprop(0x2B, 1, "User EVOUT Port C")
    USEREVOUTD = xmega3_regprop(0x2C, 1, "User EVOUT Port D")
    USEREVOUTE = xmega3_regprop(0x2D, 1, "User EVOUT Port E")
    USEREVOUTF = xmega3_regprop(0x2E, 1, "User EVOUT Port F")
    USERTCA0 = xmega3_regprop(0x33, 1, "User TCA0")
    USERTCB0 = xmega3_regprop(0x34, 1, "User TCB0")
    USERTCB1 = xmega3_regprop(0x35, 1, "User TCB1")
    USERTCB2 = xmega3_regprop(0x36, 1, "User TCB2")
    USERTCB3 = xmega3_regprop(0x37, 1, "User TCB3")
    USERUSART0 = xmega3_regprop(0x2F, 1, "User USART0")
    USERUSART1 = xmega3_regprop(0x30, 1, "User USART1")
    USERUSART2 = xmega3_regprop(0x31, 1, "User USART2")
    USERUSART3 = xmega3_regprop(0x32, 1, "User USART3")

"""Fuses"""
class Xmega3_FUSE():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    APPEND = xmega3_regprop(0x7, 1, "Application Code Section End")
    BODCFG = xmega3_regprop(0x1, 1, "BOD Configuration")
    BOOTEND = xmega3_regprop(0x8, 1, "Boot Section End")
    OSCCFG = xmega3_regprop(0x2, 1, "Oscillator Configuration")
    SYSCFG0 = xmega3_regprop(0x5, 1, "System Configuration 0")
    SYSCFG1 = xmega3_regprop(0x6, 1, "System Configuration 1")
    WDTCFG = xmega3_regprop(0x0, 1, "Watchdog Configuration")

"""General Purpose IO"""
class Xmega3_GPIO():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    GPIOR0 = xmega3_regprop(0x0, 1, "General Purpose IO Register 0")
    GPIOR1 = xmega3_regprop(0x1, 1, "General Purpose IO Register 1")
    GPIOR2 = xmega3_regprop(0x2, 1, "General Purpose IO Register 2")
    GPIOR3 = xmega3_regprop(0x3, 1, "General Purpose IO Register 3")

"""Lockbit"""
class Xmega3_LOCKBIT():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    LOCKBIT = xmega3_regprop(0x0, 1, "Lock Bits")

"""Non-volatile Memory Controller"""
class Xmega3_NVMCTRL():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    ADDR = xmega3_regprop(0x8, 2, "Address")
    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control B")
    DATA = xmega3_regprop(0x6, 2, "Data")
    INTCTRL = xmega3_regprop(0x3, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x4, 1, "Interrupt Flags")
    STATUS = xmega3_regprop(0x2, 1, "Status")

"""I/O Ports"""
class Xmega3_PORT():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    DIR = xmega3_regprop(0x00, 1, "Data Direction")
    DIRCLR = xmega3_regprop(0x02, 1, "Data Direction Clear")
    DIRSET = xmega3_regprop(0x01, 1, "Data Direction Set")
    DIRTGL = xmega3_regprop(0x03, 1, "Data Direction Toggle")
    IN = xmega3_regprop(0x08, 1, "Input Value")
    INTFLAGS = xmega3_regprop(0x09, 1, "Interrupt Flags")
    OUT = xmega3_regprop(0x04, 1, "Output Value")
    OUTCLR = xmega3_regprop(0x06, 1, "Output Value Clear")
    OUTSET = xmega3_regprop(0x05, 1, "Output Value Set")
    OUTTGL = xmega3_regprop(0x07, 1, "Output Value Toggle")
    PIN0CTRL = xmega3_regprop(0x10, 1, "Pin 0 Control")
    PIN1CTRL = xmega3_regprop(0x11, 1, "Pin 1 Control")
    PIN2CTRL = xmega3_regprop(0x12, 1, "Pin 2 Control")
    PIN3CTRL = xmega3_regprop(0x13, 1, "Pin 3 Control")
    PIN4CTRL = xmega3_regprop(0x14, 1, "Pin 4 Control")
    PIN5CTRL = xmega3_regprop(0x15, 1, "Pin 5 Control")
    PIN6CTRL = xmega3_regprop(0x16, 1, "Pin 6 Control")
    PIN7CTRL = xmega3_regprop(0x17, 1, "Pin 7 Control")
    PORTCTRL = xmega3_regprop(0x0A, 1, "Port Control")

"""Port Multiplexer"""
class Xmega3_PORTMUX():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CCLROUTEA = xmega3_regprop(0x1, 1, "Port Multiplexer CCL")
    EVSYSROUTEA = xmega3_regprop(0x0, 1, "Port Multiplexer EVSYS")
    TCAROUTEA = xmega3_regprop(0x4, 1, "Port Multiplexer TCA")
    TCBROUTEA = xmega3_regprop(0x5, 1, "Port Multiplexer TCB")
    TWISPIROUTEA = xmega3_regprop(0x3, 1, "Port Multiplexer TWI and SPI")
    USARTROUTEA = xmega3_regprop(0x2, 1, "Port Multiplexer USART register A")

"""Reset controller"""
class Xmega3_RSTCTRL():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    RSTFR = xmega3_regprop(0x0, 1, "Reset Flags")
    SWRR = xmega3_regprop(0x1, 1, "Software Reset")

"""Real-Time Counter"""
class Xmega3_RTC():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CALIB = xmega3_regprop(0x06, 1, "Calibration")
    CLKSEL = xmega3_regprop(0x07, 1, "Clock Select")
    CMP = xmega3_regprop(0x0C, 2, "Compare")
    CNT = xmega3_regprop(0x08, 2, "Counter")
    CTRLA = xmega3_regprop(0x00, 1, "Control A")
    DBGCTRL = xmega3_regprop(0x05, 1, "Debug control")
    INTCTRL = xmega3_regprop(0x02, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x03, 1, "Interrupt Flags")
    PER = xmega3_regprop(0x0A, 2, "Period")
    PITCTRLA = xmega3_regprop(0x10, 1, "PIT Control A")
    PITDBGCTRL = xmega3_regprop(0x15, 1, "PIT Debug control")
    PITINTCTRL = xmega3_regprop(0x12, 1, "PIT Interrupt Control")
    PITINTFLAGS = xmega3_regprop(0x13, 1, "PIT Interrupt Flags")
    PITSTATUS = xmega3_regprop(0x11, 1, "PIT Status")
    STATUS = xmega3_regprop(0x01, 1, "Status")
    TEMP = xmega3_regprop(0x04, 1, "Temporary")

"""Signature row"""
class Xmega3_SIGROW():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CHECKSUM1 = xmega3_regprop(0x2F, 1, "CRC Checksum Byte 1")
    DEVICEID0 = xmega3_regprop(0x00, 1, "Device ID Byte 0")
    DEVICEID1 = xmega3_regprop(0x01, 1, "Device ID Byte 1")
    DEVICEID2 = xmega3_regprop(0x02, 1, "Device ID Byte 2")
    OSCCAL16M0 = xmega3_regprop(0x18, 1, "Oscillator Calibration 16 MHz Byte 0")
    OSCCAL16M1 = xmega3_regprop(0x19, 1, "Oscillator Calibration 16 MHz Byte 1")
    OSCCAL20M0 = xmega3_regprop(0x1A, 1, "Oscillator Calibration 20 MHz Byte 0")
    OSCCAL20M1 = xmega3_regprop(0x1B, 1, "Oscillator Calibration 20 MHz Byte 1")
    OSCCAL32K = xmega3_regprop(0x14, 1, "Oscillator Calibration for 32kHz ULP")
    OSC16ERR3V = xmega3_regprop(0x22, 1, "OSC16 error at 3V")
    OSC16ERR5V = xmega3_regprop(0x23, 1, "OSC16 error at 5V")
    OSC20ERR3V = xmega3_regprop(0x24, 1, "OSC20 error at 3V")
    OSC20ERR5V = xmega3_regprop(0x25, 1, "OSC20 error at 5V")
    SERNUM0 = xmega3_regprop(0x03, 1, "Serial Number Byte 0")
    SERNUM1 = xmega3_regprop(0x04, 1, "Serial Number Byte 1")
    SERNUM2 = xmega3_regprop(0x05, 1, "Serial Number Byte 2")
    SERNUM3 = xmega3_regprop(0x06, 1, "Serial Number Byte 3")
    SERNUM4 = xmega3_regprop(0x07, 1, "Serial Number Byte 4")
    SERNUM5 = xmega3_regprop(0x08, 1, "Serial Number Byte 5")
    SERNUM6 = xmega3_regprop(0x09, 1, "Serial Number Byte 6")
    SERNUM7 = xmega3_regprop(0x0A, 1, "Serial Number Byte 7")
    SERNUM8 = xmega3_regprop(0x0B, 1, "Serial Number Byte 8")
    SERNUM9 = xmega3_regprop(0x0C, 1, "Serial Number Byte 9")
    TEMPSENSE0 = xmega3_regprop(0x20, 1, "Temperature Sensor Calibration Byte 0")
    TEMPSENSE1 = xmega3_regprop(0x21, 1, "Temperature Sensor Calibration Byte 1")

"""Sleep Controller"""
class Xmega3_SLPCTRL():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control")

"""Serial Peripheral Interface"""
class Xmega3_SPI():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control B")
    DATA = xmega3_regprop(0x4, 1, "Data")
    INTCTRL = xmega3_regprop(0x2, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x3, 1, "Interrupt Flags")

"""System Configuration Registers"""
class Xmega3_SYSCFG():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    EXTBRK = xmega3_regprop(0x02, 1, "External Break")
    OCDM = xmega3_regprop(0x18, 1, "OCD Message Register")
    OCDMS = xmega3_regprop(0x19, 1, "OCD Message Status")
    REVID = xmega3_regprop(0x01, 1, "Revision ID")

"""16-bit Timer/Counter Type A"""
class Xmega3_TCA():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CMP0 = xmega3_regprop(0x28, 2, "Compare 0")
    CMP0BUF = xmega3_regprop(0x38, 2, "Compare 0 Buffer")
    CMP1 = xmega3_regprop(0x2A, 2, "Compare 1")
    CMP1BUF = xmega3_regprop(0x3A, 2, "Compare 1 Buffer")
    CMP2 = xmega3_regprop(0x2C, 2, "Compare 2")
    CMP2BUF = xmega3_regprop(0x3C, 2, "Compare 2 Buffer")
    CNT = xmega3_regprop(0x20, 2, "Count")
    CTRLA = xmega3_regprop(0x00, 1, "Control A")
    CTRLB = xmega3_regprop(0x01, 1, "Control B")
    CTRLC = xmega3_regprop(0x02, 1, "Control C")
    CTRLD = xmega3_regprop(0x03, 1, "Control D")
    CTRLECLR = xmega3_regprop(0x04, 1, "Control E Clear")
    CTRLESET = xmega3_regprop(0x05, 1, "Control E Set")
    CTRLFCLR = xmega3_regprop(0x06, 1, "Control F Clear")
    CTRLFSET = xmega3_regprop(0x07, 1, "Control F Set")
    DBGCTRL = xmega3_regprop(0x0E, 1, "Degbug Control")
    EVCTRL = xmega3_regprop(0x09, 1, "Event Control")
    INTCTRL = xmega3_regprop(0x0A, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x0B, 1, "Interrupt Flags")
    PER = xmega3_regprop(0x26, 2, "Period")
    PERBUF = xmega3_regprop(0x36, 2, "Period Buffer")
    TEMP = xmega3_regprop(0x0F, 1, "Temporary data for 16-bit Access")
    CTRLA = xmega3_regprop(0x00, 1, "Control A")
    CTRLB = xmega3_regprop(0x01, 1, "Control B")
    CTRLC = xmega3_regprop(0x02, 1, "Control C")
    CTRLD = xmega3_regprop(0x03, 1, "Control D")
    CTRLECLR = xmega3_regprop(0x04, 1, "Control E Clear")
    CTRLESET = xmega3_regprop(0x05, 1, "Control E Set")
    DBGCTRL = xmega3_regprop(0x0E, 1, "Degbug Control")
    HCMP0 = xmega3_regprop(0x29, 1, "High Compare")
    HCMP1 = xmega3_regprop(0x2B, 1, "High Compare")
    HCMP2 = xmega3_regprop(0x2D, 1, "High Compare")
    HCNT = xmega3_regprop(0x21, 1, "High Count")
    HPER = xmega3_regprop(0x27, 1, "High Period")
    INTCTRL = xmega3_regprop(0x0A, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x0B, 1, "Interrupt Flags")
    LCMP0 = xmega3_regprop(0x28, 1, "Low Compare")
    LCMP1 = xmega3_regprop(0x2A, 1, "Low Compare")
    LCMP2 = xmega3_regprop(0x2C, 1, "Low Compare")
    LCNT = xmega3_regprop(0x20, 1, "Low Count")
    LPER = xmega3_regprop(0x26, 1, "Low Period")

"""16-bit Timer Type B"""
class Xmega3_TCB():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CCMP = xmega3_regprop(0xC, 2, "Compare or Capture")
    CNT = xmega3_regprop(0xA, 2, "Count")
    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control Register B")
    DBGCTRL = xmega3_regprop(0x8, 1, "Debug Control")
    EVCTRL = xmega3_regprop(0x4, 1, "Event Control")
    INTCTRL = xmega3_regprop(0x5, 1, "Interrupt Control")
    INTFLAGS = xmega3_regprop(0x6, 1, "Interrupt Flags")
    STATUS = xmega3_regprop(0x7, 1, "Status")
    TEMP = xmega3_regprop(0x9, 1, "Temporary Value")

"""Two-Wire Interface"""
class Xmega3_TWI():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    DBGCTRL = xmega3_regprop(0x2, 1, "Debug Control Register")
    DUALCTRL = xmega3_regprop(0x1, 1, "Dual Control")
    MADDR = xmega3_regprop(0x7, 1, "Master Address")
    MBAUD = xmega3_regprop(0x6, 1, "Master Baurd Rate Control")
    MCTRLA = xmega3_regprop(0x3, 1, "Master Control A")
    MCTRLB = xmega3_regprop(0x4, 1, "Master Control B")
    MDATA = xmega3_regprop(0x8, 1, "Master Data")
    MSTATUS = xmega3_regprop(0x5, 1, "Master Status")
    SADDR = xmega3_regprop(0xC, 1, "Slave Address")
    SADDRMASK = xmega3_regprop(0xE, 1, "Slave Address Mask")
    SCTRLA = xmega3_regprop(0x9, 1, "Slave Control A")
    SCTRLB = xmega3_regprop(0xA, 1, "Slave Control B")
    SDATA = xmega3_regprop(0xD, 1, "Slave Data")
    SSTATUS = xmega3_regprop(0xB, 1, "Slave Status")

"""Universal Synchronous and Asynchronous Receiver and Transmitter"""
class Xmega3_USART():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    BAUD = xmega3_regprop(0x8, 2, "Baud Rate")
    CTRLA = xmega3_regprop(0x5, 1, "Control A")
    CTRLB = xmega3_regprop(0x6, 1, "Control B")
    CTRLC = xmega3_regprop(0x7, 1, "Control C")
    CTRLD = xmega3_regprop(0xA, 1, "Control D")
    DBGCTRL = xmega3_regprop(0xB, 1, "Debug Control")
    EVCTRL = xmega3_regprop(0xC, 1, "Event Control")
    RXDATAH = xmega3_regprop(0x1, 1, "Receive Data High Byte")
    RXDATAL = xmega3_regprop(0x0, 1, "Receive Data Low Byte")
    RXPLCTRL = xmega3_regprop(0xE, 1, "IRCOM Receiver Pulse Length Control")
    STATUS = xmega3_regprop(0x4, 1, "Status")
    TXDATAH = xmega3_regprop(0x3, 1, "Transmit Data High Byte")
    TXDATAL = xmega3_regprop(0x2, 1, "Transmit Data Low Byte")
    TXPLCTRL = xmega3_regprop(0xD, 1, "IRCOM Transmitter Pulse Length Control")

"""User Row"""
class Xmega3_USERROW():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    USERROW0 = xmega3_regprop(0x00, 1, "User Row Byte 0")
    USERROW1 = xmega3_regprop(0x01, 1, "User Row Byte 1")
    USERROW2 = xmega3_regprop(0x02, 1, "User Row Byte 2")
    USERROW3 = xmega3_regprop(0x03, 1, "User Row Byte 3")
    USERROW4 = xmega3_regprop(0x04, 1, "User Row Byte 4")
    USERROW5 = xmega3_regprop(0x05, 1, "User Row Byte 5")
    USERROW6 = xmega3_regprop(0x06, 1, "User Row Byte 6")
    USERROW7 = xmega3_regprop(0x07, 1, "User Row Byte 7")
    USERROW8 = xmega3_regprop(0x08, 1, "User Row Byte 8")
    USERROW9 = xmega3_regprop(0x09, 1, "User Row Byte 9")
    USERROW10 = xmega3_regprop(0x0A, 1, "User Row Byte 10")
    USERROW11 = xmega3_regprop(0x0B, 1, "User Row Byte 11")
    USERROW12 = xmega3_regprop(0x0C, 1, "User Row Byte 12")
    USERROW13 = xmega3_regprop(0x0D, 1, "User Row Byte 13")
    USERROW14 = xmega3_regprop(0x0E, 1, "User Row Byte 14")
    USERROW15 = xmega3_regprop(0x0F, 1, "User Row Byte 15")
    USERROW16 = xmega3_regprop(0x10, 1, "User Row Byte 16")
    USERROW17 = xmega3_regprop(0x11, 1, "User Row Byte 17")
    USERROW18 = xmega3_regprop(0x12, 1, "User Row Byte 18")
    USERROW19 = xmega3_regprop(0x13, 1, "User Row Byte 19")
    USERROW20 = xmega3_regprop(0x14, 1, "User Row Byte 20")
    USERROW21 = xmega3_regprop(0x15, 1, "User Row Byte 21")
    USERROW22 = xmega3_regprop(0x16, 1, "User Row Byte 22")
    USERROW23 = xmega3_regprop(0x17, 1, "User Row Byte 23")
    USERROW24 = xmega3_regprop(0x18, 1, "User Row Byte 24")
    USERROW25 = xmega3_regprop(0x19, 1, "User Row Byte 25")
    USERROW26 = xmega3_regprop(0x1A, 1, "User Row Byte 26")
    USERROW27 = xmega3_regprop(0x1B, 1, "User Row Byte 27")
    USERROW28 = xmega3_regprop(0x1C, 1, "User Row Byte 28")
    USERROW29 = xmega3_regprop(0x1D, 1, "User Row Byte 29")
    USERROW30 = xmega3_regprop(0x1E, 1, "User Row Byte 30")
    USERROW31 = xmega3_regprop(0x1F, 1, "User Row Byte 31")
    USERROW32 = xmega3_regprop(0x20, 1, "User Row Byte 32")
    USERROW33 = xmega3_regprop(0x21, 1, "User Row Byte 33")
    USERROW34 = xmega3_regprop(0x22, 1, "User Row Byte 34")
    USERROW35 = xmega3_regprop(0x23, 1, "User Row Byte 35")
    USERROW36 = xmega3_regprop(0x24, 1, "User Row Byte 36")
    USERROW37 = xmega3_regprop(0x25, 1, "User Row Byte 37")
    USERROW38 = xmega3_regprop(0x26, 1, "User Row Byte 38")
    USERROW39 = xmega3_regprop(0x27, 1, "User Row Byte 39")
    USERROW40 = xmega3_regprop(0x28, 1, "User Row Byte 40")
    USERROW41 = xmega3_regprop(0x29, 1, "User Row Byte 41")
    USERROW42 = xmega3_regprop(0x2A, 1, "User Row Byte 42")
    USERROW43 = xmega3_regprop(0x2B, 1, "User Row Byte 43")
    USERROW44 = xmega3_regprop(0x2C, 1, "User Row Byte 44")
    USERROW45 = xmega3_regprop(0x2D, 1, "User Row Byte 45")
    USERROW46 = xmega3_regprop(0x2E, 1, "User Row Byte 46")
    USERROW47 = xmega3_regprop(0x2F, 1, "User Row Byte 47")
    USERROW48 = xmega3_regprop(0x30, 1, "User Row Byte 48")
    USERROW49 = xmega3_regprop(0x31, 1, "User Row Byte 49")
    USERROW50 = xmega3_regprop(0x32, 1, "User Row Byte 50")
    USERROW51 = xmega3_regprop(0x33, 1, "User Row Byte 51")
    USERROW52 = xmega3_regprop(0x34, 1, "User Row Byte 52")
    USERROW53 = xmega3_regprop(0x35, 1, "User Row Byte 53")
    USERROW54 = xmega3_regprop(0x36, 1, "User Row Byte 54")
    USERROW55 = xmega3_regprop(0x37, 1, "User Row Byte 55")
    USERROW56 = xmega3_regprop(0x38, 1, "User Row Byte 56")
    USERROW57 = xmega3_regprop(0x39, 1, "User Row Byte 57")
    USERROW58 = xmega3_regprop(0x3A, 1, "User Row Byte 58")
    USERROW59 = xmega3_regprop(0x3B, 1, "User Row Byte 59")
    USERROW60 = xmega3_regprop(0x3C, 1, "User Row Byte 60")
    USERROW61 = xmega3_regprop(0x3D, 1, "User Row Byte 61")
    USERROW62 = xmega3_regprop(0x3E, 1, "User Row Byte 62")
    USERROW63 = xmega3_regprop(0x3F, 1, "User Row Byte 63")

"""Virtual Ports"""
class Xmega3_VPORT():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    DIR = xmega3_regprop(0x0, 1, "Data Direction")
    IN = xmega3_regprop(0x2, 1, "Input Value")
    INTFLAGS = xmega3_regprop(0x3, 1, "Interrupt Flags")
    OUT = xmega3_regprop(0x1, 1, "Output Value")

"""Voltage reference"""
class Xmega3_VREF():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    CTRLB = xmega3_regprop(0x1, 1, "Control B")

"""Watch-Dog Timer"""
class Xmega3_WDT():
    def __init__(self, mcu, baseaddress):
        self.mcu = mcu
        self.baseaddress = baseaddress

    CTRLA = xmega3_regprop(0x0, 1, "Control A")
    STATUS = xmega3_regprop(0x1, 1, "Status")

class ATmega4808(Xmega3Debug):

    def __init__(self, link):
        super().__init__(link)
        self.AC0 = Xmega3_AC(self, 0x0680)
        self.ADC0 = Xmega3_ADC(self, 0x0600)
        self.BOD = Xmega3_BOD(self, 0x0080)
        self.CCL = Xmega3_CCL(self, 0x01C0)
        self.CLKCTRL = Xmega3_CLKCTRL(self, 0x0060)
        self.CPU = Xmega3_CPU(self, 0x0030)
        self.CPUINT = Xmega3_CPUINT(self, 0x0110)
        self.CRCSCAN = Xmega3_CRCSCAN(self, 0x0120)
        self.EVSYS = Xmega3_EVSYS(self, 0x0180)
        self.FUSE = Xmega3_FUSE(self, 0x1280)
        self.GPIO = Xmega3_GPIO(self, 0x001C)
        self.LOCKBIT = Xmega3_LOCKBIT(self, 0x128A)
        self.NVMCTRL = Xmega3_NVMCTRL(self, 0x1000)
        self.PORTA = Xmega3_PORT(self, 0x0400)
        self.PORTB = Xmega3_PORT(self, 0x0420)
        self.PORTC = Xmega3_PORT(self, 0x0440)
        self.PORTD = Xmega3_PORT(self, 0x0460)
        self.PORTE = Xmega3_PORT(self, 0x0480)
        self.PORTF = Xmega3_PORT(self, 0x04A0)
        self.PORTMUX = Xmega3_PORTMUX(self, 0x05E0)
        self.RSTCTRL = Xmega3_RSTCTRL(self, 0x0040)
        self.RTC = Xmega3_RTC(self, 0x0140)
        self.SIGROW = Xmega3_SIGROW(self, 0x1100)
        self.SLPCTRL = Xmega3_SLPCTRL(self, 0x0050)
        self.SPI0 = Xmega3_SPI(self, 0x08C0)
        self.SYSCFG = Xmega3_SYSCFG(self, 0x0F00)
        self.TCA0 = Xmega3_TCA(self, 0x0A00)
        self.TCB0 = Xmega3_TCB(self, 0x0A80)
        self.TCB1 = Xmega3_TCB(self, 0x0A90)
        self.TCB2 = Xmega3_TCB(self, 0x0AA0)
        self.TWI0 = Xmega3_TWI(self, 0x08A0)
        self.USART0 = Xmega3_USART(self, 0x0800)
        self.USART1 = Xmega3_USART(self, 0x0820)
        self.USART2 = Xmega3_USART(self, 0x0840)
        self.USERROW = Xmega3_USERROW(self, 0x1300)
        self.VPORTA = Xmega3_VPORT(self, 0x0000)
        self.VPORTB = Xmega3_VPORT(self, 0x0004)
        self.VPORTC = Xmega3_VPORT(self, 0x0008)
        self.VPORTD = Xmega3_VPORT(self, 0x000C)
        self.VPORTE = Xmega3_VPORT(self, 0x0010)
        self.VPORTF = Xmega3_VPORT(self, 0x0014)
        self.VREF = Xmega3_VREF(self, 0x00A0)
        self.WDT = Xmega3_WDT(self, 0x0100)
