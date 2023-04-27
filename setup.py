from distutils.core import setup
from setuptools import find_packages
import subprocess
import platform
if platform.system() == "Windows":
    from distutils import _msvccompiler
    _msvccompiler.PLAT_TO_VCVARS['win-amd64'] = 'amd64'

# subprocess.call(args='cd pointnet2 && python setup.py install && cd ../knn && python setup.py install',
#                 shell=True)

setup(
    name='graspnet',
    version='1.0.0',
    description='graspnet',
    author='Han Jianwei',
    author_email='hanjianwei92@163.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'transforms3d==0.3.1',
        'open3d>=0.8.0.0',
        'trimesh',
        'tqdm',
        'Pillow',
        'opencv-python',
        'pillow',
        'matplotlib',
        'pywavefront',
        'trimesh',
        'scikit-image',
        'autolab_core',
        'autolab-perception',
        'cvxopt',
        'dill',
        'h5py',
        'sklearn',
        'grasp_nms',
        'tensorboard'
    ],
    zip_safe=False
)
