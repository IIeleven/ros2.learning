import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalPublisher(Node):

  def __init__(self):
    super().__init__('minimal_publisher')
    self.publisher_ = self.create_publisher(String, 'topic_demo', 10)
    self.timer = self.create_timer(1.0, self.timer_callback)
    self.i = 0

  def timer_callback(self):
    msg = String()
    msg.data = f'Hello ROS 2, 这是第 {self.i} 包数据'
    self.publisher_.publish(msg)
    self.get_logger().info(f'正在发布: "{msg.data}"')
    self.i += 1


def main(args=None):
  rclpy.init(args=args)
  node = MinimalPublisher()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()