cmake_minimum_required(VERSION 3.1)
project(test_msgs)

find_package(catkin REQUIRED
 COMPONENTS
 std_msgs
 message_generation
)

# generate messages in the 'msg' folder
add_message_files(
	DIRECTORY msg
)

# generate added messages with any dependencies listed here
generate_messages(
   DEPENDENCIES
   std_msgs
)

# catkin_python_setup()

catkin_package(
 CATKIN_DEPENDS
)
