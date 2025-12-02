cmake_minimum_required(VERSION 3.8)
project(my_cpp_pkg)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(example_interfaces REQUIRED)
find_package(the_robot_msgs REQUIRED)

add_executable(cpp_node src/my_first_node.cpp)
ament_target_dependencies(cpp_node rclcpp)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable(robot_news_station src/robot_news_station.cpp)
ament_target_dependencies(robot_news_station rclcpp example_interfaces)

add_executable(smartphone src/smartphone.cpp)
ament_target_dependencies(smartphone rclcpp example_interfaces)

add_executable(number_publisher src/number_publisher.cpp)
ament_target_dependencies(number_publisher rclcpp example_interfaces)

add_executable(number_counter src/number_counter.cpp)
ament_target_dependencies(number_counter rclcpp example_interfaces)

add_executable(add_two_ints_serv src/add_two_ints_serv.cpp)
ament_target_dependencies(add_two_ints_serv rclcpp example_interfaces)

add_executable(add_two_int_clinet_no_oop src/add_two_int_clinet_no_oop.cpp)
ament_target_dependencies(add_two_int_clinet_no_oop rclcpp example_interfaces)

add_executable(add_two_int_clinet src/add_two_ints_clinet.cpp)
ament_target_dependencies(add_two_int_clinet rclcpp example_interfaces)

add_executable(hardware_robot_states src/hardware_robot_states.cpp)
ament_target_dependencies(hardware_robot_states rclcpp the_robot_msgs)



install(TARGETS 
#don't forget to add the nodes in the targets
cpp_node 
robot_news_station
smartphone
number_publisher
number_counter
add_two_ints_serv
add_two_int_clinet_no_oop
add_two_int_clinet
hardware_robot_states
DESTINATION lib/${PROJECT_NAME}

)

ament_package()
