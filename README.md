# ROS Intro Tutorial - My Robot Controller 🚀

Welcome to the **ROS Intro Tutorial** repository! This project contains a simple **robot controller** built using **ROS (Robot Operating System)** to control a simulated turtle in `turtlesim`. The robot follows a path and can draw shapes like flowers in the simulation.  

---

## 📌 Features
✅ Move the robot in different patterns (straight, circular, flower)  
✅ Obstacle detection & wall avoidance  
✅ ROS node for controlling the robot  
✅ Uses `turtlesim` for visualization  

---

## 📂 Repository Structure
```
/my_robot_controller
│── /scripts         # Python scripts for controlling the robot
│── /launch          # ROS launch files
│── /config          # Configuration files
│── README.md        # Project documentation
```

---

## 🛠️ Installation & Usage
### 1️⃣ Clone the Repository
```bash
cd ~/catkin_ws/src
git clone https://github.com/NabilHassan11/ROS_Intro_Tut.git
cd ~/catkin_ws
catkin_make
```

### 2️⃣ Run the TurtleSim Node
```bash
roscore &  
rosrun turtlesim turtlesim_node
```

### 3️⃣ Run the Robot Controller
```bash
rosrun my_robot_controller draw_flower.py
```

---

## 📷 Demo Screenshot
![Turtle Drawing a Flower](images/flower_sim.png)

---

## 🤖 Dependencies
- ROS (Noetic or Melodic)
- Python 3
- `turtlesim`

---

## 📩 Contributing
Feel free to fork this repo, make changes, and submit a pull request!  

🚀 Happy coding!
