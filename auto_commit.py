import os 
from pathlib import Path
import shutil
import time

all_images = os.listdir(r"D:\movies\work\capstone\augmented_images\all_augmented")
all_images_path = [os.path.join(r"D:\movies\work\capstone\augmented_images\all_augmented" , i) for i in all_images]


all_images_batches = [all_images_path[i:i+5000] for i in range(0,len(all_images_path) , 5000)]
print("total images" , len(all_images_path))


for i , batch in enumerate(all_images_batches):
    batch_len = len(batch)
    print("batch images length" ,len(batch))
    for image in batch:
        img_name = image.split("\\")[-1]
        new_path = os.path.join("D:\movies\work\capstone\capstone_augmented_dataset\dataset" , img_name)
        shutil.copy2(image , new_path)
        
    print("adding images to git...")
    os.system("git add .")
    print("added images to git...")
    os.system(f'git commit -m "automated commit adding {batch_len} augmented images of batch {i}"')
    os.system("git push origin main")
    print(f"\n\npushed the brach {i}\n\n")
    time.sleep(2)