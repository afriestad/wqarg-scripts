import os

from PIL import Image

IMGS_PATH = "./imgs"
STRIPS_PATH = "./large_strips"
COLUMNS = ((200, 210), (410, 420), (620, 630), (830, 840), (1040, 1050))

def main():
    files = os.listdir(IMGS_PATH)

    for filename in files:
        if filename.find("-", 1, 2) < 0 and os.path.isfile(f'{IMGS_PATH}/{filename}'):
            uuid = filename.split(".")[0]
            if os.path.isfile(f'{STRIPS_PATH}/{uuid}-0.png'):
                print(f'==> {uuid}-0.png exists, skipping')
                continue

            with Image.open(f'{IMGS_PATH}/{filename}') as f:
                _, height = f.size

                for i, (xmin, xmax) in enumerate(COLUMNS):
                    strip = f.crop((xmin, 103, xmax, height-103)).convert("RGB")
                    
                    strip.save(f'{STRIPS_PATH}/{uuid}-{i}.png', format="PNG")
                    print(f'{STRIPS_PATH}/{uuid}-{i}.png saved')



if __name__ == "__main__":
    main()
