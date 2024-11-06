import os
import shutil

def move_files(src_dir, tgt_dir, batch_size):
    all_files = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    
    batch_num = 1
    for i in range(0, len(all_files), batch_size):
        batch_folder = os.path.join(tgt_dir, f'Batch{batch_num}')
        os.makedirs(batch_folder, exist_ok=True)
        for file in all_files[i:i + batch_size]:
            # Create the same sub-directory structure in the batch folder
            relative_path = os.path.relpath(file, src_dir)
            target_path = os.path.join(batch_folder, relative_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.move(file, target_path)
        batch_num += 1

    print(f'{batch_num - 1} batches created and files moved successfully.')


# Define your source and target directories and batch size
source_dir = r'C:/Users/bryan/OneDrive/Documents/Blogging/Blogging platforms/Github/RUP/RUP'
target_dir = r'C:\Users\bryan\OneDrive\Documents\Blogging\Blogging platforms\Github\RUP\Batches'
batch_size = 99

# Run the function
move_files(source_dir, target_dir, batch_size)