import os
import subprocess

def move_and_commit_files(src_dir, tgt_dir, batch_size, repo_dir):
    all_files = []
    for root, _, files in os.walk(src_dir):
        for file in files:
            all_files.append(os.path.join(root, file))
    
    batch_num = 1
    for i in range(0, len(all_files), batch_size):
        batch_folder = os.path.join(tgt_dir, f'Batch{batch_num}')
        os.makedirs(batch_folder, exist_ok=True)
        for file in all_files[i:i + batch_size]:
            relative_path = os.path.relpath(file, src_dir)
            target_path = os.path.join(batch_folder, relative_path)
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            shutil.move(file, target_path)
        
        # Git commands to add, commit, and push the batch
        subprocess.run(['git', '-C', repo_dir, 'add', '.'])
        commit_message = f'Adding batch {batch_num}'
        subprocess.run(['git', '-C', repo_dir, 'commit', '-m', commit_message])
        subprocess.run(['git', '-C', repo_dir, 'push'])

        batch_num += 1

    print(f'{batch_num - 1} batches created, files moved, and committed successfully.')

# Define your source and target directories, batch size, and repo directory
source_dir = 'your/source/directory'
target_dir = 'your/target/directory'
batch_size = 100
repo_dir = 'your/repo/directory'  # Local path to your cloned repo

# Run the function
move_and_commit_files(source_dir, target_dir, batch_size, repo_dir)
