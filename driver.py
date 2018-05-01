import ESC
import multiwii
import thread

if __name__ == "__main__":

#    ESC.calibrate()
    try:
        # we want to show telemetry while communicating with motors, so this should do the trick
        thread.start_new_thread(ESC.manual_drive, ())
        thread.start_new_thread(multiwii.runAttitude, ())
    except Exception as e:
        print "Error: unable to start thread"
        print type(e)
        print e
    while(1):
        pass
