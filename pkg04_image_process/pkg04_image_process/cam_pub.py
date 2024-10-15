#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2


class ImagePublisher(Node):
    def __init__(self,name):
        super().__init__(name)
        self.publisher_ = self.create_publisher(Image,'image_raw',1)
        self.timer = self.create_timer(0.1,self.timer_cb)
        self.cap = cv2.VideoCapture(0) #后面是设备号
        self.cv_bridge = CvBridge()

        self.image_id = 0

    def timer_cb(self):
        ret ,frame = self.cap.read()

        if ret == True:
            image_msg = self.cv_bridge.cv2_to_imgmsg(frame,'bgr8')
            # 借助stamp对每个图片进行标号
            image_msg.header.stamp.sec = self.image_id
            self.image_id += 1

            self.publisher_.publish(image_msg)
            self.get_logger().info(f'发布id为{image_msg.header.stamp.sec}的图片')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher("topic_webcam_pub")
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()