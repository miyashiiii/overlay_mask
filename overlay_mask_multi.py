from pathlib import Path

import cv2

from overlay_mask import overlay_mask


def overlay_mask_multi(glob_str, replace_old, replace_new):
    input_dir = Path("input")
    output_dir = Path("output")

    for img_path in input_dir.glob(glob_str):
        img = cv2.imread(str(img_path))
        mask = cv2.imread(str(input_dir / img_path.name.replace(replace_old, replace_new)))
        if mask is None:
            continue
        overlay_img = overlay_mask(img, mask)
        cv2.imwrite(str(output_dir / img_path.name), overlay_img)


def main():
    overlay_mask_multi("*.jpg", ".jpg", ".mask.png")


if __name__ == "__main__":
    main()
