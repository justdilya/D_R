#!/usr/bin/env python3

import rospy
import tf
from tf.transformations import quaternion_from_euler
from turtlesim.msg import Pose

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")

if __name__ == '__main__':
    rospy.init_node('tf_turtle_broadcaster')
    turtlename = rospy.get_param('~turtle')
    rospy.Subscriber('/%s/pose' % turtlename,
                     Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
