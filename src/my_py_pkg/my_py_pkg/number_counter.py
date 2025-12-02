#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class Number_Counter(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("Number_Counter") #call the init from the Node class
        self.publiser_=self.create_publisher(Int64,"number_counter",10)
        self.subscriber_=self.create_subscription(Int64,"number",self.callback_subscriber_number,10)
        self.get_logger().info("number_counter is running...")
        self.counter_=0
        self.server_= self.create_service(SetBool,"rest_counter",self.callback_service_setbool)
     #here we used the same subcriber function to publish and this is a comman way to publish while you sub from another topic
    
    def callback_subscriber_number(self, mesg: Int64):
        self.counter_+=mesg.data
        #self.get_logger().info(str(mesg.data))
        masage = Int64()
        masage.data=self.counter_
        self.publiser_.publish(masage)
    
    def callback_service_setbool(self, request: SetBool.Request , responce: SetBool.Response ):
        if request.data:
            self.counter_= 0
            responce._success= True
            responce.message= "the counter is int to zero sucssfully"
            self.get_logger().info(f"{responce.message} : {responce._success} ")
        else:
            responce._success= False
            responce._message= "Watting to call true ..."
            self.get_logger().warn(f"{responce.message} : {responce._success} ")

        return responce
        
        



def main(args=None):
    rclpy.init(args=args)   
    node=Number_Counter()   
    rclpy.spin(node)        
    rclpy.shutdown()        



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()