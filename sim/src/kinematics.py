#!/usr/bin/env python
#
# Creation:
#   November 2023
#
#
# Description:
#   This code is intended for the simulation with kinematics of simple path following
#   algorithms of DSOR newcommers

# ROS basics
import rospy
import numpy as np

# ROS messsages
from test_msgs.msg import mRef, mState

class Kinematics:
    def __init__(self):
        rospy.loginfo('Initializing Kinematics Node')
        rospy.init_node('pf_node')

        self.timer = rospy.Timer(rospy.Duration(0.1), self.timerCallback)

        # Subscriber definition
        self.sub_ref = rospy.Subscriber("/ref", mRef, self.refCallback)

        # Publisher definition
        self.pub_state = rospy.Publisher("/state", mState, queue_size=10)
        
        # Parameters definition
        self.x = 0
        self.y = 0
        self.yaw = 0

        self.last_time = rospy.get_time()

        self.surge = 0
        self.yaw_rate = 0

    def refCallback(self, msg):
        self.surge = msg.u
        self.yaw_rate = msg.r

    def timerCallback(self, event):
        new_time = rospy.get_time()
        dt = new_time - self.last_time

        x_dot = self.surge * np.cos(self.yaw)
        y_dot = self.surge * np.sin(self.yaw)
        
        self.x = self.x + x_dot * dt
        self.y = self.y + y_dot * dt
        self.yaw = self.yaw + self.yaw_rate * dt        # TODO VERY IMPORTANT ANGLE WRAP AROUND 2pi OR 360 DEGREES

        state_msg = mState()
        state_msg.x = self.x
        state_msg.y = self.y
        state_msg.psi = self.yaw
        self.pub_state.publish(state_msg)

        self.last_time = new_time

if __name__ == '__main__':
    pf_node = Kinematics()

    rospy.spin()