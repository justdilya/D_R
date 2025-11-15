#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import LaserScan
import math

def scan_callback(data):
    # Получаем данные с лидара
    ranges = data.ranges  # массив расстояний
    angle_min = data.angle_min  # минимальный угол
    angle_max = data.angle_max  # максимальный угол
    angle_increment = data.angle_increment  # шаг угла
    
    # Находим расстояние вперед (примерно 0 градусов)
    front_index = len(ranges) // 2
    front_distance = ranges[front_index]
    
    # Находим расстояние слева (примерно -90 градусов)
    left_index = len(ranges) // 4
    left_distance = ranges[left_index]
    
    # Находим расстояние справа (примерно 90 градусов)
    right_index = 3 * len(ranges) // 4
    right_distance = ranges[right_index]
    
    # Выводим информацию
    print(f"Перед: {front_distance:.2f} м | Слева: {left_distance:.2f} м | Справа: {right_distance:.2f} м")
    
    # Простая логика избегания препятствий
    if front_distance < 1.0 and front_distance > 0.1:  # если препятствие ближе 1 метра
        print("⚠️  ВНИМАНИЕ: Препятствие впереди!")
    if left_distance < 0.5 and left_distance > 0.1:   # если слева ближе 0.5 метра
        print("⬅️  Слева близко!")
    if right_distance < 0.5 and right_distance > 0.1:  # если справа ближе 0.5 метра
        print("➡️  Справа близко!")
    print("---")  # разделитель для читаемости

def lidar_listener():
    rospy.init_node('lidar_analyzer', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, scan_callback)
    
    print("Анализатор лидара запущен...")
    print("Нажмите Ctrl+C для остановки")
    rospy.spin()

if __name__ == '__main__':
    try:
        lidar_listener()
    except rospy.ROSInterruptException:
        pass
