#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def callback(msg):
    rospy.loginfo('Position of turtle1: x=%f, y=%f, theta=%f', msg.x, msg.y, msg.theta)
    rospy.loginfo('velocity of turtle1: x=%f, y=%f', msg.linear_velocity, msg.angular_velocity)

def pose_subcriber():
    rospy.init_node('pose_subscriber', anonymous=True)
    sub=rospy.Subscriber('/turtle1/pose', Pose, callback)

    rospy.spin()

if __name__ == '__main__':
    pose_subcriber()
    
    