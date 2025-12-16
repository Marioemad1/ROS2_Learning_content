#include "rclcpp/rclcpp.hpp" 

class MyNode : public rclcpp::Node //creating a class that inherits from rclcpp::Node
{
     public:
        MyNode(): Node("cpp_test"), counter_(0) 
        {

            RCLCPP_INFO(this->get_logger(),"Hello World from MyNode class"); //this-> is used to refer to the current object instance

            timer_ = this->create_wall_timer(std::chrono::seconds(1),std::bind(&MyNode::timercallback,this)); //creating a wall timer that calls the timercallback function every second

        }
     private:
        void timercallback() //defining the timer callback function
        {
            RCLCPP_INFO(this->get_logger(),"Hello World from MyNode class %d",counter_);
            counter_++;
        }
        rclcpp::TimerBase::SharedPtr timer_; //creating a private timer pointer
        int counter_;                        //creating a private counter variable
};

int main(int argc,char **argv )
{
    rclcpp::init(argc, argv); //the ros2 communications init


    auto node = std::make_shared<MyNode>();         //creating a shared pointer to assign the a object
   // RCLCPP_INFO(node->get_logger(),"Hello World");  //to print in the terminal you hve to call the RCLCPP_INFO FUNC like macro
                                                    //and give it the (node->) the content inside the pointer means the object
                                                    //and call the logger func giving it the ,"msg"
    rclcpp::spin(node); //to keep the node alive and processing callbacks
    rclcpp::shutdown();//shut down the ros2 node
    return 0;//returning zero to elemenat the fuunction
}