#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/msg/int64.hpp"
#include "example_interfaces/srv/set_bool.hpp"
using namespace std::chrono_literals;
using namespace std::placeholders;

class Number_Counter : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Number_Counter() : Node("Number_Counter") , counter_(0)
        {
            //assign the v and the methods
            this->publisher_=this->create_publisher<example_interfaces::msg::Int64>("number_counter",10);
            this->subscriber_=this->create_subscription<example_interfaces::msg::Int64>("CPP_number",10,
            std::bind(&Number_Counter::callback_subscriber,this,_1));
            RCLCPP_INFO(this->get_logger(),"The counter started...");


            this->server_= this->create_service<example_interfaces::srv::SetBool>("number_reset_counter",
                                                std::bind(&Number_Counter::callback_setbool,this, _1, _2));

        }   
    private:
    //define the v of the class and the private methods
    rclcpp::Publisher<example_interfaces::msg::Int64>::SharedPtr publisher_;
    rclcpp::Subscription<example_interfaces::msg::Int64>::SharedPtr subscriber_;
    rclcpp::Service<example_interfaces::srv::SetBool>::SharedPtr server_;
    int64_t counter_ ;

    void callback_subscriber(const example_interfaces::msg::Int64::SharedPtr msg)
    {
        auto temp = example_interfaces::msg::Int64();
        this->counter_+= msg->data;
        temp.data= counter_;

        this->publisher_->publish(temp);
    }

    void callback_setbool(const example_interfaces::srv::SetBool::Request::SharedPtr request ,
                          const example_interfaces::srv::SetBool::Response::SharedPtr responce)
    {
        if(request->data)
        {
            this->counter_=0;
            responce->success= 1;
            responce->message= "The counter is zero now: %d",responce->success ;
            RCLCPP_INFO(this->get_logger(),"The counter is zero now: %d",responce->success);
        }
        else
        {
            responce->success= 0;
            responce->message= "Sending false Waite for  true : %d",responce->success ;
            RCLCPP_WARN(this->get_logger(),"Sending false Waite for  true : %d",responce->success);
        }
    }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Number_Counter>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
