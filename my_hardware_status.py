#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from the_robot_msgs.msg import HardwareStatus

class HardWareState_Publisher(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("hardware_state_publisher") #call the init from the Node class
        self.publisher_= self.create_publisher(HardwareStatus,"Robot_state",10)
        self.timer_=self.create_timer(0.5,self.callback_publisher)
        self.get_logger().info("Hardwate_publisher_is running...")


    def callback_publisher(self):
        msg= HardwareStatus()
        msg.temperature= 40.7
        msg.are_motor_ready= True
        msg.debug_message= "every thing is well..."
        self.publisher_.publish(msg)
        #self.get_logger().info("the massage is published")




def main(args=None):
    rclpy.init(args=args)  
    node=HardWareState_Publisher()  
    rclpy.spin(node)       
    rclpy.shutdown()       



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()