#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class SmartPhonenode(Node):
    def __init__(self): 
        super().__init__("Smart_Phonenode")
        self.subscriper_= self.create_subscription(String,"robot_news",self.callback_suscriper,10)
        self.get_logger().info("Sub is init")
    
    def callback_suscriper(self, msg: String):
        self.get_logger().info(msg.data)  


def main(args=None):
    rclpy.init(args=args)  
    node=SmartPhonenode()  
    rclpy.spin(node)       
    rclpy.shutdown()       



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()