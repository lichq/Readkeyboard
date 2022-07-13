from evdev import InputDevice
from select import select

def detectInputKey():
    dev = InputDevice('/dev/input/event3')
    while True:
        select([dev], [], [])
        print("correct event")
        for event in dev.read():
            if (event.value == 1 or event.value == 0) and event.code != 0:
                print ("Key: %s Status: %s" % (event.code, "pressed" if event.value else "release"))


if __name__ == '__main__':
    detectInputKey()

