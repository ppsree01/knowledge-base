# Stage 1: Basic File Operations
Implement three methods:

## Add File:
```
add_file(self, name: str, size: int) -> bool
```
- Adds a new file with name and size (in bytes, positive integer) to storage.
- If a file with name already exists, do not overwrite it; return False.
- Otherwise, store the file and return True.

## Copy File:
```
copy_file(self, name_from: str, name_to: str) -> bool
```
- Copies the file at name_from to name_to.
- If name_from does not exist, or if name_to already exists, return False.
- Otherwise, create an independent copy at name_to with the same size and return True.

## Get File Size:
```
get_file_size(self, name: str) -> int | None
```
- Returns the size of the file name if it exists, or None if it does not exist.

