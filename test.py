import time
import updi.link
from atmega4808z import ATmega4808

demo_blinkled = True
demo_uart = True

link = updi.link.UpdiDatalink("COM3", "200000")
mcu = ATmega4808(link)

mcu.attach()

if demo_blinkled:
    time.sleep(5) # LED is static

    port = mcu.PORTF
    pin = 1 << 4
    port.DIRSET = pin

    for i in range(0, 50):
        # let PORTF.4 blink as fast as it can (which isn't too fast)
        port.OUTTGL = pin

    time.sleep(5) # LED is static again

if demo_uart:

    def uartputstr(uart, s):
        for c in s:
            uart.TXDATAL = ord(c)

    mcu.PORTA.DIRSET = 0x01 # PORTA.0 -> output

    mcu.USART0.CTRLB = 1<<6 # TXEN
    mcu.USART0.CTRLC = 0x03 # 8 bit

    fcpu = 20000000/6
    baudrate = 9600
    baudreg = int((64 * fcpu) / (16 * baudrate))

    mcu.USART0.BAUD = baudreg
    mcu.USART0.DBGCTRL = 1 # continue to run in break mode (important!)

    uartputstr(mcu.USART0, "Hello World!")

mcu.detach()