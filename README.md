# updizombie

Imagine running python code on a microcontroller without actually running the code on the microcontroller. No compiling, no memory limits, just UART. But it's dead slow.

A short live-demo can be seen on [YouTube](https://youtu.be/_P3E_l8vl1U).

# Working principle
With UPDI, the new generation of ~~Atmel~~ Microchip microcontrollers offer a simple interface to program and debug the chips.

With the great work of mraardvark, [pyupdi](https://github.com/mraardvark/pyupdi), a USB to UART dongle and a resistor is all you need to flash your series-0/1 AVR.

The UPDI protocol allows to read and write the whole address space of the CPU, therefore you theoretically can access all (not confirmed yet) available registers.

Ok, so: "this so ridiculous, it has to work."

And it actually does! Writing 0xFF to address 0x04A7 (PORTF.OUTTGL) with the st command toggles all pins of PORTF on a ATmega4808. Yay!

There is only one caveat: this is done during the execution of the firmware. Great for fuzzing, bad if you don't want to break stuff.

# Halting the CPU

So, you got to halt the CPU. The official can do it and the documentation - no wonder - mentions Go, Stop, Reset and Step Into functionality, but no details on it.

Fair enough. Having an Atmel-ICE and a logic analyzer (even a UART-dongle could do the trick), this shouldn't be a bigger issue.

My first suspicion were the Control and Status Registers, as some of them are not described. And it turned out to be true, register 4 seems to contain the data for flow control: 1 is Stop, 2 is Go. 

Just writing this register isn't all; to use debugging functions, you have to write the correct key (with the equally named function). 
I don't want to give too much away, however, anyone with crypto Obsessive-Compulsive Disorders will not like how On-Chip Debugging is enabled. ;)

# Example

To distinguish what (and who) is currently running on the periperhals, the easiest way is to blink a LED.
The following code is compiled and flashed to the MCU via the usual way:

```c
#define F_CPU 3333333UL
#include <avr/io.h>
#include <util/delay.h>

int main(void)
{
    PORTF.DIRSET = (1 << 4);
    while (1)
    {
        PORTF.OUTTGL = (1 << 4);
        _delay_ms(500);
    }
}
```

With a CPU OSCCFG.FREQSEL = 20 MHz, (and the default clock divider of 6), the LED should blink with 1 Hz.

Now, let's go for zombie mode:

```python
import time
import updi.link
from atmega4808z import ATmega4808

link = updi.link.UpdiDatalink("COM3", "100000")
mcu = ATmega4808(link)

mcu.attach()
time.sleep(5) # LED is static

port = mcu.PORTF
pin = 1 << 4
port.DIRSET = pin

for i in range(0, 50):
    # let PORTF.4 blink as fast as it can
    port.OUTTGL = pin

time.sleep(5) # LED is static again
mcu.detach()
```

The code above will connect to COM3 with 100 kbaud (which is fairly slow, though my setup didn't work above 220 kbaud), attach to the MCU, halt it and wait for 5 seconds.

During this time, the LED should be static (either on or off, depending on the current state).

After that, PORTF.4 is re-initialized as output (not needed if you got the firmware above running) and toggled 50 times.

Since the communication is fairly slow (net vs. gross speed), the blinking is well visible.

After that, the program will again sleep for 5 seconds let the CPU run again. Please note that it won't leave debugging mode.

# Usage & Limitations

The registers can be accessed as properties of the Microcontroller's object as known from the newer hierarchical register scheme from Microchip Studio. Underscore-Properties (like `PORTA_DIR`) are not available.

Please note that those properties are not locally cached and access is slow. Be mindful with accessing the registers as some have special behavior.

In my quick tests, reading `DREIF` from `USART0.STATUS` didn't reflect the actual status. This might be the case for other modules and peripherals.

Also keep in mind to always enable the `DBGCTRL.DBGRUN` for the peripherals you're using.

Cranking up the baudrate may lock up the UPDI interface. Power cycling the MCU usually fixes this issue.

# But why?

Well, why not?

Actually, this can come handy for the colleagues that keep bugging/blaming you that the microcontroller you selected has no JTAG/BSCAN functionality.

Yes, it still not BSCAN but you neither need additional firmware nor hardware nor additional wiring nor free pins for your in-circuit tests.

# Where to go?

For now, the experiment ends here.

In `test.py` you can also find an example how to send data via UART0. 

I didn't bother to test more modules but I had some fun writing a simple converter for the atdf-files that come with Microchip Studio (e.g. `C:/Program Files (x86)/Atmel/Studio/7.0/packs/atmel/ATmega_DFP/<version>/atdf/ATmega4808.atdf`).

Just run `convert_adtf.py -f file.atdf` for a conversion to the corresponding classes to stdout. You should be able to pipe the output to a .py-file.