import evdev
from evdev import *
def readBarcodes():
  print ("Reading barcodes from device")
  current_barcode = ""
  for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value == 1:
      keycode = categorize(event).keycode
      if keycode == 'KEY_ENTER':
        print(current_barcode.replace("LEFTSHIFT","").replace("TAB",",").replace("KPSLASH","/").replace("MINUS","-").replace("EQUAL","+").split(","))
        current_barcode = ""
      else:
        current_barcode += keycode[4:]
def find_device():
  device_name = 'Symbol Technologies, Inc, 2008 Symbol Bar Code Scanner::EA'
  devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
  for d in devices:
    print(d.name)
    if d.name == device_name:
      print("Found device " + d.name)
      return d
print(find_device())

device = find_device()
if device is None:
  print("Unable to find " + device_name)
else:
  # ... and read the bar codes.
  readBarcodes()
