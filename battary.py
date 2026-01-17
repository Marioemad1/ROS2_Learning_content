#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from the_robot_msgs.msg import LedStateM
from the_robot_msgs.srv import LedState

class My_custom_name(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("battary_clinet") #call the init from the Node class 
        self.bat_clinet_=self.create_client(LedState,"set_led")
        self.timer4s_= self.create_timer(4.0,self.call_empty_req)
        self.timer6s_= self.create_timer(6.0,self.call_full_req)
        self.timer6s_.cancel()
        self.get_logger().info("the Battary is running...")


    def call_empty_req(self):
        self.call_battary_state(True)

        self.timer4s_.cancel()
        self.timer6s_=self.create_timer(6.0,self.call_full_req)

    def call_full_req(self):
        self.call_battary_state(False)

        self.timer6s_.cancel()
        self.timer4s_=self.create_timer(4.0,self.call_empty_req)

    #the bool here means true->empty , false->full
    def call_battary_state(self,state: bool):
        while not self.bat_clinet_.wait_for_service(1.0):
            self.get_logger().warn("watting for the server... ")
        
        request = LedState.Request()
        
        if state == True:
            request.request = [0, 0, 1]
        else:
            request.request = [0, 0, 0]
        future = self.bat_clinet_.call_async(request)
        future.add_done_callback(self.callback_futrue)
    def callback_futrue(self, future):
        response=future.result()
        self.get_logger().info(f"{response.response}")

def main(args=None):
    rclpy.init(args=args)   
    node=My_custom_name()   
    rclpy.spin(node)        
    rclpy.shutdown()        



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()