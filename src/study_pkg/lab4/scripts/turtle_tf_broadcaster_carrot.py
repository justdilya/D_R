#!/usr/bin/env python3

import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose
import math
import time

# Глобальная переменная для времени
start_time = time.time()

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    
    # Публикуем преобразование для черепашки
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")
    
    # Если это первая черепашка, добавляем ВРАЩАЮЩУЮСЯ морковку
    if turtlename == "turtle1":
        # Морковка вращается по кругу вокруг черепашки
        radius = 1.0  # радиус вращения
        angular_speed = 1.0  # скорость вращения (рад/с)
        
        # Вычисляем текущий угол на основе времени
        current_time = time.time() - start_time
        angle = angular_speed * current_time
        
        # Координаты морковки (круг)
        x_carrot = radius * math.cos(angle)
        y_carrot = radius * math.sin(angle)
        
        # Публикуем преобразование для вращающейся морковки
        br.sendTransform((x_carrot, y_carrot, 0),
                         quaternion_from_euler(0, 0, 0),
                         rospy.Time.now(),
                         "carrot",
                         turtlename)
        
        rospy.loginfo_once("Вращающаяся морковка создана!")

if __name__ == '__main__':
    rospy.init_node('tf_turtle_broadcaster_carrot')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                     Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
