#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import math

def draw_flower():
    rospy.init_node('turtle_flower')

    rospy.loginfo("Node has been started")

    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    
    vel_msg = Twist()
    
    petals = 6  # Number of petals
    angle = 360 / petals
    
    for _ in range(petals):
        for _ in range(12):  # Smaller petal curve
            vel_msg.linear.x = 1  # Lower speed
            vel_msg.angular.z = math.radians(30)  # Sharper turns
            pub.publish(vel_msg)
            rate.sleep()
        
        for _ in range(12):  # Complete the petal curve
            vel_msg.linear.x = 1
            vel_msg.angular.z = -math.radians(30)
            pub.publish(vel_msg)
            rate.sleep()
        
        # Rotate to start the next petal
        vel_msg.linear.x = 0
        vel_msg.angular.z = math.radians(angle)
        for _ in range(10):
            pub.publish(vel_msg)
            rate.sleep()

        

    # Rotate to start the next petal
    vel_msg.linear.x = 0
    vel_msg.angular.z = -math.radians(120)   
    for _ in range(9):
            pub.publish(vel_msg)
            rate.sleep()    
    
    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

    for _ in range(12):  # Smaller petal curve
            vel_msg.linear.x = 2  # Lower speed
            vel_msg.angular.z = math.radians(15)  # Sharper turns
            pub.publish(vel_msg)
            rate.sleep()

    for _ in range(12):  # Smaller petal curve
            vel_msg.linear.x = 2  # Lower speed
            vel_msg.angular.z = -math.radians(15)  # Sharper turns
            pub.publish(vel_msg)
            rate.sleep()

    # Stop the turtle
    vel_msg.linear.x = 0
    vel_msg.angular.z = 0
    pub.publish(vel_msg)

if __name__ == '__main__':
    try:
        draw_flower()
    except rospy.ROSInterruptException:
        pass
