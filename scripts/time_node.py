#!/usr/bin/env python3

import rospy
import datetime
import time

def main():
    rospy.init_node('time_node')
    
    while not rospy.is_shutdown():
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        rospy.loginfo(f"Time: {current_time}")
        time.sleep(5)

if __name__ == "__main__":
    main()
