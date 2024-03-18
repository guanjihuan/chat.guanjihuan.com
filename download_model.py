# pip install --upgrade huggingface_hub

from huggingface_hub import snapshot_download

snapshot_download(repo_id="THUDM/chatglm3-6b-32k", local_dir = './THUDM/chatglm3-6b-32k', local_dir_use_symlinks=False)