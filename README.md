# Mavros
Some of my basic mavros code that usefull for starting mavros project and learning ROS.

A. Get Started using ROS

    1. Create workspace:
      - mkdir catkin_ws
      - enter directory catkin_ws
      - mkdir src
      - (on terminal):catkin_make
     
    2. Set Up Environtment:
      - source devel/setup.sh
     
    3. Create Packages:
      - catkin_create_pkg <package_name> [depend1] [depend2] [depend3]
      - to see depend, go to /opt/ros/kinetic/share
      - create script on .. /<your_packages>/src/
      
B. Basic ROS command
    
    1. roscore (do roscore first to connect with master)
    2. rosrun <packages> <your_code> (to run your program)
    3. rostopic
    4. roslaunch (sometimes launch file have init node)
      
    
