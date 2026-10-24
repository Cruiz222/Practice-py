class TwoSum:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def find_indices(self, target: int) -> list[int]:
        indices = [index for index, value in enumerate(self.nums) if value == target]

        return indices