import rclpy
from rclpy.node import Node
from my_robot_msgs.msg import RobotData

class PublisherNode(Node):
    def __init__(self):
        super().__init__('publisher_node')
        
        self.publisher_ = self.create_publisher(RobotData, 'robot_data', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        
        self.x = 0.0

    def timer_callback(self):
        msg = RobotData()
        
        msg.x = self.x
        msg.y = self.x * 2
        msg.speed = 1.5
        
        self.publisher_.publish(msg)
        
        self.get_logger().info(
            f'Publishing -> x: {msg.x}, y: {msg.y}, speed: {msg.speed}'
        )
        
        self.x += 1.0

def main(args=None):
    rclpy.init(args=args)
    node = PublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
