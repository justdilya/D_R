#!/usr/bin/env python3
import rospy

def main():
    rospy.init_node('param_demo_node')
    
    # Устанавливаем параметры разных типов
    rospy.set_param('~private_param', 'Это приватный параметр')
    rospy.set_param('local_param', 'Это локальный параметр')
    rospy.set_param('/global_param', 'Это глобальный параметр')
    
    # Чтение параметров
    try:
        private_val = rospy.get_param('~private_param')
        rospy.loginfo(f"Приватный параметр: {private_val}")
    except KeyError:
        rospy.logwarn("Приватный параметр не найден")
    
    # Чтение с значением по умолчанию
    default_val = rospy.get_param('nonexistent_param', 'значение_по_умолчанию')
    rospy.loginfo(f"Параметр по умолчанию: {default_val}")
    
    # Список всех параметров
    all_params = rospy.get_param_names()
    rospy.loginfo("Все параметры:")
    for param in all_params:
        rospy.loginfo(f"  - {param}")
    
    rospy.loginfo("Демонстрация параметров завершена!")

if __name__ == '__main__':
    main()
