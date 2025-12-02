#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Add_Two_Ints_Node(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("add_two_ints_serv") #call the init from the Node class 
        self.server_= self.create_service(AddTwoInts,"add_two_ints",self.callback_addtwoints)
        self.get_logger().info("add_two_int_service run....")



    def callback_addtwoints(self,request: AddTwoInts.Request, responce: AddTwoInts.Response):
        responce.sum = request.a + request.b
        self.get_logger().info(f"{request.a}+{request.b}={responce.sum}")
        return responce



def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=Add_Two_Ints_Node()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()