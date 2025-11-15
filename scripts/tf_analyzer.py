#!/usr/bin/env python3
import rospy
import tf2_ros
import geometry_msgs.msg
import math

def analyze_tf():
    rospy.init_node('tf_analyzer')
    
    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)
    
    rate = rospy.Rate(1)  # 1 Hz
    
    print("Анализ TF трансформаций...")
    print("=" * 50)
    
    while not rospy.is_shutdown():
        try:
            # Статическая трансформация
            static_tf = tf_buffer.lookup_transform('base_footprint', 'base_scan', rospy.Time())
            static_x = static_tf.transform.translation.x
            static_y = static_tf.transform.translation.y
            static_z = static_tf.transform.translation.z
            
            # Динамическая трансформация (одометрия)
            dynamic_tf = tf_buffer.lookup_transform('odom', 'base_footprint', rospy.Time())
            dynamic_x = dynamic_tf.transform.translation.x
            dynamic_y = dynamic_tf.transform.translation.y
            dynamic_z = dynamic_tf.transform.translation.z
            
            print(f"СТАТИЧЕСКАЯ (base_footprint → base_scan):")
            print(f"  x: {static_x:.3f}, y: {static_y:.3f}, z: {static_z:.3f}")
            
            print(f"ДИНАМИЧЕСКАЯ (odom → base_footprint):")
            print(f"  x: {dynamic_x:.3f}, y: {dynamic_y:.3f}, z: {dynamic_z:.3f}")
            print(f"  Расстояние от начала: {math.sqrt(dynamic_x**2 + dynamic_y**2):.2f} м")
            print("-" * 30)
            
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            print("Ошибка получения TF трансформации")
        
        rate.sleep()

if __name__ == '__main__':
    try:
        analyze_tf()
    except rospy.ROSInterruptException:
        pass
