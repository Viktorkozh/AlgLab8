#!/usr/bin/env python3
# coding: utf-8 -*-

import random


def merge_sort(alist):
    if len(alist) > 1:
        mid = len(alist)//2  # Разделение пополам
        left_half = alist[:mid]
        right_half = alist[mid:]

        # Сортировка половин и подсчет инверсий
        left_half, left_inversions = merge_sort(left_half)
        right_half, right_inversions = merge_sort(right_half)
        total_inversions = left_inversions + right_inversions

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                alist[k] = left_half[i]
                i += 1
            else:
                alist[k] = right_half[j]
                j += 1
                total_inversions += len(left_half) - i
            k += 1

        while i < len(left_half):
            alist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            alist[k] = right_half[j]
            j += 1
            k += 1

        return alist, total_inversions
        
    return alist, 0  


def fill_list(numOfEl):
    a = [random.randint(0, 1000) for _ in range(numOfEl)]
    return a


if __name__ == "__main__":
    a = fill_list(100)
    print(a)
    a, cnt = merge_sort(a)
    print("Reps: ", cnt)
    print(a)