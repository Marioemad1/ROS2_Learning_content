#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from the_robot_msgs.msg import LedStateM
from the_robot_msgs.srv import LedState


class LED_Panal(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("LED_Panal") #call the init from the Node class 
        self.Leds_server_=self.create_service(LedState,"set_led",self.callback_led_service)
        self.led_state_publisher_=self.create_publisher(LedStateM,"led_state",10)
        self.timer_=self.create_timer(0.5,self.callback_publisher)
        self.responce_= LedState.Response()
        self.get_logger().info("The led server is running....")


    def callback_led_service(self, resquest:LedState.Request ,responce:LedState.Response ):
        if resquest.request[0] == 0 and resquest.request[1] == 0 and resquest.request[2] == 1:
            responce.response[2]= True
            self.responce_=responce
        else:
            responce.response[2]=False
            self.responce_=responce
        return responce
    
    
    
    def callback_publisher(self):
        msg= LedStateM()
        if self.responce_.response[2]==True:
            msg.led_state[2]=True
            self.led_state_publisher_.publish(msg)
        else:
            msg.led_state[2]=False
            self.led_state_publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=LED_Panal()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()