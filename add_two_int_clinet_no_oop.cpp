#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::chrono_literals;

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("add_two_ints_clinet_no_oop"); //create the shared pointer of the my node

    auto clinet= node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
    while (! clinet->wait_for_service(1s))
    {
        RCLCPP_WARN(node->get_logger(),"Watting for the server....");

    }
    
    auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
    request->a = 5;
    request->b = 6;

    auto future = clinet->async_send_request(request);
    rclcpp::spin_until_future_complete(node, future);

    auto responce= future.get();
    RCLCPP_INFO(node->get_logger(),"%d + %d = %d" , (int) request->a , (int) request->b , (int) responce->sum );






    rclcpp::shutdown();
    return 0;

}
