#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

num1 = None
num2 = None

def callback_num1(msg):
    global num1
    num1 = msg.data
    publish_sum()

def callback_num2(msg):
    global num2
    num2 = msg.data
    publish_sum()

def publish_sum():
    global num1, num2
    if num1 is not None and num2 is not None:
        total = num1 + num2
        rospy.loginfo(f"Adding numbers: {num1} + {num2} = {total}")
        pub.publish(total)

def adder():
    global pub
    rospy.init_node('adder_node', anonymous=True)
    rospy.Subscriber('num1', Int32, callback_num1)
    rospy.Subscriber('num2', Int32, callback_num2)
    pub = rospy.Publisher('sum', Int32, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        adder()
    except rospy.ROSInterruptException:
        pass
