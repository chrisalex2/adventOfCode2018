class Claim(object):
    claim_id = ""
    left_space = 0
    top_space = 0
    width = 0
    height = 0

    def __init__(self, claim_id, left_space, top_space, width, height):
        self.claim_id = claim_id
        self.left_space = left_space
        self.top_space = top_space
        self.width = width
        self.height = height
