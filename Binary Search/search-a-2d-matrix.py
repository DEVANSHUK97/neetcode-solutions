class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        vert_l = 0
        vert_h = len(matrix) - 1

        while vert_l <= vert_h:
            vert_mid = (vert_l + vert_h)//2
            if matrix[vert_mid][0] == target:
                return True
            elif matrix[vert_mid][0] < target:
                vert_l = vert_mid + 1
            else:  # matrix[vert_mid][0] > target:
                vert_h = vert_mid - 1

        hrzn_l = 0
        hrzn_h = len(matrix[0]) - 1

        while hrzn_l <= hrzn_h:
            hrzn_mid = (hrzn_l + hrzn_h)//2

            if target == matrix[vert_h][hrzn_mid]:
                return True
            elif target > matrix[vert_h][hrzn_mid]:
                hrzn_l = hrzn_mid + 1
            else:  # target < matrix[vert_h][hrzn_mid]:
                hrzn_h = hrzn_mid - 1

        return False
