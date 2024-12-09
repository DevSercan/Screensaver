from lib.Screensaver import Screensaver

def main():
    inactivityDuration = 1000
    screensaver = Screensaver(inactivityDuration=inactivityDuration)
    screensaver.run()

if __name__ == "__main__":
    main()
    
