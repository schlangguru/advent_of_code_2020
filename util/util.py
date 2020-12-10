from typing import List

def sliding_window(list: List[any], window_size = 2, skip_tail = False):
    """
    Generator for a sliding window of the given list.
    If skip_tail == True and the last window would be smaller than window_size this window is sipped.
    If skip_tail == False (default) the last window could be smaller than window_size.
    """
    start = 0
    while start < len(list):
        end = start + window_size
        if end > len(list):
            if  skip_tail:
                break
            else:
                end = len(list)
        yield list[start:end]
        start += 1