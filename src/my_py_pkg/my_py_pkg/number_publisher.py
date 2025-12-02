#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class Number_Publisher(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("Number_Publisher") #call the init from the Node class
        self.publisher_=self.create_publisher(Int64,"number",10)
        self.timer_=self.create_timer(0.5,self.Publish_number)
        self.msg = Int64() #don't forget to treat this as class not varible
        self.msg.data= 2
        self.get_logger().info("Number_Publisher node is running.....")

    def Publish_number(self):
        self.publisher_.publish(self.msg)


def main(args=None):
    rclpy.init(args=args)   
    node=Number_Publisher()   
    rclpy.spin(node)      
    rclpy.shutdown()        



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()