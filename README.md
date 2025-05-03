# CourierBot

## Table of Contents

[Installation](##installation)

[How to run](##how-to-run)

[Known Issues](##known-issues)

[Assumptions](##assumptions)

## Installation

The simplest way to use the CourierBot code is to download the relevant files and then use ROS 2's `colcon build` function to turn
your package into a usable program. Follow the following steps to setup your workspace directory:

    
1. A contained directory for you source files is needed. In a terminal run the 
    command `mkdir -p ~/your_ros2_ws/src/mail_delivery/mail_delivery`

2. This will create a number of nested directories in your home directory. In the mail_delivery
    directory, copy the two python files (\__init\__.py, and mail_delivery.py) found in the 
    CourierBot2/src/mail_delivery/mail_delivery directory of this repository.

   The CourierBot2 directory has the most recently updated code.

4. Next navigate to your root `mail_delivery` directory and make a directory for the project's 
    map files with the command `mkdir maps`. This is where you should place the map files you 
    have.

5. Now you can navigate to the root directory of your workspace with the command `cd ~/your_ros2_ws`.
    If you have not already installed colcon, do so with the command `sudo apt install python3-colcon-common-extensions`.
    Next, run the command `colcon build --symlink-install`.
    After the build is finished, you should see the `build`, `install`, and `log` directories. 

6. Navigate to your root `mail_delivery` directory and edit the `setup.py` file. Make sure the 
    last section of code looks like:
    ```
    entry_points={
        'console_scripts': [
            'mail_delivery = mail_delivery.mail_delivery:main'
    ]
   ```


## How to run

In order to make sure all pieces of the program are running correctly, it is 
recommended to start every piece of the code individually. There are four pieces needed
to run this program:

1. Turtlebot4 localization
2. Turtlebot4 nav2
3. Turtlebot4 RViz
4. mail_delivery code

The recommended order of starting this programs and how to start them is as follows:

1. Turtlebot4 nav2 localization

    This part of the code can be run with the following command:
    ```
   ros2 launch turtlebot4_navigation localization.launch.py map:=<path_to_your_yaml_map_file>
   ```
    This should begin the nav2 localization process. If the output messages seem to get stuck,
    quit the launch process and start again

2. Turtlebot4 nav2

    This part of the code can be run with the following command:
    ```
   ros2 launch turtlebot4_navigation nav2.launch.py
   ```
    This should begin the actual nav2  process. Again, if the output messages seem to get stuck,
    quit the launch process and start again

3. Turtlebot4 RViz

    This part of the code can be run with the following command:
    ```
   ros2 launch turtlebot4_viz view_navigation.launch.py
   ```
    This should begin the RViz window through which you can see your map. This piece of the
    program is not known to cause lots of issues, so it should be able to be run with no worries.

4. mail_delivery code

    This part of the code can be run with the following command:
    ```
   ros2 launch mail_delivery mail_delivery
   ```
    This should begin the mail_delivery code from this repository. When the amcl messages from the
    localization process are recognized by this code, you can start sending your turtlebot to locations
    on your map. If there are issues with loading this piece of the code, it is recommended to terminate
    this process, along with the previous three processes that you just started, and launch them again.


## Known Issues

It is a very common occurrence for one of the Turtlebot4 navigation servers to not initialize themselves
correctly. This is why the recommended course of starting this program is to run them one at a time and see
where the error is happening. 

## Assumptions

These instructions assume that you are using a Turtlebot4.

These instructions assume that you have ROS 2 Jazzy installed and configured. 
If that is not the case, instructions for how to install and configure ROS 2 Jazzy can be found 
[here](https://docs.ros.org/en/jazzy/Tutorials.html "ROS 2 Tutorials").

These instructions assume that you have already built a map using SLAM, or you know how to. 
If that is not the case, instructions for how to build your map can be found 
[here](https://turtlebot.github.io/turtlebot4-user-manual/tutorials/generate_map.html "Turtlebot4 map generation instructions").
