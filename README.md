
# Dynamic Programming Repository: Classic Problems Solved 🚀

Welcome to my dynamic programming repository where I explore and explain solutions to classic problems using both recursion and dynamic programming techniques. This repository serves as a practical reference for coding enthusiasts interested in understanding and applying dynamic programming strategies to solve problems efficiently.

## Table of Contents 📚
- [About the Repository](#about-the-repository)
- [Installation](#installation)
- [Problems Solved](#problems-solved)
  - [All Problems](#all-problems)
  - [Fibonacci Sequence](#fibonacci-sequence)
  - [Climbing Stairs](#climbing-stairs)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Acknowledgments](#acknowledgments)

## About the Repository

This repository includes Python scripts that solve 15 LeetCode problems with both recursion and dynamic programming (see [All Problems](#all-problems)). Two of them have detailed write-ups:
- Fibonacci Sequence (Leetcode 509)
   - [Recursion vs. Dynamic Programming: Fibonacci](https://medium.com/data-science/dynamic-programming-i-python-8b20387870f5)
- Climbing Stairs (Leetcode 70)
   - [Recursion vs. Dynamic Programming: Climbing Stairs](https://medium.com/geekculture/recursion-vs-dynamic-programming-climbing-stairs-48032b31db98)

Each solution is discussed with respect to both its recursive and dynamic programming implementations, including analysis of time and space complexities.

## Installation 💽

To clone and run these scripts locally, use the following commands:

```bash
git clone https://github.com/hzmsh/DynamicProgramming.git
cd DynamicProgramming
```

## Problems Solved

### All Problems
- Longest Palindromic Substring (Leetcode 5)
- Generate Parentheses (Leetcode 22)
- Jump Game II (Leetcode 45)
- Maximum Subarray (Leetcode 53)
- Climbing Stairs (Leetcode 70)
- Edit Distance (Leetcode 72)
- Decode Ways (Leetcode 91)
- Interleaving String (Leetcode 97)
- Pascal's Triangle (Leetcode 118)
- Pascal's Triangle II (Leetcode 119)
- Best Time to Buy and Sell Stock (Leetcode 121)
- Counting Bits (Leetcode 338)
- Is Subsequence (Leetcode 392)
- Fibonacci Number (Leetcode 509)
- Divisor Game (Leetcode 1025)

### Fibonacci Sequence 🧬

**Description**: The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1.

**Example Usage**:

```bash
python "0509_Fibonacci Number_DP.py"
```

**Detailed Analysis**: Includes performance comparison of recursive vs dynamic programming approaches with visual aids.

### Climbing Stairs 🧗‍♂️

**Description**: Determine the number of ways to climb `n` steps when you can climb either one or two steps at a time.

**Example Usage**:

```bash
python "0070_Climb Stairs_DP.py"
```

**Detailed Analysis**: Focuses on optimizing the recursive solution using dynamic programming techniques to reduce time complexity from exponential to polynomial.

## Usage 🚀

Each problem has a recursion version and a DP version (for example `0072_EditDistance_Recursion.py` and `0072_EditDistance_DP.py`). Most files are LeetCode-style `Solution` classes: paste one into LeetCode, or load it in Python and call it, for example `Solution().minDistance("horse", "ros")`.

The Fibonacci and Climbing Stairs files also set an input `n` at the top and store the result in `out`, so you can run them directly; the Fibonacci DP version prints the DP array as it fills it.

`0070_Climb Stairs_Time Complexity.py` times the recursive Climbing Stairs solution for larger `n` and plots the runtime (needs `matplotlib`).

## Contributing 🤝

Contributions to improve the existing solutions or add new problem solutions are welcome. Please fork the repository, make your changes, and submit a pull request.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact 📧

If you have any questions or suggestions, please contact me via [GitHub email](mailto:markusma@alumni.upenn.edu).

## Acknowledgments 🎉

Special thanks to:
- [Towards Data Science](https://towardsdatascience.com/) and [Geek Culture](https://medium.com/geekculture) for hosting the articles that inspired these solutions.
- Contributors and readers who provide valuable feedback and suggestions.
