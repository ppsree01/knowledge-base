# Stage 2: Search & Ranking

- Add a search method to your class:
```
find_by_prefix_and_suffix(self, prefix: str, suffix: str) -> list[str]
```
- Finds all files whose name starts with prefix and ends with suffix.
- Note: prefix and suffix are allowed to overlap (e.g., file "aba" matches prefix="ab" and suffix="ba"—standard str.startswith() and str.endswith() behavior).
- Sorting rules: Return a list of formatted strings f"{name}({size})" sorted by:
    - size in descending order (largest files first).
    - name in lexicographical (ASCII) ascending order to break ties.
- If no files match, return an empty list [].