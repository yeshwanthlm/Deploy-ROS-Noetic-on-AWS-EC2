#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32
import random

def publisher():
    rospy.init_node('number_publisher', anonymous=True)
    pub1 = rospy.Publisher('num1', Int32, queue_size=10)
    pub2 = rospy.Publisher('num2', Int32, queue_size=10)
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        a = random.randint(1, 100)  # Random number between 1 and 100
        b = random.randint(1, 100)
        rospy.loginfo(f"Publishing numbers: num1={a}, num2={b}")
        pub1.publish(a)
        pub2.publish(b)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
