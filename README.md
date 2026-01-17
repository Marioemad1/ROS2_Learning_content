# ROS2 Learning Content

My ROS2 files that I created throughout my learning path.

## 📋 Overview

This repository contains various ROS2 packages and examples that I've built while learning ROS2 (Robot Operating System 2). It serves as a personal collection of implementations, experiments, and practice projects covering different ROS2 concepts.

## 🚀 Features

- **Custom ROS2 Packages**: Various packages demonstrating different ROS2 functionalities
- **C++ and Python Implementations**: Examples in both programming languages
- **Publisher/Subscriber Examples**: Basic communication patterns
- **Service/Client Examples**: Request-response communication
- **Action Examples**: Long-running tasks with feedback
- **Custom Messages and Services**: Interface definitions

## 🛠️ Prerequisites

- **OS**: Ubuntu 22.04 (Jammy Jellyfish)
- **ROS2 Distribution**: Humble Hawksbill (or specify your version)
- **Build System**: colcon
- **Dependencies**: 
  - `ros-humble-desktop` (or your ROS2 distro)
  - `python3-colcon-common-extensions`
  - `python3-rosdep`

## 📦 Installation

### 1. Clone the Repository

```bash
cd ~
git clone https://github.com/Marioemad1/ROS2_Learning_content.git ros2_ws
cd ros2_ws
```

### 2. Install Dependencies

```bash
# Update rosdep
sudo rosdep init  # Only if not initialized before
rosdep update

# Install package dependencies
rosdep install --from-paths src --ignore-src -r -y
```

### 3. Build the Workspace

```bash
# Source ROS2
source /opt/ros/humble/setup.bash

# Build all packages
colcon build

# Source the workspace
source install/setup.bash
```

## 🎯 Usage

### Running Examples

After building and sourcing the workspace, you can run different packages:

```bash
# Example: Run a publisher node
ros2 run <package_name> <node_name>

# Example: Launch a launch file
ros2 launch <package_name> <launch_file.py>
```

### List Available Packages

```bash
# See all packages in this workspace
colcon list
```

## 📚 Package Overview

### 1. my_py_pkg
- **Language**: Python
- **Description**: Python-based ROS2 nodes demonstrating basic ROS2 concepts
- **Type**: Learning examples and practice implementations

### 2. my_cpp_pkg
- **Language**: C++
- **Description**: C++ ROS2 nodes for performance-critical operations
- **Type**: C++ implementation examples

### 3. turtul_cath_them_all
- **Language**: Python
- **Description**: Interactive turtle simulation project (likely a multi-turtle management/catching game)
- **Type**: TurtleSim-based learning project

### 4. the_robot_msgs
- **Type**: Custom Messages & Services Package
- **Description**: Custom ROS2 message and service definitions
- **Contains**:
  - Custom `.msg` files for specialized data structures
  - Custom `.srv` files for service definitions

### 5. my_robot_bringup
- **Type**: Launch & Configuration Package
- **Description**: Launch files and configuration parameters for bringing up robot systems
- **Contains**:
  - Launch files for starting multiple nodes
  - Configuration files (YAML) for parameter management

## 🗂️ Repository Structure

```
ros2_ws/
├── src/
│   ├── my_py_pkg/              # Python ROS2 nodes
│   ├── my_cpp_pkg/             # C++ ROS2 nodes
│   ├── turtul_cath_them_all/   # Turtle simulation project
│   ├── the_robot_msgs/         # Custom messages & services
│   └── my_robot_bringup/       # Launch files & configs
├── build/                       # Build artifacts (ignored)
├── install/                     # Install files (ignored)
├── log/                         # Build logs (ignored)
└── README.md
```

## 📖 Learning Resources

Resources I used while learning:

- [ROS2 Official Documentation](https://docs.ros.org/en/humble/)
- [ROS2 Tutorials](https://docs.ros.org/en/humble/Tutorials.html)
- [ROS2 Design Concepts](https://design.ros2.org/)

## 🤝 Contributing

This is a personal learning repository, but suggestions and improvements are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -m 'Add some improvement'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 Notes

- This repository is a work in progress as I continue learning ROS2
- Some packages may be experimental or incomplete
- Feel free to use any code for your own learning purposes

## 📧 Contact

**Mario Emad**
- GitHub: [@Marioemad1](https://github.com/Marioemad1)

## 📄 License

This project is open source and available for educational purposes.

---

**Last Updated**: January 2026

⭐ If you found this helpful, please consider giving it a star!
