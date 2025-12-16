#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class Add_two_int_Clint(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("add_two_int_clint") #call the init from the Node class
        self.client_=self.create_client(AddTwoInts,"add_two_ints")


    def call_add_two_int(self , a , b):
        while not self.client_.wait_for_service(1.0):
            self.get_logger().warn("waiting for the server...")

        request   = AddTwoInts.Request()
        request.a = a
        request.b = b


        future = self.client_.call_async(request)

        future.add_done_callback(self.callback_add_two_ints)

    def callback_add_two_ints(self, future):
        responce= future.result()
        self.get_logger().info(f"Got the responce: {responce.sum}")


def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=Add_two_int_Clint()   #create a object from the class
    node.call_add_two_int(10,11)
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()