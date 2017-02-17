# import cv2
# import numpy as np
#
# cap = cv2.VideoCapture(0)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter_('output.avi',forcc,20.0,(640,480))
#
# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#     out.write(frame)
#     cv2.imshow('frame',frame)
#     cv2.imshow('gray',gray)
#
#     if cv2.waitKey(1) & Oxff == ord('q'):
#         break
#
# cap.release()
# out.release()
# cv2.destroyAllWindows()

import cv2
# Print version string
print "OpenCV version :  {0}".format(cv2.__version__)
