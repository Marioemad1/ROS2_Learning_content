#include "rclcpp/rclcpp.hpp" //importing the ros2 lib if it shows a error open vs from the terminal
#include "example_interfaces/srv/add_two_ints.hpp"
using namespace std::placeholders;

class Add_two_Ints_serv : public rclcpp::Node //create a class and inharet from the rclcpp
{
    public: //puplic
        Add_two_Ints_serv() : Node("Add_two_ints") 
        {
            //assign the v and the methods
            server_= this->create_service<example_interfaces::srv::AddTwoInts>("add_two_ints",
                                        std::bind(&Add_two_Ints_serv::callback_add_two_int,this,_1,_2));
            RCLCPP_INFO(this->get_logger(),"the CPP add two int in running...");

        }   
    private:
    //define the v of the class and the private methods
        rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;

        void callback_add_two_int(const example_interfaces::srv::AddTwoInts::Request::SharedPtr request,
                                  const example_interfaces::srv::AddTwoInts::Response::SharedPtr responce )
        {
            responce->sum= request->a + request->b ;
            RCLCPP_INFO(this->get_logger(),"%d + %d = %d" , (int) request->a , (int) request->b , (int) responce->sum );
        }
};

int main(int argc,char **argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<Add_two_Ints_serv>(); //create the shared pointer of the my node
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}
