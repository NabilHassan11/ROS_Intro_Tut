#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def pose_callback(pose: Pose):
    cmd = Twist()

    if pose.x > 9.0 or pose.x< 2.0 or pose.y > 9.0 or pose.y <2.0:
        cmd.linear.x = 1
        cmd.angular.z = 1.5

    else:
        cmd.linear.x = 5
        cmd.angular.z = 0.0
    
    pub.publish(cmd)
    
    #rospy.loginfo("(" + str(msg.x) + ", " + str(msg.y) + ")")

if __name__ == '__main__':

    rospy.init_node("turtle_controller")

    pub = rospy.Publisher("/turtle1/cmd_vel", Twist , queue_size= 10)

    sub = rospy.Subscriber("/turtle1/pose", Pose, callback = pose_callback)

    rospy.loginfo("The node has been started")

    rospy.spin()