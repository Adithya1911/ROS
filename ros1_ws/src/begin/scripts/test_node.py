#!/usr/bin/env python3
import rospy



if __name__ == '__main__':
    rospy.init_node('test_node')                                #this is the name of the node that you will able to see in the node list when you run the command rosnode list 
    rospy.loginfo('test_node is started running ')              #this works as the print statement in th python but send the info/data present parameters 
    # rospy.logwarn('test_node is sending the warning message')   #this is used to make the warning message that appear in the terminal for making the warning   
    # rospy.logerr('test_node is sending the error message')      #this is used to make the error message to raise the error if something is gone wrong
    # rospy.spin()                                               #this keeps the node running until it is manually stopped by pressing Ctrl + C
    rate=rospy.Rate(10)                                        #this is used to setting the time to 1/10 seconds
     
    while not rospy.is_shutdown():                             #this is used to run the following steps until the node is terminated or shutdown by killing the terminal or Ctrl + C
        # your code here
        rospy.loginfo('test_node is running at 10 Hz')
        rate.sleep()
        