#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

rospy.init_node('even_numbers_talker')
pub = rospy.Publisher('even_numbers_topic', Int32, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

def start_talker():
    number = 0
    while not rospy.is_shutdown():
        # Публикуем только четные числа
        rospy.loginfo("Publishing even number: %d", number)
        
        msg = Int32()
        msg.data = number
        pub.publish(msg)
        
        number += 2  # Увеличиваем на 2 для след. четного числа
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
