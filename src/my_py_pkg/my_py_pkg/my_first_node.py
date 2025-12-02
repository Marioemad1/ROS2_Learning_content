#/usr/bin/env/ python3
import rclpy
from rclpy.node import Node

class MyNode(Node):                                             #creating a class and inheart the Node class in it  
    def __init__(self):                                         #define the atributes
        super().__init__("my_1_node")                           #now inside the Node class use the __init__function to define the node name
        self.get_logger().info("hello world")                   #now use the get_logger function to print in the terminal
        self.__counter=0
        self.freq=1.0
        self.create_timer(self.freq,self.timer_callback)        #create a timer that take the time to repet and the function to call

    def timer_callback(self):                               #the function that the timer will call 
            self.get_logger().info(f"hello world {self.__counter}")
            self.__counter+=1 

def main(args=None):                        #create the main function
    rclpy.init(args=args)                   #setup the communication
    node=MyNode()                           #createing a MyNode OBJECT
    #node.get_logger().info("hello world")  print in the terminal  but now we moved it to the class
    rclpy.spin(node)                        #this will make the program spins until we hir ctr-c
    rclpy.shutdown()                        #shutdown the node

#this if condation is for running the main file in the terminal 

if __name__=="__main__":
    main()

