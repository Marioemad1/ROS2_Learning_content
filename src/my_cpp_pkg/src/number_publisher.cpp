#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/msg/int64.hpp"
using namespace std::chrono_literals;

class Number_Publisher : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Number_Publisher() : Node("Number_Publisher") 
        {
            publisher_=this->create_publisher<example_interfaces::msg::Int64>("CPP_number",10);
            timer_ = this->create_wall_timer(1.0s,std::bind(&Number_Publisher::publisher,this));
            RCLCPP_INFO(this->get_logger(),"Number Publisher started...");
            

        }   
    private:
    //define the v of the class and the private methods
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    void publisher ()
    {
        auto msg_ = example_interfaces::msg::Int64();
        msg_.data = 2;
        this->publisher_->publish(msg_);
    }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Number_Publisher>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
