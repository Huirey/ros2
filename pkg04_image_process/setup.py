from setuptools import find_packages, setup

package_name = 'pkg04_image_process'

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
    maintainer='wjh',
    maintainer_email='huirey@foxmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'cam_pub = pkg04_image_process.cam_pub:main',
            'cam_sub = pkg04_image_process.cam_sub:main',
        ],
    },
)
