# Heap Data Structures Assignment

## Overview

This project implements and analyzes heap data structures, focusing on Heapsort and a Priority Queue using a binary heap. The goal is to understand their design, efficiency, and real-world applications, as well as compare Heapsort with other sorting algorithms such as Quicksort and Merge Sort.

## Features

* Heapsort implementation using a max heap
* Priority Queue with core operations: insert, extract_max, increase_key, decrease_key, and is_empty
* Comparison of sorting algorithms on random, sorted, and reverse-sorted data
* Performance analysis based on execution time

## Requirements

* Python 3.x

## How to Run

1. Download or clone the repository
2. Open the project folder in a terminal
3. Run the following commands:

   * python heapsort.py
   * python priority_queue.py

## Summary of Findings
Heapsort consistently performs at O(n log n) across all input types, making it reliable and predictable.
Quicksort is faster on average but performs poorly on sorted data if not optimized.
Merge Sort provides stable performance but requires additional memory. 
The Priority Queue efficiently handles task scheduling operations with O(log n) complexity, making it suitable for applications such as CPU scheduling and real-time systems.
