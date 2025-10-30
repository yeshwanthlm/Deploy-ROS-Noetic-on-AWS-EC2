import time
import roslibpy

# Connect to rosbridge running on your cloud machine
ros = roslibpy.Ros(host='3.88.102.27', port=9090)
ros.run()

if ros.is_connected:
    print('Connected to ROS master via rosbridge!')
else:
    print('Failed to connect.')
    exit(1)

# Create a publisher to topic /numbers
talker = roslibpy.Topic(ros, '/numbers', 'std_msgs/Int32')

count = 0
try:
    while ros.is_connected:
        talker.publish(roslibpy.Message({'data': count}))
        print(f'Published: {count}')
        count += 1
        time.sleep(1)  # publish every 1 second
except KeyboardInterrupt:
    print('\nStopped by user')
finally:
    talker.unadvertise()
    ros.close()
