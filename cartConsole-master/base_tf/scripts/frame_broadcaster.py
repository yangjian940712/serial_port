#!/usr/bin/env python
#-*- coding: utf-8 -*-
import roslib
roslib.load_manifest('base_tf')
import rospy
import tf
from nav_msgs.msg import Odometry

def handle_pose(msg, framename):
    br = tf.TransformBroadcaster()
    # br.sendTransform(msg.pose.pose.position,
    #                  msg.pose.pose.orientation,
    #                  rospy.Time.now(),
    #                  framename,
    #                  msg.child_frame_id)
    br.sendTransform((msg.pose.pose.position.x,msg.pose.pose.position.y,msg.pose.pose.position.z),
                     (msg.pose.pose.orientation.x,msg.pose.pose.orientation.y,msg.pose.pose.orientation.z,msg.pose.pose.orientation.w),
                     rospy.Time.now(),
                     framename,
                     msg.child_frame_id)
    print msg.pose.pose.orientation

if __name__ == '__main__':
    rospy.init_node('frame_broadcaster')
    framename = rospy.get_param('~frame')
    # rospy.Subscriber('/%s/pose' % framename,
    #                  turtlesim.msg.Pose,
    #                  handle_pose,
    #                  framename)
    rate = rospy.Rate(10)
    rospy.Subscriber('/%s' % framename,Odometry,handle_pose,framename)
    rospy.spin()