import re

import numpy as np
from claim import Claim
from itertools import product


def main():
    fabric_length = 1000
    fabric = np.zeros([fabric_length, fabric_length], dtype="U5")
    duplicated_fabric = 0
    claims = []
    with open("input.txt") as file:
        claims_input = file.readlines()
        for claim_input in claims_input:
            split_claim = re.split(' @ |,|: |x', claim_input.strip())
            claim = Claim(split_claim[0], int(split_claim[1]), int(split_claim[2]), int(split_claim[3]),
                          int(split_claim[4]))
            claims.append(claim)

    for claim in claims:
        for x, y in product(range(claim.left_space, claim.left_space + claim.width),
                            range(claim.top_space, claim.top_space + claim.height)):
            if '#' in fabric[x][y]:
                duplicated_fabric += 1
                fabric[x][y] = 'xx'
            elif fabric[x][y] == '':
                fabric[x][y] = claim.claim_id

    for claim in claims:
        claim_intact = True
        for x, y in product(range(claim.left_space, claim.left_space + claim.width),
                            range(claim.top_space, claim.top_space + claim.height)):
            if fabric[x][y] != claim.claim_id:
                claim_intact = False
                break
        if claim_intact:
            print(claim.claim_id)


if __name__ == "__main__":
    main()
