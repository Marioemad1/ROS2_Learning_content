#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class My_custom_name(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("my_node_name") #call the init from the Node class 



def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=My_custom_name()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()