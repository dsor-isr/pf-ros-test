# Installation:
 
> **[IMPORTANT]** It is highly recommended that DSOR Bookstack's "First Steps" are thoroughly read before using this repo.

Run:
```sh
mkdir -p ~/dsor/catkin_ws_pf-ros-test/src
cd ~/dsor/pf-ros-test/src
git clone git@github.com:dsor-isr/pf-ros-test.git .
set_catkin_ws_function pf-ros-test
cd ~/dsor/pf-ros-test/
catkin build
source ~/.bashrc
```

# How to run:

Find out in which port ROS is running in your current pc. If you're running this in your local pc, it should be `11311`. Otherwise (assuming you're using DSOR servers), it is something different - please follow Bookstack's "First Steps" to find it out.

Now that you know your port number, run the following commands in different terminals:

```sh
roscore -p <port_number>
rosrun pf pathfollowing.py
rosrun sim kinematics.py
```

For easy visualisation of ROS topics in real-time (and to help debugging), use [Plotjuggler](https://index.ros.org/p/plotjuggler/):

```sh
rosrun plotjuggler plotjuggler
```