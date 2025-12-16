#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtuleController(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("turtule_controller") #call the init from the Node class
        self.target_x_ = 0.0
        self.target_y_ = 0.0
        self.sub_pose1_=self.create_subscription(Pose,"/turtle1/pose",self.callback_pose_turtule1,10)
        self.cmd_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.timer_= self.create_timer(0.01,self.go_to_target)
        self.main_turtule_postion_ :Pose = None
        self.get_logger().info("the controller is running...")

    def callback_pose_turtule1(self, postion :Pose ):
        self.main_turtule_postion_=postion
    
    def go_to_target(self):
        if self.main_turtule_postion_ == None :
            return
        
        dis_x = self.target_x_ - self.main_turtule_postion_.x
        dis_y = self.target_y_ - self.main_turtule_postion_.y
        distance = math.sqrt((dis_x**2) + (dis_y**2))

        cmd_vel = Twist()

        angel_target = math.atan2(dis_y,dis_x)
        dif_angel= angel_target - self.main_turtule_postion_.theta

        if distance > 0.5:
            cmd_vel.linear.x = 2*distance

            if dif_angel > math.pi:
                dif_angel -= 2*math.pi
            elif dif_angel < -math.pi:
                dif_angel += 2*math.pi

            cmd_vel.angular.z = 6*dif_angel
        else:
            cmd_vel.linear.x = 0.0
            cmd_vel.angular.z = 0.0

        self.cmd_pub_.publish(cmd_vel)





def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=TurtuleController()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()