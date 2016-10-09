import OpenST

OpenST.calibrate(True, 6500000)
while True :
    OpenST.say(OpenST.listen("en-US", True, True))
