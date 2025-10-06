#!/usr/bin/env python3

import rospy

def main():
    # Инициализируем узел ROS с именем "first_node"
    rospy.init_node('first_node')
    
    # Выводим сообщение
    rospy.loginfo("Hello ROS World!")
    
    # Чтобы программа не завершалась сразу
    rospy.spin()

if __name__ == "__main__":
    main()

