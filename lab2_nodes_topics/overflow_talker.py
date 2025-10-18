#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32, String

rospy.init_node('overflow_talker')
pub_even = rospy.Publisher('even_numbers_topic', Int32, queue_size=10)
pub_overflow = rospy.Publisher('overflow_topic', String, queue_size=10)
rate = rospy.Rate(10)  # 10 Hz

def start_talker():
    number = 0
    while not rospy.is_shutdown():
        rospy.loginfo("Publishing number: %d", number)
        
        # Публикуем четное число
        msg_even = Int32()
        msg_even.data = number
        pub_even.publish(msg_even)
        
        # Проверяем переполнение
        if number >= 100:
            overflow_msg = String()
            overflow_msg.data = "OVERFLOW! Counter reached %d" % number
            pub_overflow.publish(overflow_msg)
            rospy.logwarn("Overflow detected! Resetting counter.")
            number = 0  # Сбрасываем счетчик
        else:
            number += 2  # Следующее четное число
        
        rate.sleep()

try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
