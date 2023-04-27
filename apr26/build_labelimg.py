import os

label_image_path = os.path.join('code', 'repo')
if not os.path.exists(label_image_path):
    if os.name == 'posix':   # Mac, Linux
        os.system(f'mkdir -p {label_image_path}')
    elif os.name == 'nt':  # Windows
        os.system(f'mkdir {label_image_path}')

    os.system(f'git clone https://github.com/tzutalin/labelImg {label_image_path}')

    if os.name == 'posix':
        os.system(f'cd {label_image_path} && make qt5py3')
    elif os.name == 'nt':
        os.system(f'cd {label_image_path} && pyrcc5 -o libs/resources.py resources.qrc')
    
    os.system(f'cd {label_image_path} && python  labelImg.py')