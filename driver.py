import pymultiwii import MultiWii
import ESC




if __name__ == "__main__":

    ESC.calibrate()

    board = MultiWii("/dev/tty.SLAB_USBtoUART")
    try:
        while True:
            board.getData(MultiWii.ATTITUDE)
            message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(float(board.attitude['angx']),float(board.attitude['angy']),float(board.attitude['heading']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
    except Exception,error:
        print "Error on Main: "+str(error)
