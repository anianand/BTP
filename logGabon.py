import cv2
import math
import numpy as np
number_scales = 5          # scale resolution
number_orientations = 8    # orientation resolution
N = 128                    # image dimensions
def getFilter(f_0, theta_0):
    # filter configuration
    scale_bandwidth =  0.996 * math.sqrt(2/3)
    angle_bandwidth =  0.996 * (1/math.sqrt(2)) * (np.pi/number_orientations)

    # x,y grid
    extent = np.arange(-N/2, N/2 + N%2)
    x, y = np.meshgrid(extent,extent)

    mid = int(N/2)
    ## orientation component ##
    theta = np.arctan2(y,x)
    center_angle = ((np.pi/number_orientations) * theta_0) if (f_0 % 2) \
                else ((np.pi/number_orientations) * (theta_0+0.5))

    # calculate (theta-center_theta), we calculate cos(theta-center_theta) 
    # and sin(theta-center_theta) then use atan to get the required value,
    # this way we can eliminate the angular distance wrap around problem
    costheta = np.cos(theta)
    sintheta = np.sin(theta)
    ds = sintheta * math.cos(center_angle) - costheta * math.sin(center_angle)    
    dc = costheta * math.cos(center_angle) + sintheta * math.sin(center_angle)  
    dtheta = np.arctan2(ds,dc)

    orientation_component =  np.exp(-0.5 * (dtheta/angle_bandwidth)**2)

    ## frequency componenet ##
    # go to polar space
    raw = np.sqrt(x**2+y**2)
    # set origin to 1 as in the log space zero is not defined
    raw[mid,mid] = 1
    # go to log space
    raw = np.log2(raw)

    center_scale = math.log2(N) - f_0
    draw = raw-center_scale
    frequency_component = np.exp(-0.5 * (draw/ scale_bandwidth)**2)

    # reset origin to zero (not needed as it is already 0?)
    frequency_component[mid,mid] = 0

    return frequency_component * orientation_component
img=cv2.imread('050.png')
im=getFilter(img,1.0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
