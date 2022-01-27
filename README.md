# The Complete Data Structures and Algorithms Course in Python [(link)](https://www.udemy.com/course/data-structures-and-algorithms-bootcamp-in-python/)

## Contents
<!-- MarkdownTOC -->

- [Section 1: Introduction](#section-1-introduction)
    + [Types of Data Structures](#types-of-data-structures)
    + [Types of Algorithms](#types-of-algorithms)
- [Sections 2-4: Recursion](#sections-2-4-recursion)
- [Section 5-6: Big O Notation](#section-5-6-big-o-notation)
    + [Time Complexity](#time-complexity)
    + [Space Complexity](#space-complexity)
    + [Drop Constants and Non-Dominant Terms](#drop-constants-and-non-dominant-terms)
        * [Example](#example)
        * [Recursive Examples](#recursive-examples)
- [Section 7: Arrays](#section-7-arrays)
    + [What is an array?](#what-is-an-array)
    + [Types of Arrays](#types-of-arrays)
    + [Arrays in Memory](#arrays-in-memory)
    + [Array Operations](#array-operations)
    + [When to Use/Avoid](#when-to-useavoid)
- [Section 8: Python Lists](#section-8-python-lists)
    + [Lists versus Arrays](#lists-versus-arrays)
    + [Operations](#operations)
- [Section 12: Dictionaries](#section-12-dictionaries)
    + [Operations](#operations-1)

<!-- /MarkdownTOC -->
<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Section 1: Introduction
- Data structures are just ways of organizing data to make access to that data easier/faster/more efficient.
- An algorithm is just a set of steps for accomplishing some task. Examples:
    + Compression algorithms for audio and video data: AAC, MP3, JPEG, H.265 (all stuff you've heard of before).
    + Graph algorithms for stuff like Google Maps
- Companies only tend to focus on DSA during interviews because it's the best way they know of to evaluate candidate's problem solving skills and software engineering fundamentals in a limited time.

### Types of Data Structures
- Primitive: Pre-defined in programming language (integer, float, character, string, boolean)
- Non-primitive: User-defined, combine two or more primitives
    + Linear: Data items arranged in memory in a linear, sequential manner
        * Static: Associated memory locations fixed at compile time (array, etc.)
        * Dynamic: Associated memory locations change (linked list, static, queue, etc.)
    + Non-linear: Data item connected to other items, non-sequential in memory (tree, graph, etc.)

### Types of Algorithms
- Simple recursive algorithms
    + Calls itself
- Divide and conquer algorithms
    + Divide problem into smaller subproblems of the same type, solve subproblems recursively
    + Combine solutions to subproblems into solution to original problem
    + Examples: Quick sort and merge sort
- Dynamic programming algorithms
    + Worked based on memoization (remember past results and use them to find new results)
    + Generally used for optimization problems
- Greedy algorithms
    + Works in phases, at each phase we do the best we can without considering future consequences
    + Hope that choosing local optimum solution at each step, we will end up at global optimum solution
    + Also used for optimization problems
- Brute force algorithms
    + Simply try all possibilities until satisfactory solution is found
- Randomized algorithms
    + Use random number at least once during computation to make a decision
    + Examples: Quick sort algorithm

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Sections 2-4: Recursion
- A way of solving a problem by having a function call itself. Properties:
    + Performing the same operation multiple times with different inputs
    + In every step we try smaller inputs to make the problem smaller
    + Base condition needed to stop recursion, otherwise infinite loop occurs
- System uses LIFO stack memory to remember/manage calls to recursive functions
- All recursive algorithms can be implemented
- Recursive algorithms can be very inefficient in memory space
- Recursion versus iteration:

|                  | Recursion | Iteration | Notes                                                                         |
|:-----------------|:----------|:----------|:------------------------------------------------------------------------------|
| Space efficient? | No        | Yes       | Iteration doesn't require stack memory                                        |
| Time efficient?  | No        | Yes       | Recursion incurs time overhead for push/pop operations on stack memory        |
| Easy to code?    | Yes       | No        | Recursion easier when we know problem can be divided into smaller subproblems |

- When to use recursion:
    + When problem can be broken into similar subproblems
    + When we are fine with extra time and space overhead
    + Need quick working solution more than efficient solution (recursion can be slow)
    + Relatively small inputs
    + Traversing pre-ordered trees
    + When using memoization to reduce time complexity
- When to avoid recursion:
    + Memory-constrained environments (mobile devices)
    + Time-critical applications (airbag deployment system)
    + Large inputs

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Section 5-6: Big O Notation
- Big O: Complexity ≤ worst case
- Big Ω: Complexity ≥ best case
- Big Θ: Worst case < complexity < best case
- O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)

### Time Complexity
- How long algorithm takes to run
```python
array = [1, 2, 3, 4, 5]

# O(1): Constant time complexity
element = array[n] # Direct lookup

# O(n): Linear time complexity
for element in array:
    print(element) # Visiting every element in array once

# O(log n): Logarithmic time complexity
for i in range(0, len(array), 3):
    print(array[i]) # Only visiting some of the elements
# Binary search of sorted array is another example of logarithmic complexity

# O(n^2): Quadratic time complexity
for x in array:
    for y in array:
        print(x, y) # Visiting each element in array for each element in array

# O(2^n): Exponential time complexity
def fibonacci(n):
    assert n >= 0 and isinstance(n, int), 'n must be a non-negative integer!'
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) # Two recursive calls per call
```

### Space Complexity
- How much memory is needed to run algorithm
    + Array of size n ⇒ O(n)
    + Array of size n\*n ⇒ O(n^2)

```python
# O(n) space complexity
def sum(n):
    if n <= 0:
        return 0
    else:
        return n + sum(n - 1)

# O(1) space complexity
def pair_sum_sequence(n):
    sum = 0
    for i in range(0, n + 1):
        sum = sum + pair_sum(i, i + 1)
    return sum

def pair_sum(a, b):
    return a + b
```

### Drop Constants and Non-Dominant Terms
- As n → ∞, constants/non-dominant terms don't really matter
- O(2n)        → O(n)
- O(n^2 + n)   → O(n^2)
- O(n + log n) → O(n)
- O(2\*2^n + 1000n^100) → O(2^n)

#### Example
```python
def findBiggestNumber(sampleArray):
    biggestNumber = sampleArray[0] # O(1)
    for index in range(1,len(sampleArray)): # O(n)
        if sampleArray[index] > biggestNumber: # O(1)
            biggestNumber = sampleArray[index] # O(1)
    print(biggestNumber) # O(1)

# O(1) + O(n) + O(1) + O(1) + O(1) ⇒ O(n)

```

#### Recursive Examples
```python
def findMaxNumRec(sampleArray, n): # M(n)
    if n == 1: # O(1)
       return sampleArray[0] # O(1)
    return max(sampleArray[n-1],findMaxNumRec(sampleArray,n-1)) # M(n - 1)

# M(n) = O(1) + M(n - 1)
# M(1) = O(1)
# M(n - 1) = O(1) + M((n - 1) - 1)
# M(n - 2) = O(1) + M((n - 2) - 1)

# M(n) = 1 + 1 + M((n - 1) - 1)
# = 2 + M(n - 2)
# = 2 + 1 + M((n - 2) - 1)
# = 3 + M(n - 3)
# ...
# = a + M(n - a), substitute a = n - 1
# = n - 1 + M(n - n - 1)
# = n - 1 + 1
# = n
```

```python
def f(n):
    if n <= 1:
        return 1
    return f(n-1) + f(n-1)

# O(2^n) = O(branches^depth)
```

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Section 7: Arrays
### What is an array?
- Stores data of the same type (traditionally)
- Elements located contiguously in memory (makes access efficient)
- Each element has unique index or key
- Size is predefined and cannot be modified

### Types of Arrays
- One-dimensional or multi-dimensional
- Think of 3D array as 2D array with a depth dimension as well
    + (First index is depth)

### Arrays in Memory
- Elements located sequentially in memory
- 2D and 3D arrays stored in memory as 1D array

### Array Operations
- Python uses list instead of traditional arrays
- But does have traditional arrays ([docs](https://docs.python.org/3/library/array.html))
    ```python
    from array import *
    my_array = array(typecode, [initializers]) #
    ```
- 1D array operations
    | Operation          |          Time Complexity           | Space Complexity |
    |:-------------------|:----------------------------------:|:----------------:|
    | Creation           |                O(1)                |       O(n)       |
    | Insertion          | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |
    | Accessing          |                O(1)                |       O(1)       |
    | Traversal          |                O(n)                |       O(1)       |
    | Searching (linear) |                O(n)                |       O(1)       |
    | Deletion           | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |

- 2D array operations
    | Operation            |           Time Complexity           | Space Complexity |
    |:---------------------|:-----------------------------------:|:----------------:|
    | Creation             |                O(1)                 |      O(mn)       |
    | Insertion of col/row | O(1) (end)<br>O(mn) (anywhere else) |       O(1)       |
    | Accessing            |                O(1)                 |       O(1)       |
    | Traversal            |                O(mn)                |       O(1)       |
    | Searching (linear)   |                O(mn)                |       O(1)       |
    | Deletion             | O(1) (end)<br>O(mn) (anywhere else) |       O(1)       |

### When to Use/Avoid
- When to use
    + To store multiple variables of same data type
    + When can leverage direct random access to elements
- When to avoid
    + When want to store multiple variables of different data types
    + Reserves specific amount of memory to store content
    + When array size could grow uncontrolably and thrash memory

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Section 8: Python Lists
- List: Data structure that holds an ordered collection of items
- Can contain items of different types

### Lists versus Arrays
- Both mutable.
- Both can be indexed and iterated.
- Both can be sliced.
- Arrays optimized for arithmetic operations.
- Lists can contain elements of different data types.

### Operations
| Operation          |          Time Complexity           | Space Complexity |
|:-------------------|:----------------------------------:|:----------------:|
| Creation           |                O(1)                |       O(n)       |
| Insertion          | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |
| Accessing          |                O(1)                |       O(1)       |
| Traversal          |                O(n)                |       O(1)       |
| Searching (linear) |                O(n)                |       O(1)       |
| Deletion           | O(1) (end)<br>O(n) (anywhere else) |       O(1)       |

(Same as 1D arrays)

<!-- ───────────────────────────────────────────────────────────────────────────── -->

## Section 12: Dictionaries
- Collection which is unordered (sort of), mutable, and indexed.
- Also known as associative array.
- If element added to dictionary causes a collision, it's added to the associated index as a linked list.
- Dictionary versus List
    | Dictionary                          |                 List                 |
    |:------------------------------------|:------------------------------------:|
    | Unordered                           |               Ordered                |
    | Access via keys                     |           Access via index           |
    | Collection of key-value pairs       |        Collection of elements        |
    | Preferred when you have unique keys | Preferred when you have ordered data |
    | No duplicate elements               |      Allows duplicate elements       |

### Operations
| Operation          |     Time Complexity      | Space Complexity |
|:-------------------|:------------------------:|:----------------:|
| Creation           |        O(len(d))         |       O(n)       |
| Insertion          | O(1)<br>O(n) (amortized) |       O(1)       |
| Accessing          |           O(1)           |       O(1)       |
| Traversal          |           O(n)           |       O(1)       |
| Searching (linear) |           O(n)           |       O(1)       |
| Deletion           |           O(1)           |       O(1)       |
