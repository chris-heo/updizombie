import sys
import argparse
import xml.etree.ElementTree as ET

def convert_atdf(file):
    tree = ET.parse(file)
    root = tree.getroot()

    modules = root.findall("modules/module")

    print("from updizombie import xmega3_regprop, Xmega3Debug")
    print()

    for md in modules:
        print("\"\"\"%s\"\"\"" % md.get("caption"))
        print("class Xmega3_%s():" % md.get("name"))
        print("    def __init__(self, mcu, baseaddress):")
        print("        self.mcu = mcu")
        print("        self.baseaddress = baseaddress")
        print()

        regs = md.findall("register-group/register")
        for reg in regs:

            print("    %s = xmega3_regprop(%s, %s, \"%s\")" % (
                reg.get("name"),
                reg.get("offset"),
                reg.get('size'),
                reg.get("caption")
            ))
        print()

    devs = root.findall("devices/device")

    for dev in devs:

        print("class %s(Xmega3Debug):" % dev.get("name"))
        print()
        print("    def __init__(self, link):")
        print("        super().__init__(link)")

        reggroups = dev.findall("peripherals/module/instance/register-group")

        for rg in reggroups:
            #self.PORTA = Xmega3Port(self, 0x0400)
            print("        self.%s = Xmega3_%s(self, %s)" % (
                rg.get('name'),
                rg.get('name-in-module'),
                rg.get('offset'),
            ))

def main():
    parser = argparse.ArgumentParser(description="Convert ATDF files to Python classes")
    parser.add_argument("-f", "--file", required=True,
                        help="ATDF file to be converted")

    args = parser.parse_args(sys.argv[1:])

    convert_atdf(args.file)



if __name__ == "__main__":
    main()