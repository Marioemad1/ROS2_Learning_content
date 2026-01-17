#!/usr/bin/env python3
import rclpy
import random
import math
from rclpy.node import Node
from turtlesim.srv import Spawn
from the_robot_msgs.msg import LiveTurtuiles
from std_msgs.msg import Int16


class TargetCreater(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("spawn") #call the init from the Node class 
        self.random_turtiles_clinet_ = self.create_client(Spawn,"/spawn")
        self.alive_turtuiles_pub_ = self.create_publisher(LiveTurtuiles,"live_turtiles",10)
        self.enable_sub_ = self.create_subscription(Int16,"enable",self.enable_callback,10)
        self.enable_button = Int16()
        self.enable_button.data = 0
        self.live_turtile_ = LiveTurtuiles()
        self.turtile_name_:LiveTurtuiles.name = None
        self.HZ_turtiles_ = self.create_timer(0.8,self.create_turtuiles)
        self.get_logger().info("the spawn caller is running...")


    def enable_callback(self, msg: Int16):
        self.enable_button = msg

    def create_turtuiles(self):
        while not self.random_turtiles_clinet_.wait_for_service(1.0):
            self.get_logger().warn("waiting for the server...")
        
        while self.enable_button.data  == 0:
            self.get_logger().warn("waitting for the enable button")
            return
        
        
        linear_x = random.uniform(1.0,10.0)
        self.live_turtile_.target_x = linear_x 
        linear_y = random.uniform(1.0,10.0)
        self.live_turtile_.target_y = linear_y
        thata_spawn = random.uniform(0.0,math.pi)

        Spawn_turuile = Spawn.Request()

        Spawn_turuile.x     = linear_x
        Spawn_turuile.y     = linear_y
        Spawn_turuile.theta = thata_spawn

        future_ = self.random_turtiles_clinet_.call_async(Spawn_turuile)
        future_.add_done_callback(self.future_callback)


    def future_callback(self, future):
        responce = future.result()
        self.live_turtile_.name = responce.name
        self.alive_turtuiles_pub_.publish(self.live_turtile_)
        self.get_logger().info(f"the turtile: {responce.name} is created")



def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=TargetCreater()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()