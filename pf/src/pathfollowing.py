#!/usr/bin/env python
#
# Creation:
#   November 2023
#
#
# Description:
#   This code is intended for the implementation of simple path following algorithms for
#   testing purposes for DSOR newcommers

# ROS basics
import rospy

# ROS messsages
from test_msgs.msg import mRef, mState

class PathFollowing:
    def __init__(self):
        rospy.loginfo('Initializing Path Following Node')
        rospy.init_node('pf_node')

        self.timer = rospy.Timer(rospy.Duration(0.1), self.timerCallback)

        # Subscriber definition
        self.sub_state = rospy.Subscriber("/state", mState, self.stateCallback)

        # Publisher definition
        self.pub_ref = rospy.Publisher("/ref", mRef, queue_size=10)

        # Parameters definition
        self.x = 0
        self.y = 0
        self.yaw = 0

        self.last_time = rospy.get_time()

    def stateCallback(self, msg):
        self.x = msg.x
        self.y = msg.y
        self.yaw = msg.psi

    # TODO
    def pathCreation(self):
        pass

    def timerCallback(self, event):
        pass

if __name__ == '__main__':
    pf_node = PathFollowing()