#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/msg/string.hpp"//the msgs type that we will use to create the msg

class Smart_phone : public rclcpp::Node //create a class and inharet from the rclcpp
{
public: //puplic
    Smart_phone() : Node("Smart_phone_cpp") 
    {
        //assign the v and the methods
        subscriber_= this->create_subscription<example_interfaces::msg::String>("robot_news",10,
        std::bind(&Smart_phone::callback_robot_news,this,std::placeholders::_1));
        //this line above is to create sub giving it the type of msg and the topic name and q
        //also the bind to call the callback function and declare that its only one input in the callback
        RCLCPP_INFO(this->get_logger(),"smartphone_cpp_is running..."); 
    }   
private:
   //ctreate the callback function of print in terminal
   void callback_robot_news(const example_interfaces::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(),"%s",msg->data.c_str()); 
    }
    //the shated ptr of subscriber
    rclcpp::Subscription<example_interfaces::msg::String>::SharedPtr subscriber_;
 };

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Smart_phone>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
