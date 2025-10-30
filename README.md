# Deploy ROS Noetic on AWS EC2: End-to-End Demo

<img width="1920" height="1080" alt="Run ROS Noetic on AWS EC2" src="https://github.com/user-attachments/assets/83197c26-a99b-4645-84a3-303edec3a084" />

## Prerequisites: 
1. AWS Account with the permission to create EC2.
2. Three EC2 Instances.
3. ROS Should be installed on all the three servers. 


Step 0: Login to AWS Console: https://console.aws.amazon.com/console/

Step 1: Create EC2 Server with the Userdata Script:

```sh
#!/bin/bash
set -e
sudo apt update -y
sudo apt install -y software-properties-common curl vim lsb-release
sudo add-apt-repository universe -y
sudo add-apt-repository restricted -y
sudo add-apt-repository multiverse -y
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update -y
sudo apt install -y ros-noetic-ros-base
sudo apt install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo rosdep init || true
rosdep update
sudo apt update -y
sudo apt install -y ros-noetic-rosbridge-server
```

Step 2: Run this command: 
```sh
source /opt/ros/noetic/setup.bash
```

Step 3: Set Up Catkin Workspace and Sourcing

```sh
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin_make
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Step 4: Create ROS Package and Custom Folders

```sh
cd ~/catkin_ws/src
catkin_create_pkg my_robot_pkg std_msgs rospy roscpp
cd my_robot_pkg
mkdir launch arduino_scripts python_scripts
cd ~/catkin_ws
catkin_make
```

Step 5: Add the sample python script:

```sh
cd /root/catkin_ws/src/my_robot_pkg/python_scripts
```

Step 6: Export ROS URI's:

```sh
export ROS_MASTER_URI=http://MSATER_NODE_IP:11311
export ROS_HOSTNAME=IP_OF_THE _HOST
```

Step 7: Run and Test ROS:

```sh
roscore
roslaunch rosbridge_server rosbridge_websocket.launch
```

## For Bridge Network:

Cloud Server:
```sh
roslaunch rosbridge_server rosbridge_websocket.launch
```

Local Machine:
```sh
pip install roslibpy
```
```sh
python3 name_of_the_file.py
```

Connect with me:
* Follow us on LinkedIn: https://www.linkedin.com/in/yeshwanth-l-m/
* YouTube: https://www.youtube.com/@TechWithYeshwanth/videos
* Follow our blog here: https://dev.to/yeshwanthlm/
* Follow us on Instagram: https://www.instagram.com/techwithyeshwanth/
