# ROS 2 Learning Project (Jazzy)

This repository documents my hands-on learning journey with ROS 2 (Robot Operating System), using the Jazzy distribution on Ubuntu 24.04.
The project focuses on understanding core ROS 2 concepts such as node creation, inter-node communication, and custom message handling. It serves as a foundational step toward building real-world robotic systems.

## Overview

This project demonstrates how different components in a robotic system communicate using ROS 2. It includes basic nodes, a publisher-subscriber system, and a custom message definition to simulate structured robot data exchange.

## Features Implemented

### 1. ROS 2 Workspace Setup

* Created a structured ROS 2 workspace (`ros2_ws`)
* Built using `colcon`

### 2. Custom ROS 2 Package

* Package: `my_first_pkg`
* Built using `ament_python`
* Contains core nodes for communication

### 3. Basic Node

* Implemented a simple ROS 2 node
* Used `rclpy` for logging and execution

### 4. Timer-Based Node

* Added periodic execution using ROS timers
* Demonstrates continuous node behavior

### 5. Publisher Node

* Publishes data to a topic
* Topics used: `/chatter` and `/robot_data`
* Demonstrates message broadcasting

### 6. Subscriber Node

* Subscribes to topics and receives data
* Logs incoming messages

### 7. Custom Message Package

* Package: `my_robot_msgs`
* Message: `RobotData.msg`

```text
float32 x
float32 y
float32 speed
```

* Used to simulate structured robot state data

---

## Concepts Covered

* ROS 2 architecture
* Nodes and topics
* Publisher–subscriber communication
* Timers
* Custom message creation
* Package structure
* Workspace build system (`colcon`)

---

## Technologies Used

* ROS 2 Jazzy
* Ubuntu 24.04
* Python (`rclpy`)
* Colcon build system

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ros2-learning-project.git
cd ros2-learning-project
```

### 2. Build the workspace

```bash
colcon build
source install/setup.bash
```

### 3. Run the publisher

```bash
ros2 run my_first_pkg publisher_node
```

### 4. Run the subscriber (in a separate terminal)

```bash
ros2 run my_first_pkg subscriber_node
```

---

## Expected Output

Publisher:

```
Publishing -> x: 1.0, y: 2.0, speed: 1.5
```

Subscriber:

```
Received -> x: 1.0, y: 2.0, speed: 1.5
```

---

## Learning Outcome

Through this project, I learned:

* How ROS 2 nodes communicate in a distributed system
* How to structure a ROS 2 workspace and packages
* How to define and use custom messages
* How real robotic systems exchange data between modules

---

## Future Work

* Implement ROS 2 services and actions
* Integrate Gazebo for simulation
* Add navigation (Nav2)
* Process sensor data (LiDAR and camera)
* Connect with real hardware (Raspberry Pi or Arduino)

## Recent Progress: Robot Modeling and Visualization

In this phase of the project, I extended the system from basic ROS 2 communication to actual robot modeling and visualization.

### URDF Robot Model

* Created a new package: `my_robot_description`
* Defined a robot using URDF (Unified Robot Description Format)
* Built a simple differential drive robot consisting of:

  * `base_link` (robot body)
  * `left_wheel` and `right_wheel`
  * Joints connecting wheels to the base

### TF (Transform) Understanding

* Learned how coordinate frames are structured in a robot
* Understood the relationship between:

  * Links (physical components)
  * Joints (connections)
  * TF tree (coordinate transformations)
* Debugged common TF issues such as:

  * Missing transforms
  * Incorrect fixed frame in RViz

### Robot State Publishing

* Used `robot_state_publisher` to publish transforms from URDF
* Integrated `joint_state_publisher` to simulate joint states
* Understood the pipeline:

  * Joint states → Transform computation → Visualization

### RViz Visualization

* Visualized the robot model in RViz
* Configured:

  * Fixed frame (`base_link`)
  * RobotModel display
  * TF display
* Debugged visualization errors and frame mismatches

### Geometry and Orientation Fixes

* Corrected wheel placement using joint origins
* Fixed wheel orientation using RPY (roll, pitch, yaw)
* Understood default axis alignment in URDF (cylinder along Z-axis)

### Key Learnings

* URDF defines structure, not behavior
* TF is essential for spatial understanding in robotics
* Visualization tools are critical for debugging
* Proper frame management is required for all robotic systems

---

This stage marks the transition from basic ROS 2 communication to building and understanding the physical structure of a robot, which is essential for simulation and real-world deployment.


---

## Author

Aditya Sonwane
Robotics learner focusing on ROS 2 and autonomous systems

---

## Note

This repository is part of an ongoing learning process and will continue to evolve with more advanced robotics concepts.
