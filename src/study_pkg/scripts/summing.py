#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray, Float32

class Summing:
    def __init__(self):
        rospy.init_node('summing')
        self.sub = rospy.Subscriber('squared_numbers', Float32MultiArray, self.callback)
        self.pub = rospy.Publisher('final_result', Float32, queue_size=10)
        rospy.loginfo("Summing node started")
        
    def callback(self, msg):
        numbers = msg.data
        rospy.loginfo(f"Received squared numbers: {numbers}")
        
        # Суммируем все числа
        total_sum = sum(numbers)
        
        result_msg = Float32()
        result_msg.data = total_sum
        
        self.pub.publish(result_msg)
        rospy.loginfo(f"Sent total sum: {total_sum}")

if __name__ == "__main__":
    Summing()
    rospy.spin()
