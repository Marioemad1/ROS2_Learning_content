#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::chrono_literals;
using namespace std::placeholders;



class Add_Two_Ints_Clinets : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Add_Two_Ints_Clinets() : Node("add_two_node_clinet") 
        {
            //assign the v and the methods
            clinet_= this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");

        }

        void callAddTwoInts(int a , int b) 
        {
            while (! clinet_->wait_for_service(1s))
            {
                RCLCPP_WARN(this->get_logger(),"Watting for the server...");
            }

            auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
            request->a = a;
            request->b = b;


            clinet_->async_send_request(request,std::bind(&Add_Two_Ints_Clinets::callback_calladd_two_ints,this, _1));
            
        }

    private:
    //define the v of the class and the private methods
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr clinet_;

    void callback_calladd_two_ints(rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future)
    {
        auto responce = future.get();


        RCLCPP_INFO(this->get_logger(),"Sum: %d",(int)responce->sum);
    }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Add_Two_Ints_Clinets>(); //create the shared pointer of the my node
    node->callAddTwoInts(10,5);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
