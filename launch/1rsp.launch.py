# Example of what to look for in your launch file
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rover',  # Change this from 'Rover' to 'rover'
            executable='your_executable_name',
            name='rover_node',
            output='screen',
            parameters=[{
                'param_name': 'param_value'
            }]
        )
    ])

