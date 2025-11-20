def move_tower(height, from_pole, to_pole, with_pole):
    if height < 1:
        return
    move_tower(height - 1, from_pole, with_pole, to_pole)
    move_disk(from_pole, to_pole)
    move_tower(height - 1, with_pole, to_pole, from_pole)


def move_disk(from_pole, to_pole):
    print(f"moving disk from {from_pole} to {to_pole}")
