# Write your solution here
def create_tuple(x: int, y: int, z: int):
    nums = [x, y, z]

    nx = min(nums)
    ny = max(nums)
    nz = sum(nums)

    return (nx, ny, nz)


if __name__ == "__main__":
    print(create_tuple(5, 3, -1))