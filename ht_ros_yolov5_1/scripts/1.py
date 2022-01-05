#!/usr/bin/env python3
#coding=utf-8

import rospy
import cv2
from my_msgs.msg import MyImage
import numpy as np

def publish():
    image = MyImage()
    image.size = []
    size = 0
    while True:
        cap = cv2.VideoCapture('/media/htbao/xunfei/讯飞/讯飞规则解读 .mp4') # 视频
        while cap.isOpened() and not rospy.is_shutdown():
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, (1280, 720), interpolation=cv2.INTER_LINEAR)
                if not size:
                    image.size = list(frame.shape)
                    size = image.size[0]*image.size[1]*image.size[2]
                image.data = frame.reshape(size).tolist()	# 转一维list
                image.time = rospy.get_time()
                image_pub.publish(image)
                print("publish one：",image.time)

if __name__ == '__main__':
    try:
        print("publish start...")
        rospy.init_node('image_publish', anonymous=True)
        image_pub = rospy.Publisher('cam_image', MyImage, queue_size=5)
        publish()
        rospy.spin()
    except rospy.ROSInterruptException:
        print('ROSInterruptException')
        pass


