from pymultiwii import MultiWii
import ESC
import multiwii

if __name__ == "__main__":

    ESC.calibrate()
    try:
        # we want to show telemetry while communicating with motors, so this should do the trick
        thread.start_new_thread(ESC.manual_drive())
        thread.start_new_thread(multiwii.runAttitude())
    except:
        print "Error: unable to start thread"
