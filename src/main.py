from generate_pages_recursive import generate_pages_recursive
import os
import shutil


def the_dir_copy_function(source_dir_path, dest_dir_path):
    items_in_dir = os.listdir(source_dir_path)
    
    for item in items_in_dir:
        item_path = os.path.join(source_dir_path, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dest_dir_path)
            print(f"Copying: {item_path} -> {dest_dir_path}")
        else:
            item_dest_path = os.path.join(dest_dir_path, item)
            os.mkdir(item_dest_path)
            the_dir_copy_function(item_path, item_dest_path)
            
            
def main():
    target_path  = "public"
    if os.path.exists(target_path):
        shutil.rmtree(target_path)
    os.mkdir(target_path)
    source_dir_path = "static"
    dest_dir_path = "public"
    the_dir_copy_function(source_dir_path, dest_dir_path)
    
    generate_pages_recursive("content", "template.html", "public")
    
    
if __name__ == "__main__":
    main()