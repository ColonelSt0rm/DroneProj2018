import pymultiwii import MultiWii
import ESC
import multiwii



if __name__ == "__main__":
    
    ESC.calibrate()
    try:
        thread.start_new_thread(ESC.manual_drive())
        thread.start_new_thread(multiwii.runAttitude())
    except:
        print "Error: unable to start thread"
