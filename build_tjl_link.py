import json
import requests

from base64 import urlsafe_b64encode

MAPPING_URI = "https://tjl.co/wqarg/mapping.json"
NEIGHBOUR_FILE = "./neighbours.json"


def main():
    

    print("Fetching mappings")

    mapping = requests.get(MAPPING_URI).json()

    def map_to_mapping(position_tuple):
        filename, index = position_tuple
        uuid, strip_number = filename.split(".")[0].rsplit("-", 1);

        mappedUuid = mapping[uuid]

        return (f"{mappedUuid}-{int(strip_number) + 1}", index)

    print("Reading neighbours")

    neighbours = json.loads(open(NEIGHBOUR_FILE, "r").read())

    print("Ordering neighbours into list")

    order = []
    for strip in neighbours:
        if not strip in order:
            order.append(strip)

        current_index = order.index(strip)
        
        left_neighbour = neighbours[strip][0][0]
        if not left_neighbour in order:
            order.insert(current_index - 1, left_neighbour)

        if len(neighbours[strip]) > 1:
            right_neighbour = neighbours[strip][1][0]
            if not right_neighbour in order:
                order.insert(current_index, right_neighbour)
    
    print("Building TJL tool indexes")

    indexes = [(order[0], 0)]
    current_index = 1
    for i in range(1, len(order)):
        previous_filename = order[i-1]
        current_filename = order[i]

        
        #if not current_filename in list(map(lambda neighbour : neighbour[0], neighbours[previous_filename])):
         #   current_index += 1
        
        indexes.append((current_filename, current_index))

        current_index += 1
    
    indexes = list(map(map_to_mapping, indexes))

    blobbable = dict(indexes)

    blob = str(urlsafe_b64encode(json.dumps(blobbable).encode("utf-8")), "utf-8")

    print(f"https://tjl.co/wqarg/arrange.html#{blob}")

        







if __name__ == "__main__":
    main()