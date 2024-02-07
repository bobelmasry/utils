#!/usr/bin/env python3
import rospy
from std_msgs.msg import String, Float64MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

bridge = CvBridge()

def depth_status_callback(data):
    global depth_image
    rospy.loginfo(f"Received coordinates: [{int(data.data[0])}, {int(data.data[1])}, {int(data.data[2])}, {int(data.data[3])}]")
    col = int((data.data[0] + data.data[2]) / 2)
    row = int((data.data[1] + data.data[3]) / 2)
    depth_value = depth_image[row, col]
    depth_meters = depth_value / 1000.0
    rospy.loginfo(f"Distance to pixel ({row}, {col}): {depth_meters} meters")
    if depth_meters <= 0.5:
        pass
        #depth_status_pub.publish("Yes")
    else:
        pass
        #depth_status_pub.publish("No")

def depth_callback(data):
    global depth_image
    depth_image = bridge.imgmsg_to_cv2(data)



def main():
    rospy.init_node('depth_status_listener_node', anonymous=True)
    rospy.Subscriber('object_coordinates_pub', Float64MultiArray, depth_status_callback)
    rospy.Subscriber('/camera/depth/image_rect_raw', Image, depth_callback)
    rospy.spin()

if __name__ == '__main__':
    main()
