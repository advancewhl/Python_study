from deque import Deque


def pal_checker(a_str):
    char_deque = Deque()
    for ch in a_str:
        char_deque.add_rear(ch)

    while char_deque.size() > 1:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            return False

    return True


print(pal_checker("adda"))
