#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStation(Node): 
    def __init__(self): 
        super().__init__("robot_news_station") 
        self.publisher_ = self.create_publisher(String, "robot_news", 10 )#this is the function that creates a publisher 
        self.robot_name_="C3PO"
        self.counter_=0
        #this function take (data of tha msg , name of the channal ,and a Q size like a connection protocol protect in the big msgs)              
        self.timer_=self.create_timer(0.5,self.publish_news)
        self.get_logger().info("robot_news_has_been_started")

    def publish_news(self):                                                                                #this is the publisher function which will contain msg we want to publish
        msg = String()                                                                                     #create a object of type string that will cary our msg
        msg.data= f"Hello this is  {self.robot_name_} and this the robot staion msg num {self.counter_}"#inside this object inside data we save the msg
        self.counter_+=1
        self.publisher_.publish(msg)                                                                       #now inside or pub object call the publisher method and passing the msg 

def main(args=None):
    rclpy.init(args=args)   
    node=RobotNewsStation() 
    rclpy.spin(node)        
    rclpy.shutdown()        




if __name__ == "__main__":
    main()