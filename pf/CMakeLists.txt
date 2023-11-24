cmake_minimum_required(VERSION 3.1)
project(pf)

find_package(catkin REQUIRED
 COMPONENTS
 rospy
)

catkin_python_setup()

catkin_package(
 CATKIN_DEPENDS
)

catkin_install_python(PROGRAMS src/pathfollowing.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)