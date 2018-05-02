from pymultiwii import MultiWii
from sys import stdout

def runAttitude():
    board = MultiWii("/dev/bus/usb/001/002")
    print "MARK2"
    try:
        while True:
            board.getData(MultiWii.ATTITUDE)
            message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(float(board.attitude['angx']),float(board.attitude['angy']),float(board.attitude['heading']),float(board.attitude['elapsed']))
            stdout.write("\r%s" % message )
            stdout.flush()
    except Exception,error:
        print "Error on Main: "+str(error)
