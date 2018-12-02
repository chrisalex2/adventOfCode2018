from collections import Counter
from itertools import combinations


def main():
    box_id_length = 26
    num_2_boxes = set([])
    num_3_boxes = set([])
    with open("input.txt") as file:
        box_ids = file.readlines()
        for box_id in box_ids:
            for occurrence in Counter(box_id.strip()).most_common(box_id_length):
                if occurrence[1] == 2:
                    num_2_boxes.add(box_id.strip())
                elif occurrence[1] == 3:
                    num_3_boxes.add(box_id.strip())

    compare_boxes(num_2_boxes.union(num_3_boxes), box_id_length)


def compare_boxes(boxes, box_id_length):
    for box_a, box_b in combinations(boxes, 2):
        count = 0
        common_id = ""
        for c1, c2 in zip(box_a, box_b):
            if c1 == c2:
                count += 1
                common_id = common_id + c1
        if count == box_id_length - 1:
            print(common_id)


if __name__ == "__main__":
    main()
