import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TestNode(Node):
    def __init__(self):
        super().__init__("TestNode")
        self.get_logger().info("Hello World")
        self.pub = self.create_publisher(String,"repeat_Hello",20)
        self.period = self.create_timer(1, self.callBackFunctionPublisher)

    # this is the callback function
    def callBackFunctionPublisher(self):
        
        messagePythonString= 'Repeat Myself...'

        messageToBeSent = String()
        messageToBeSent.data = messagePythonString
        
        self.pub.publish(messageToBeSent)        


def main():
    rclpy.init()
    node = TestNode()
    # ......

    # this will spin the Node, that is, it will make sure that the proper
    # callback function is called
    # while rclpy.ok()
    rclpy.spin(node)

    # here, we destroy and shutdown
    node.destroy_node()
    rclpy.shutdown()
