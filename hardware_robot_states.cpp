#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "the_robot_msgs/msg/hardware_status.hpp"
using namespace std::chrono_literals;
class HardwareStates_publisher : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        HardwareStates_publisher() : Node("hardware_publisher_states") 
        {
            this->publisher_= this->create_publisher<the_robot_msgs::msg::HardwareStatus>("Robot_state",10);
            this->timer_=this->create_wall_timer(1.0s,std::bind(&HardwareStates_publisher::callback_publisher,this));
            RCLCPP_INFO(get_logger(),"the Hardware_publisher is running...");

        }   
    private:
    //define the v of the class and the private methods
    rclcpp::Publisher<the_robot_msgs::msg::HardwareStatus>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;

    void callback_publisher()
    {
        auto msg=the_robot_msgs::msg::HardwareStatus();
        msg.are_motor_ready = true;
        msg.temperature= 40.5;
        msg.debug_message= "every thing is good";

        this->publisher_->publish(msg);
    }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<HardwareStates_publisher>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
