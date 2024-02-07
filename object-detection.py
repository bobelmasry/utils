#!/usr/bin/env python3.8
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge,CvBridgeError
import time
from ultralytics import YOLO
import cv2
from std_msgs.msg import Float64MultiArray

# Create a CvBridge instance to convert between ROS Image messages and OpenCV images
bridge = CvBridge()

object_coordinates_pub = rospy.Publisher('object_coordinates_pub', Float64MultiArray, queue_size=10)

# Load YOLO model, I put the weights close to the depth node for ease of access
model = YOLO("./models/yolov8s.pt")
print("YOLO model loaded.")

latest_image = None

# gets image from stream, predicts and sends data to depth listener
def image_callback(msg):
    global latest_image, bridge
    print("Received Image")
    try:
        latest_image = bridge.imgmsg_to_cv2(msg,"bgr8")
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
        print(f"{box} - {name} - {confidence}")

        # Converts the resulting coordinates into an array and publishes it into the specified topic to be listened to by depth_status_listener
        data_to_send = Float64MultiArray()
        data_to_send.data = box
        object_coordinates_pub.publish(data_to_send)


def main():
    rospy.init_node('yolo_detector')
    rospy.Subscriber('/camera/color/image_raw', Image, image_callback)

    while not rospy.is_shutdown():
        if latest_image is not None:
            cv2.imshow("YOLO Detection - Live", latest_image)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
