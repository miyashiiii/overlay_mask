from pathlib import Path

import cv2
import numpy as np

target_color = (255, 255, 255)
draw_color = [0, 0, 128]
draw_alpha = 0.5


def overlay_mask(img, mask):
    opaque_overlay = img.copy()
    opaque_overlay[np.all(mask == target_color, axis=-1)] = draw_color
    overlay_img = cv2.addWeighted(img, 1 - draw_alpha, opaque_overlay, draw_alpha, 1)
    return overlay_img


def main():
    input_dir = Path("input")
    img_path = input_dir / "img.jpg"
    mask_path = input_dir / "mask.png"

    img = cv2.imread(str(img_path))
    mask = cv2.imread(str(mask_path))

    overlay_img = overlay_mask(img, mask)

    cv2.imwrite("overlay.jpg", overlay_img)


if __name__ == "__main__":
    main()
