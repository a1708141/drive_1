import rclpy
from rclpy.node import Node
from rclpy.publisher import Publisher
from geometry_msgs.msg import PoseStamped
from rclpy.duration import Duration

def drive_to_pos(x, y, w):
    rclpy.init(args=None)  # Initialize rclpy

    # Create a ROS 2 node
    node = Node("drive_to_pos_node")

    # Create a Publisher for the PoseStamped message
    pose_publisher1 = node.create_publisher(PoseStamped, "/goal_pose", 10)

    # Create a PoseStamped message
    goal_pose = PoseStamped()
    goal_pose.header.frame_id = "map"
    goal_pose.header.stamp = node.get_clock().now().to_msg()
    # goal_pose.pose.position.x = 0.2
    # goal_pose.pose.position.y = 1.5
    # goal_pose.pose.position.z = 0.0
    # goal_pose.pose.orientation.z = 0.7
    goal_pose.pose.orientation.w = 0.0
    print("I am here")
    # Publish the goal pose
    pose_publisher1.publish(goal_pose)
    print("I am here")

    # Spin the node to allow messages to be published
    rclpy.spin_once(node)

    # Shutdown the node when done
    node.destroy_node()
    rclpy.shutdown()
    print("I am here")
    # You can return the created message if needed
    return None