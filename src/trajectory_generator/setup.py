from setuptools import setup

package_name = 'trajectory_generator'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='basti',
    maintainer_email='sebastian.mai@ovgu.de',
    description='a packge with planners to generate a trajectory',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'vehicle_model_node = trajectory_generator.vehicle_model_node:main',
            'direct_planner = trajectory_generator.direct_planner:main',
            'pso_planner = trajectory_generator.pso_planner:main',
            'continuous_planner = trajectory_generator.continuous_planner:main',
            'obstacle_inflation = trajectory_generator.obstacle_inflation:main',
        ],
    },
)
