from PIL import Image
import os

# 入力フォルダ（再帰的に検索）
input_root = "./static/img"

# 目標比率（横:縦） → 148:210 = 7:10
TARGET_RATIO = 148 / 210


def crop_to_ratio(img, target_ratio):
    width, height = img.size
    current_ratio = width / height

    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        box = (0, 0, new_width, height)
    else:
        new_height = int(width / target_ratio)
        box = (0, 0, width, new_height)

    return img.crop(box)


for root, _, files in os.walk(input_root):
    for filename in files:
        if filename.lower().endswith("_top.jpg"):
            path = os.path.join(root, filename)
            try:
                with Image.open(path) as img:
                    cropped = crop_to_ratio(img, TARGET_RATIO)
                    cropped.save(path)  # 上書き保存
                    print(f"Cropped (overwritten): {path}")
            except Exception as e:
                print(f"Error processing {path}: {e}")

print("すべて完了しました。")
