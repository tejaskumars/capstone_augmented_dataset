import os 
from pathlib import Path
import shutil

all_images = os.listdir(r"D:\movies\work\capstone\CapstoneDataset_Resized\resized\all_resized")
all_images_path = [os.path.join(r"D:\movies\work\capstone\CapstoneDataset_Resized\resized\all_resized" , i) for i in all_images]


all_images_batches = [all_images_path[i:i+5000] for i in range(0,len(all_images_path) , 5000)]
# print(len(all_images_path))

all_images_test = all_images_batches[0][:10]
all_images_test_batch = [all_images_test[i:i+5] for i in range(0,len(all_images_test) , 5)]


for i , batch in enumerate(all_images_test_batch):
    batch_len = len(batch)
    # print(len(batch))
    for image in batch:
        img_name = image.split("\\")[-1]
        new_path = os.path.join("D:\movies\work\capstone\capstone_augmented_dataset\dataset" , img_name)
        shutil.copy2(image , new_path)
        
    print("adding images to git...")
    os.system("git add .")
    print("added images to git...")
    os.system(f'git commit -m "automated commit -m adding {batch_len} images of batch {i}"')
    os.system("git push origin main")
    os.system("pushed the batch")