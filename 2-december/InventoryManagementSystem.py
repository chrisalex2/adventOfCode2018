from collections import Counter


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

    print(len(num_2_boxes) * len(num_3_boxes))


if __name__ == "__main__":
    main()
