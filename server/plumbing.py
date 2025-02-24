import json
from util import config_path, safe_open

def save_task(task):
    blob_idx = task["blob_idx"]
    blob_prefix = blob_idx[:2]

    with safe_open(f"{config_path()}/data/{blob_prefix}/{blob_idx}", "w") as f:
        json.dump(task, f, indent=2)

def load_task(blob_idx):
    blob_prefix = blob_idx[:2]
    with safe_open(f"{config_path()}/data/{blob_prefix}/{blob_idx}", "r") as f:
        return json.load(f)

def save_active(active):
    with safe_open(f"{config_path()}/active", "w") as f:
        json.dump(active, f, indent=2)

def load_active():
    try:
        with safe_open(f"{config_path()}/active", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Gives the task an ID. Either reuse next free slot or append to the end
def next_free_id(active, blob_idx):
    for i, other_idx in enumerate(active):
        if other_idx is None:
            active[i] = blob_idx
            return i
    # No free slot found so just append
    active.append(blob_idx)
    return len(active) - 1

def save_archive(month, archive):
    with safe_open(f"{config_path()}/archive/{month}", "w") as f:
        json.dump(archive, f, indent=2)

def load_archive(month):
    try:
        with safe_open(f"{config_path()}/archive/{month}", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
