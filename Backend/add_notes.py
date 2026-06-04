import sqlite3

# Connect Database
conn = sqlite3.connect("dsa_tracker.db")
cursor = conn.cursor()

# Check database
cursor.execute("SELECT COUNT(*) FROM problems")
print("Problems:", cursor.fetchone()[0])

# Problem 1
note1 = """
Approach:
Use a HashMap to store previously visited elements and check if the complement exists.

Pseudo Code:

Create empty hashmap

For each number:
    complement = target - current

    If complement exists:
        return indices

    Store current element

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
HashMap enables constant-time lookup.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note1, 1)
)

# Problem 2
note2 = """
Approach:
Repeatedly divide the sorted array into two halves and search in the correct half.

Pseudo Code:

low = 0
high = n - 1

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        low = mid + 1

    else:
        high = mid - 1

Time Complexity:
O(log n)

Space Complexity:
O(1)

Key Learning:
Binary Search works only on sorted data.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note2, 2)
)

# Problem 3
note3 = """
Approach:
Use a stack to keep track of opening brackets.

Pseudo Code:

Create empty stack

For each character:

    If opening bracket:
        push into stack

    Else:

        If stack is empty:
            return False

        If top does not match:
            return False

        Pop stack

Return stack is empty

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Stack is useful for matching nested structures.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note3, 3)
)

# Problem 4
note4 = """
Approach:
Merge arrays from the end to avoid overwriting values.

Pseudo Code:

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:

    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1

    else:
        nums1[k] = nums2[j]
        j -= 1

    k -= 1

Copy remaining nums2 elements

Time Complexity:
O(m+n)

Space Complexity:
O(1)

Key Learning:
Backward traversal avoids extra space.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note4, 4)
)

# Problem 5
note5 = """
Approach:
Track minimum price seen so far and maximum profit.

Pseudo Code:

minPrice = infinity
maxProfit = 0

For each price:

    minPrice = min(minPrice, price)

    profit = price - minPrice

    maxProfit = max(maxProfit, profit)

Return maxProfit

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Maintain running minimum while traversing.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note5, 5)
)

# Problem 6
note6 = """
Approach:
Use Slow and Fast pointers.

Pseudo Code:

slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        return True

Return False

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Floyd Cycle Detection is efficient for cycle finding.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note6, 6)
)
# Problem 7
note7 = """
Approach:
Sort array and use two pointers.

Pseudo Code:

Sort array

For each i:

    left = i + 1
    right = n - 1

    while left < right:

        sum = nums[i] + nums[left] + nums[right]

        if sum == 0:
            store triplet

        elif sum < 0:
            left += 1

        else:
            right -= 1

Time Complexity:
O(n²)

Space Complexity:
O(1)

Key Learning:
Sorting helps eliminate duplicate triplets.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note7, 7)
)

# Problem 8
note8 = """
Approach:
Group words using sorted string as key.

Pseudo Code:

Create hashmap

For each word:

    key = sorted(word)

    hashmap[key].append(word)

Return hashmap values

Time Complexity:
O(n*k log k)

Space Complexity:
O(n)

Key Learning:
Anagrams share the same sorted form.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note8, 8)
)

# Problem 9
note9 = """
Approach:
Use Sliding Window.

Pseudo Code:

Create set

left = 0

For right in range(n):

    while character exists:

        remove left character
        left += 1

    add current character

    update answer

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
Sliding Window avoids rechecking characters.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note9, 9)
)

# Problem 10
note10 = """
Approach:
Use two pointers from both ends.

Pseudo Code:

left = 0
right = n - 1

while left < right:

    area = min(height[left], height[right])
           * (right-left)

    update answer

    move smaller height pointer

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Move only the smaller wall.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note10, 10)
)

# Problem 11
note11 = """
Approach:
Use DFS to visit connected land cells.

Pseudo Code:

For each cell:

    if land:

        DFS(row,col)

        islands += 1

DFS:

    mark visited

    visit 4 directions

Time Complexity:
O(m*n)

Space Complexity:
O(m*n)

Key Learning:
Connected components form islands.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note11, 11)
)

# Problem 12
note12 = """
Approach:
Sort intervals and merge overlaps.

Pseudo Code:

Sort intervals

For each interval:

    if overlap:

        merge intervals

    else:

        add new interval

Time Complexity:
O(n log n)

Space Complexity:
O(n)

Key Learning:
Sorting simplifies overlap detection.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note12, 12)
)
# Problem 13
note13 = """
Approach:
Use Backtracking.

Pseudo Code:

Place queen row by row

If safe:

    place queen

    recurse next row

    remove queen

If row == n:

    store solution

Time Complexity:
O(N!)

Space Complexity:
O(N)

Key Learning:
Backtracking explores all valid configurations.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note13, 13)
)

# Problem 14
note14 = """
Approach:
Use BFS to find shortest transformation.

Pseudo Code:

Add beginWord to queue

while queue not empty:

    pop word

    generate neighbors

    if endWord found:
        return level

    push valid neighbors

Time Complexity:
O(N * M²)

Space Complexity:
O(N)

Key Learning:
BFS guarantees shortest path.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note14, 14)
)

# Problem 15
note15 = """
Approach:
Use Backtracking.

Pseudo Code:

Find empty cell

Try digits 1-9

If valid:

    place digit

    recurse

    remove digit

If board complete:

    return solution

Time Complexity:
O(9^(n²))

Space Complexity:
O(n²)

Key Learning:
Backtracking tries all valid possibilities.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note15, 15)
)

# Problem 16
note16 = """
Approach:
Use Dynamic Programming.

Pseudo Code:

dp[i][j]

If characters match:

    move diagonally

Handle '*' cases separately

Return dp[m][n]

Time Complexity:
O(m*n)

Space Complexity:
O(m*n)

Key Learning:
DP avoids repeated computations.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note16, 16)
)

# Problem 17
note17 = """
Approach:
Use DFS with recursion stack.

Pseudo Code:

For each node:

    DFS(node)

DFS:

    mark visited

    mark recursion stack

    visit neighbors

    if neighbor in recursion stack:
        cycle found

Time Complexity:
O(V+E)

Space Complexity:
O(V)

Key Learning:
Recursion stack helps detect back edges.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note17, 17)
)

# Problem 18
note18 = """
Approach:
Use Dijkstra's Algorithm.

Pseudo Code:

Initialize distances

Push source into priority queue

while queue not empty:

    pop minimum distance node

    relax neighbors

Return shortest distances

Time Complexity:
O((V+E) log V)

Space Complexity:
O(V)

Key Learning:
Greedy selection gives shortest path.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note18, 18)
)
# Problem 19
note19 = """
Approach:
Use Binary Search on answer space.

Pseudo Code:

low = 1
high = max(piles)

while low <= high:

    mid = (low + high) // 2

    calculate hours needed

    if hours <= h:
        answer = mid
        high = mid - 1

    else:
        low = mid + 1

Time Complexity:
O(n log m)

Space Complexity:
O(1)

Key Learning:
Binary Search can be applied on answers.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note19, 19)
)

# Problem 20
note20 = """
Approach:
Use Binary Search on maximum pages.

Pseudo Code:

low = max(books)
high = sum(books)

while low <= high:

    mid = (low + high) // 2

    if allocation possible:

        answer = mid
        high = mid - 1

    else:

        low = mid + 1

Time Complexity:
O(n log(sum))

Space Complexity:
O(1)

Key Learning:
Minimize maximum value using Binary Search.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note20, 20)
)

# Problem 21
note21 = """
Approach:
Use Kadane's Algorithm.

Pseudo Code:

currentSum = 0
maxSum = -infinity

for number:

    currentSum += number

    maxSum = max(maxSum,currentSum)

    if currentSum < 0:
        currentSum = 0

Return maxSum

Time Complexity:
O(n)

Space Complexity:
O(1)

Key Learning:
Negative prefixes should be discarded.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note21, 21)
)

# Problem 22
note22 = """
Approach:
Use HashMap for complement lookup.

Pseudo Code:

Create hashmap

For each price:

    complement = money - price

    if complement exists:
        return indices

    store current price

Time Complexity:
O(n)

Space Complexity:
O(n)

Key Learning:
HashMap reduces lookup time.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note22, 22)
)

# Problem 23
note23 = """
Approach:
Generate primes using Sieve.

Pseudo Code:

Create sieve array

Mark all numbers prime

For i from 2 to sqrt(n):

    if prime:

        mark multiples

Output primes

Time Complexity:
O(n log log n)

Space Complexity:
O(n)

Key Learning:
Sieve efficiently generates primes.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note23, 23)
)

# Problem 24
note24 = """
Approach:
Sort array using reversal operations.

Pseudo Code:

For each position:

    find correct element

    reverse segment

Repeat until sorted

Time Complexity:
O(n²)

Space Complexity:
O(1)

Key Learning:
Reversal can simulate sorting operations.
"""

cursor.execute(
    "UPDATE problems SET notes=? WHERE id=?",
    (note24, 24)
)
# Save Changes
conn.commit()

# Close Database
conn.close()

print("Notes Added Successfully")