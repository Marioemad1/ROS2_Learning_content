# ROS 2 Learning Portfolio 🤖

**Author:** Mario Emad Boles

Welcome to my **ROS 2 (Robot Operating System)** development workspace. This repository documents my journey mastering robotics software using both **C++** and **Python**. It moves from basic node creation to complex multi-node systems and custom interfaces.

## 📂 Workspace Structure & Packages

This workspace is organized into 5 core packages, each serving a specific learning purpose:

### 1. `my_cpp_pkg` (C++ Implementation)
Contains the C++ implementations of core ROS 2 concepts.
* **Basics:** `my_first_node` (OOP structure).
* **Topics (Pub/Sub):**
    * `robot_news_station` (Publisher) ➡ `smartphone` (Subscriber).
    * `number_publisher` ➡ `number_counter`.
* **Services (Client/Server):**
    * `add_two_ints_serv` (Server).
    * `add_two_ints_clinet` (OOP Client) & `add_two_int_clinet_no_oop`.
* **Hardware Simulation:**
    * `battery`, `led_Panal`, `hardware_robot_states` (Simulating hardware logic).

### 2. `my_py_pkg` (Python Implementation)
Mirrors the C++ package to demonstrate Pythonic ROS 2 development.
* **Basics:** `my_first_node`.
* **Topics:** `robot_news_station`, `smart_phone_sub`, `number_publisher`, `number_counter`.
* **Services:** `add_two_ints_serv`, `add_two_ints_clint`.
* **Hardware:** `battary`, `led_panal`, `my_hardware_status`.

### 3. `the_robot_msgs` (Custom Interfaces)
Defines custom data structures used by other packages to ensure modularity.
* **Messages (`.msg`):** `HardwareStatus.msg`, `LedStateM.msg`, `LiveTurtuiles.msg`.
* **Services (`.srv`):** `ComputeRectangleArea.srv`, `LedState.srv`.

### 4. `my_robot_bringup` (Launch System)
Manages the startup of multiple nodes and configurations using Python and XML launch files.
* **Launch Files:** `number_app.launch.py`, `robot_news_app.launch.xml`.
* **Project Launch:** `turtle_killer_app.launch.xml`.
* **Configuration:** `number_publisher.yaml` (Parameter loading).

### 5. `turtul_cath_them_all` (Capstone Project)
A "Turtle Catch" project (Game/Simulation) interacting with the Turtlesim simulator.
* **Nodes:**
    * `target_creater.py`: Spawns targets/turtles.
    * `turtule_controller.py`: Controls the main turtle to catch targets.

---

## 🛠️ Build Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd ros2_ws
    ```

2.  **Install Dependencies:**
    ```bash
    sudo rosdep init
    rosdep update
    rosdep install --from-paths src --ignore-src -r -y
    ```

3.  **Build the Workspace:**
    ```bash
    colcon build --symlink-install
    ```

4.  **Source the Environment:**
    ```bash
    source install/setup.bash
    ```

---

## 💻 Usage Examples

### Running the "Number Counter" System (C++)
This demonstrates a Publisher -> Subscriber relationship using standard Int64 messages.
```bash
# Terminal 1
ros2 run my_cpp_pkg number_publisher

# Terminal 2
ros2 run my_cpp_pkg number_counter
