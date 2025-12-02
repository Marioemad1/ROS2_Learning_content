from setuptools import find_packages, setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='mario',
    maintainer_email='mario@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={ # here in this list you create the execute entries inside the list
                   #so we can call them in the ros2 commands 
        'console_scripts': [
            "py_node = my_py_pkg.my_first_node:main" ,# name for exe taple = pkg name.the node name:the function you wnat to call
            "robot_news_station = my_py_pkg.robot_news_station:main" ,
            "smart_phone= my_py_pkg.smart_phone_sub:main ",
            "number_publisher= my_py_pkg.number_publisher:main",
            "number_counter= my_py_pkg.number_counter:main ",
            "add_two_ints= my_py_pkg.add_two_ints_serv:main",
            "add_two_ints_clint_no_oop= my_py_pkg.add_two_ints_clint_no_oop:main",
            "add_two_clinet= my_py_pkg.add_two_ints_clint:main",
            "hardware_publisher= my_py_pkg.my_hardware_status:main",
            "led_panal= my_py_pkg.led_panal:main",
            "battary= my_py_pkg.battary:main"
        ],
    },
)
