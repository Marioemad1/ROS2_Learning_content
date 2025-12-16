#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

def main(args=None):
    rclpy.init(args=args)   
    node=Node("ADD_two_ints_clint_no_oop")  

    clint = node.create_client(AddTwoInts, "add_two_ints")     
     
    while not clint.wait_for_service(1.0):
        node.get_logger().warn("waiting for add to int server...")


    request = AddTwoInts.Request()
    request.a= 10
    request.b= 15

    future = clint.call_async(request)

    rclpy.spin_until_future_complete(node, future)

    responce= future.result()

    node.get_logger().info(str(responce))

    rclpy.shutdown()        



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()