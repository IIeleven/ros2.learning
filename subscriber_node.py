import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class MinimalSubscriber(Node):

  def __init__(self):
    super().__init__('minimal_subscriber')
    self.subscription = self.create_subscription(
        String, 'topic_demo', self.listener_callback, 10
    )
    self.subscription
    self.get_logger().info('订阅者节点已启动，开始监听 topic_demo...')

  def listener_callback(self, msg):
    self.get_logger().info(f'收到消息: "{msg.data}"')


def main(args=None):
  rclpy.init(args=args)
  node = MinimalSubscriber()
  try:
    rclpy.spin(node)
  except KeyboardInterrupt:
    pass
  node.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()