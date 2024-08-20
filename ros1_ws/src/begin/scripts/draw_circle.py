#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


if __name__ == '__main__':
    rospy.init_node('draw_cycle')
    rospy.loginfo('Node /draw_cycle is started running')
    
    pub=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    
    rate=rospy.Rate(10)
    
    while not rospy.is_shutdown():
        # Create a Twist message
        twist = Twist()
        
        # Set the linear and angular velocities
        twist.linear.x = 0.5
        twist.angular.z = 0.2
        
        # Publish the Twist message
        pub.publish(twist)
        
        rate.sleep()