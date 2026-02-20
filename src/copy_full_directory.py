import os
import shutil

def copy_complete_dir(src, dst, is_root=True):
    if is_root and os.path.exists(dst):  
        shutil.rmtree(dst)       #clears out the old version of the directory
    os.makedirs(dst, exist_ok=True)    #makes an empty version of the same destination
    
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            copy_complete_dir(src_path, dst_path, is_root=False)

    
    
    