#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32MultiArray

class Polynominal:
    def __init__(self):
        rospy.init_node('polynominal')
        self.sub = rospy.Subscriber('input_numbers', Float32MultiArray, self.callback)
        self.pub = rospy.Publisher('squared_numbers', Float32MultiArray, queue_size=10)
        rospy.loginfo("Polynominal node started")
        
    def callback(self, msg):
        numbers = msg.data
        rospy.loginfo(f"Received numbers: {numbers}")
        
        # Возводим в степень в зависимости от позиции (1, 2, 3)
        squared = [num ** (i+1) for i, num in enumerate(numbers)]
        
        result_msg = Float32MultiArray()
        result_msg.data = squared
        
        self.pub.publish(result_msg)
        rospy.loginfo(f"Sent squared numbers: {squared}")

if __name__ == "__main__":
    Polynominal()
    rospy.spin()
