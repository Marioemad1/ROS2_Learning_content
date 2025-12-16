#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "the_robot_msgs/srv/led_state.hpp"
#include "the_robot_msgs/msg/led_state_m.hpp"
using namespace std::placeholders;
class LedPanal : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        LedPanal() : Node("Led_panal") 
        {
            //assign the v and the methods
            led_panal_publisher_=this->create_publisher<the_robot_msgs::msg::LedStateM>("led_state",10);
            led_panal_server_=this->create_service<the_robot_msgs::srv::LedState>("set_led",
            std::bind(&LedPanal::callback_led_srv,this,_1,_2));
            RCLCPP_INFO(get_logger(),"The_led_panal_cpp_is_running...");

        }   
    private:
    //define the v of the class and the private methods
        rclcpp::Service<the_robot_msgs::srv::LedState>::SharedPtr led_panal_server_;
        rclcpp::Publisher<the_robot_msgs::msg::LedStateM>::SharedPtr led_panal_publisher_;


        void callback_led_srv(const the_robot_msgs::srv::LedState::Request::SharedPtr request , the_robot_msgs::srv::LedState::Response::SharedPtr responce)
        {
            auto msg = the_robot_msgs::msg::LedStateM();
            if (request->request[2]== 1 )
            {
                responce->response[2]=true;
                msg.led_state[2]=true;
                led_panal_publisher_->publish(msg);
            }
            else
            {

                responce->response[2]=false;
                msg.led_state[2]=false;
                led_panal_publisher_->publish(msg);
            }
            RCLCPP_INFO(this->get_logger(),"Rq is executed");
        }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<LedPanal>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
