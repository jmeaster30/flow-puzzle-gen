# WFC 1

This is code was for me to understand the wave function collapse algorithm and start gauging the difficulty of generating these puzzles

In this I attempted to just use valid shapes that the puzzles allowed but it often led to grids that couldn't be completed.

Then I converted to allowing every possible flow connection which helped me catch a bunch of bugs and simplified the code a little bit.

Problems:

- Recursion depths hit often
- Occasionally sets some cells to not have possibilities even though it is obviously there should be some
- Does not generate a valid puzzle

I want to attempt to turn the recursive algorithm into an iterative one so we can avoid hitting the max recursion depth. I also believe the second issue is a bug so that will be fixed as well. I think that even though this doesn't generate a valid puzzle currently, we can generate a valid puzzle from this by removing all invalid connections and invalidating the neighbor cells.
