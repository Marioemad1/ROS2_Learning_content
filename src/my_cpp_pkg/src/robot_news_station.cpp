#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/msg/string.hpp"//the msgs type that we will use to create the msg
using namespace std::chrono_literals;

class Robot_news_station : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Robot_news_station() : Node("Robot_news_station") , robot_name_("CPP03")
        {
            //assign the v and the methods
            publisher_ = this->create_publisher<example_interfaces::msg::String>("robot_news",10);
            //here we assigned ower shared ptr from type publisher to a publisher method that takes the type of msg the topic name and q of msg 
            timer_= this->create_wall_timer(0.5s,std::bind(&Robot_news_station::publisher,this));
            RCLCPP_INFO(this->get_logger(),"Robot news station has been started");
        }   
    private:
        void publisher()
        {
            auto msg = example_interfaces::msg::String(); //create the msg
            msg.data = std::string("this is ") + robot_name_ + std::string(" From the robot news"); //load the ms inside the msg
            publisher_->publish(msg);//from the shared ptr use publishe method and publish msg 
        }
        std::string robot_name_;
        rclcpp::Publisher<example_interfaces::msg::String>::SharedPtr publisher_;
        //the line above means we created a object of type published in type string msg from the lib we included and then make a shared ptr called publisher
        rclcpp::TimerBase::SharedPtr timer_; //creating a timer object 
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Robot_news_station>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}