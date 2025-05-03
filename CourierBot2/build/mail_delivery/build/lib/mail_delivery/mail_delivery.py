#!/usr/bin/env python3

# Copyright 2023 Clearpath Robotics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# @author Hilary Luo (hluo@clearpathrobotics.com)

import rclpy
import time

from turtlebot4_navigation.turtlebot4_navigator import TurtleBot4Directions, TurtleBot4Navigator


def main(args=None):
    rclpy.init(args=args)

    navigator = TurtleBot4Navigator()

    # Start on dock
    # if not navigator.getDockedStatus():
    #     navigator.info('Docking before intialising pose')
    #     navigator.dock()

    # Set initial pose
    # initial_pose = navigator.getPoseStamped([8.02,7.17], TurtleBot4Directions.SOUTH_EAST)
    # navigator.setInitialPose(initial_pose)

    # navigator.info("set initial pose")
    # time.sleep(3)

    # Give the system time to process the pose
    navigator.info("Waiting for amcl_pose to be received...")


    # Wait for Nav2
    navigator.waitUntilNav2Active()

    # Undock
    # navigator.undock()

    # Prepare goal pose options
    """ Listed here are the defualt 'locations' from
        the tutorial code. We can change these to
        whatever we need them to be """
    goal_options = [
        {'name': 'Dr. Sowell',
         'pose': navigator.getPoseStamped([12.7, 10.8], TurtleBot4Directions.NORTH_EAST)},

        {'name': 'Woods 119',
         'pose': navigator.getPoseStamped([-1.4, 3.5], TurtleBot4Directions.EAST)},

         {'name': 'Prof. Liu',
         'pose': navigator.getPoseStamped([6.9, 6.75], TurtleBot4Directions.SOUTH)},

         {'name': 'Dr. Hopkins',
         'pose': navigator.getPoseStamped([0.0, 4.3], TurtleBot4Directions.SOUTH)},

         {'name': 'Hallway',
         'pose': navigator.getPoseStamped([22.7, 0.28], TurtleBot4Directions.EAST)},

         {'name': '134 Back Door Side',
         'pose': navigator.getPoseStamped([32.0, -12.0], TurtleBot4Directions.WEST)},

         {'name': '134 Back Window Side',
         'pose': navigator.getPoseStamped([35.5, -10.5], TurtleBot4Directions.WEST)},

         {'name': '134 Front Door Side',
         'pose': navigator.getPoseStamped([28.3, -4.0], TurtleBot4Directions.EAST)},

         {'name': '134 Front Window Side',
         'pose': navigator.getPoseStamped([32.4, -3.25], TurtleBot4Directions.EAST)},

         {'name': 'Dr. C',
         'pose': navigator.getPoseStamped([23.5, -3.13], TurtleBot4Directions.NORTH)},

         {'name': 'Poster',
         'pose': navigator.getPoseStamped([25.7, -6.66], TurtleBot4Directions.SOUTH)},

         {'name': 'Woods 136',
         'pose': navigator.getPoseStamped([29.5, -15.0], TurtleBot4Directions.WEST)},

         {'name': 'Glass Doors',
         'pose': navigator.getPoseStamped([10.0, -16.5], TurtleBot4Directions.NORTH)},

         {'name': 'Plant',
         'pose': navigator.getPoseStamped([18.5, -13.0], TurtleBot4Directions.NORTH)},

         {'name': 'Intersection',
         'pose': navigator.getPoseStamped([26.8, -8.76], TurtleBot4Directions.SOUTH)},

        {'name': 'Exit',
         'pose': None},
    ]

    # tbh idk where this gets printed
    navigator.info('Welcome to the mail delivery service.')

    # core delivery loop
    while True:
        # Create a list of the goals for display
        options_str = 'Please enter the number corresponding to the desired robot goal position:\n'
        for i in range(len(goal_options)):
            options_str += f'    {i}. {goal_options[i]["name"]}\n'

        # Prompt the user for the goal location
        raw_input = input(f'{options_str}Selection: ')

        selected_index = 0

        # Verify that the value input is a number
        try:
            selected_index = int(raw_input)
        except ValueError:
            navigator.error(f'Invalid goal selection: {raw_input}')
            continue

        # Verify that the user input is within a valid range
        if (selected_index < 0) or (selected_index >= len(goal_options)):
            navigator.error(f'Goal selection out of bounds: {selected_index}')

        # Check for exit
        elif goal_options[selected_index]['name'] == 'Exit':
            break

        else:
            # Navigate to requested position
            navigator.startToPose(goal_options[selected_index]['pose'])

    rclpy.shutdown()


if __name__ == '__main__':
    main()
