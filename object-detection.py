#!/usr/bin/env python3.8
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import time
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import cv2
from std_msgs.msg import String
import numpy as np

# Create a CvBridge instance to convert between ROS Image messages and OpenCV images
bridge = CvBridge()

coordinates_pub = rospy.Publisher('depth_pub', String, queue_size=10)

def depth_callback(data):
    global depth_image
    depth_image = bridge.imgmsg_to_cv2(data)

# Load YOLO model, I put the weights close to the depth node for ease of access
model = YOLO("./models/yolov8s.pt")
print("YOLO model loaded.")

latest_image = None
annotated_image =  None


# gets image from stream, predicts and sends data to depth listener
def image_callback(msg):
    global latest_image, bridge, annotated_image
    print("Received Image")
    try:
        latest_image = bridge.imgmsg_to_cv2(msg,"bgr8")
        annotator = Annotator(latest_image)
        print("Image Converted")
    except CvBridgeError as e:
        print(e)
    results = model.predict(latest_image)

    boxResults = results[0].boxes
    boxes2 = boxResults.xyxy.tolist()
    classes = boxResults.cls.tolist()
    names = results[0].names
    confidences = boxResults.conf.tolist()

    # Iterates over all known objects and prints their coordinates, label and the confidence that that indeed is the label
    for box,cls,conf in zip(boxes2, classes, confidences):
        x1, y1, x2, y2 = box
        confidence = conf
        detected_class = cls
        name = names[int(cls)]

        # Converts the resulting coordinates into an array and publishes it into the specified topic to be listened to by depth_status_listener
        col = int((box[0] + box[2]) / 2)
        row = int((box[1] + box[3]) / 2)
        depth_value = depth_image[row, col]
        depth_meters = depth_value / 1000.0
        annotator.box_label(box, model.names[int(cls)])
        annotated_image = annotator.result()
        
        # col is x coordinate while row is y coordinate
        # angle is calculated where 0 degrees is straight ahead while -35 is 35 to the left and +35 is 35 to the right
        if depth_meters != 0.0:
            angle = ((col / 1280) * 70) - 35
            coordinates_pub.publish(f"{name} - {depth_meters} - {confidence} - [{col}, {row}] - {angle}")


def main():
    global annotated_image, latest_image

    rospy.init_node('yolo_detector')
    rospy.Subscriber('/camera/color/image_raw', Image, image_callback)
    rospy.Subscriber('/camera/depth/image_rect_raw', Image, depth_callback)

    rospy.spin()

if __name__ == '__main__':
    main()
