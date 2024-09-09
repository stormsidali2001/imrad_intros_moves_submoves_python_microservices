from huggingface_hub import snapshot_download

print("Downloading  moves model ")
snapshot_download(
    repo_id="stormsidali2001/IMRAD_introduction_moves_classifier",
    local_dir="./tensorflow-models/models/moves/1",
)

print("Downloading move 0  sub moves model ")
snapshot_download(
    repo_id="stormsidali2001/IMRAD-introduction-move-zero-sub-moves-classifier",
    local_dir="./tensorflow-models/models/sub_moves_0/1",
)


print("Downloading move 1  sub moves model ")
snapshot_download(
    repo_id="stormsidali2001/IMRAD-introduction-move-one-sub-moves-classifier",
    local_dir="./tensorflow-models/models/sub_moves_1/1",
)


print("Downloading move 2  sub moves model ")
snapshot_download(
    repo_id="stormsidali2001/IMRAD-introduction-move-two-sub-moves-classifier",
    local_dir="./tensorflow-models/models/sub_moves_2/1",
)
