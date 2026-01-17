#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "the_robot_msgs/srv/led_state.hpp"
using namespace std::chrono_literals;
using namespace std::placeholders;
class Battery : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Battery() : Node("battery_cpp"), battery_("fully")
        {
            clock_= this->get_clock();
            the_last_time_battery_changed = clock_->now();
            battery_client_ = this->create_client<the_robot_msgs::srv::LedState>("set_led");
            timer_= this->create_wall_timer(1s,std::bind(&Battery::call_check_battery_state,this));
            RCLCPP_INFO(get_logger(),"BatteryNode_Running....");

        }

    private:
    //define the v of the class and the private methods
        rclcpp::Client<the_robot_msgs::srv::LedState>::SharedPtr battery_client_ ;
        rclcpp::TimerBase::SharedPtr timer_;
        rclcpp::Clock::SharedPtr clock_;
        rclcpp::Time the_last_time_battery_changed;
        std::string battery_;

        void call_check_battery_state()
        {
            auto time_now = this->clock_->now();
            if(this->battery_ == "fully")
            {
                if(time_now-the_last_time_battery_changed > 4s)
                {
                    battery_="empty";
                    the_last_time_battery_changed=clock_->now();
                    callback_request_led(3,1);

                }
            }
            else if (this->battery_== "empty")
            {
                if (time_now-the_last_time_battery_changed > 6s)
                {
                    battery_="fully";
                    the_last_time_battery_changed=clock_->now();
                    callback_request_led(3,0);
                }
                
            }
        }


        void callback_request_led(int led_number, int led_state)
        {
            while ( !battery_client_->wait_for_service(1s))
            {
                RCLCPP_WARN(this->get_logger(),"Waitting for the server....");
            }

            auto request=std::make_shared<the_robot_msgs::srv::LedState::Request>();
            
            if (led_number==3 && led_state == 1)
            {
                request->request={0,0,1};
            }
            else if (led_number==3 && led_state == 0)
            {
                request->request={0,0,0};
            }
            else
            {
                request->request={0,0,0};
                RCLCPP_WARN(this->get_logger(),"Error in the input..");
            }


            this->battery_client_->async_send_request(request,std::bind(&Battery::future_callback,this,_1));
            
            
        }

        void future_callback(rclcpp::Client<the_robot_msgs::srv::LedState>::SharedFuture future)
        {
            auto responce = future.get();
            RCLCPP_INFO(this->get_logger(),"the responce: %d",(bool)responce->response[2]);
        }
        


};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Battery>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
