#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray, Float32

class Request:
    def __init__(self, numbers):
        rospy.init_node('request')
        self.pub = rospy.Publisher('input_numbers', Float32MultiArray, queue_size=10)
        self.sub = rospy.Subscriber('final_result', Float32, self.callback)
        self.result = None
        self.numbers = numbers
        rospy.loginfo("Request node started")
        
    def callback(self, msg):
        self.result = msg.data
        rospy.loginfo(f"Final result received: {self.result}")
        rospy.signal_shutdown("Result received")
        
    def run(self):
        # Ждём подключения подписчиков
        rospy.sleep(2)
        
        # Отправляем числа
        msg = Float32MultiArray()
        msg.data = self.numbers
        self.pub.publish(msg)
        rospy.loginfo(f"Sent numbers to process: {self.numbers}")
        
        rospy.spin()
        return self.result

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: request.py num1 num2 num3")
        print("Example: request.py 2 3 4")
        sys.exit(1)
        
    numbers = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
    node = Request(numbers)
    result = node.run()
    print(f"FINAL RESULT: {result}")
