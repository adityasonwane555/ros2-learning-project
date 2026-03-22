import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import RobotData

class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node')
        
        self.subscription = self.create_subscription(
            RobotData,
            'robot_data',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'Received -> x: {msg.x}, y: {msg.y}, speed: {msg.speed}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = SubscriberNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
