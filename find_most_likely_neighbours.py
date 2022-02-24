import os
import json

def main():
    strips = json.loads(open("./comparisons.json", "r").read())

    print("Looking through all neighbours to find two most likely")

    probable_closest_neighbours = {}
    for strip in strips:
        if not strip in probable_closest_neighbours:
            probable_closest_neighbours[strip] = []

        neighbours = list(strips[strip].items())
        neighbours.sort(key=lambda x : x[1])

        new_neighbours = [*neighbours[:2], *probable_closest_neighbours[strip]]

        for peek_neighbours in new_neighbours:
            if not peek_neighbours[0] in probable_closest_neighbours:
                probable_closest_neighbours[peek_neighbours[0]] = [(strip, peek_neighbours[1])]

        new_neighbours.sort(key=lambda x : x[1])

        new_neighbours = new_neighbours[:2]

        probable_closest_neighbours[strip] = new_neighbours
    
    print("All neighbours parsed, closest matches found.")

    print("Saving matches to file")

    with open("./neighbours.json", "w") as f:
        f.write(json.dumps(probable_closest_neighbours, sort_keys=True, indent=2))
    
    print("Matches saved")
    


        






if __name__ == "__main__":
    main()