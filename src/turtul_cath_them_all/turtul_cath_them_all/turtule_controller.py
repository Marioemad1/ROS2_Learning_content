#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Kill
from the_robot_msgs.msg import LiveTurtuiles
from std_msgs.msg import Int16


class TurtuleController(Node): #create the class and inharet from node
    def __init__(self): 
        super().__init__("turtule_controller") #call the init from the Node class
        #the array of turtils
        self.list_of_trutles_= []
        
        #clinet to the kill serves
        self.kill_that_turule_ = self.create_client(Kill,"/kill")

        #the enable topic to make a sequance
        self.enable_=self.create_publisher(Int16,"enable",10)

        #the postion of the main turtle
        self.sub_pose1_=self.create_subscription(Pose,"/turtle1/pose",self.callback_pose_turtule1,10)

        #the command velcoity 
        self.cmd_pub_ = self.create_publisher(Twist,"/turtle1/cmd_vel",10)

        self.target_turtile_sub_= self.create_subscription(LiveTurtuiles,"live_turtiles", self.callback_sub_target_turtile,10)
        self.timer_= self.create_timer(0.01,self.go_to_target)
        self.main_turtule_postion_ :Pose = None
        self.get_logger().info("the controller is running...")

    def callback_sub_target_turtile(self, target_:LiveTurtuiles ):
        self.list_of_trutles_.append(target_)
        #self.get_logger().info(f"{self.list_of_trutles_}")

    def callback_pose_turtule1(self, postion :Pose ):
        self.main_turtule_postion_=postion
    

    def check_the_shortest(self):
        list_of_distance= []
        temp_list = []
        for t in self.list_of_trutles_:
            dis_x = t.target_x - self.main_turtule_postion_.x
            dis_y = t.target_y - self.main_turtule_postion_.y
            list_of_distance.append(math.sqrt((dis_x**2) + (dis_y**2)))

        temp_list=list_of_distance.copy()
        temp_list.sort()
        return list_of_distance.index(temp_list[0])

    
    def go_to_target(self):
        while not self.kill_that_turule_.wait_for_service(1.0):
                    self.get_logger().warn("waiting for the server...")
        
        if self.main_turtule_postion_ == None or len(self.list_of_trutles_) == 0  :
            msg = Int16()
            msg.data = 1
            self.enable_.publish(msg)
            return
        else:
            if len(self.list_of_trutles_) > 1:
               i=self.check_the_shortest()
            else:
               i=0
        

            t = self.list_of_trutles_[i] 


            dis_x = t.target_x - self.main_turtule_postion_.x
            dis_y = t.target_y - self.main_turtule_postion_.y
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
                kill_name = Kill.Request()
                kill_name.name = t.name
                self.list_of_trutles_.pop(i)
                future = self.kill_that_turule_.call_async(kill_name)


            self.cmd_pub_.publish(cmd_vel)





def main(args=None):
    rclpy.init(args=args)   #init the communication
    node=TurtuleController()   #create a object from the class
    rclpy.spin(node)        #make the node spin
    rclpy.shutdown()        #shutdow the node



#if the name main called in the terminal call the main function
if __name__ == "__main__":
    main()