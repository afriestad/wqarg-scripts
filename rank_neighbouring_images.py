import os
import json

from PIL import Image

SOURCE_PATH = "./strips"

def main():
    files = os.listdir(SOURCE_PATH)

    print(f"Reading {len(files)} strips into memory")
    strips = {}

    for filename in files:
        if os.path.isfile(f'{SOURCE_PATH}/{filename}'):
            with Image.open(f'{SOURCE_PATH}/{filename}', formats=["PNG"]) as f:
                strips[filename] = list(f.getdata())

    print("Files read")

    print("Comparing strips for clustering")

    comparisons = json.loads(open("comparisons.json", "r").read())
    for i, firstName in enumerate(strips.keys()):
        print(i)
        comparisons[firstName] = {}
        for j, secondName in enumerate(strips.keys()):
            if j <= i:
                continue
            if secondName in comparisons[firstName]:
                continue
            
            firstPixels = strips[firstName]
            secondPixels = strips[secondName]

            total_difference = 0
            for k in range(len(firstPixels)):
                r1, g1, b1 = firstPixels[k]
                r2, g2, b2 = secondPixels[k]

                weighted_pixel_difference = pow(abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2), 2)
                total_difference += weighted_pixel_difference
            
            comparisons[firstName][secondName] = total_difference
    
    print("Comparisons done.")

    print("Saving comparisons to file")
    
    with open("./comparisons.json", "w") as compfile:
        compfile.write(json.dumps(comparisons, sort_keys=True, indent=2))

    print("Comparisons saved to ./comparisons.json")


            





if __name__ == "__main__":
    main()