import os

from PIL import Image

SOURCE_PATH = "./large_strips"
DESTINATION_PATH = "./strips"

def main():
    files = os.listdir(SOURCE_PATH)

    for filename in files:
        if os.path.isfile(f'{SOURCE_PATH}/{filename}'):
            if os.path.isfile(f'{DESTINATION_PATH}/{filename}'):
                        print(f'==> {filename} exists, skipping')
                        continue

            print(filename)

            with Image.open(f'{SOURCE_PATH}/{filename}', formats=["PNG"]) as f:
                width, height = f.size

                smallStrip = f.reduce(10)
                smallStrip.save(f"{DESTINATION_PATH}/{filename}")
                print(f'==> reduced')


if __name__ == "__main__":
    main()
