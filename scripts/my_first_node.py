#!/usr/bin/env python3
import rospy

if __name__ == '__main__':
    rospy.init_node("test_node")

    rospy.loginfo("test_node has been started")
    # rospy.logwarn("This is a warning")
    # rospy.logerr("This is an error")

    # rospy.sleep(1.0)

    # rospy.loginfo("End of program")

    rate = rospy.Rate(1)

    count_down = 10
    
    while not rospy.is_shutdown():
        if(count_down > 0):
            rospy.loginfo(count_down)
            rate.sleep()
            count_down = count_down-1
        
        else:
            rospy.loginfo("Nigger")
            rospy.sleep(0.1)

        
