main
│
├──> snailfish_add(left, right)
│     │
│     └──> reduce([left, right])
│            │
│            ├── loop:
│            │
│            ├──> explode(number, depth=0)
│            │     │
│            │     ├── recursively tries left branch:
│            │     │     └── explode(left, depth+1)
│            │     │           ├── if explosion happens on the left:
│            │     │           │    └── add_leftmost(right, rcarry)
│            │     │           └── returns (new_left, lcarry, None)
│            │     │
│            │     ├── if no explosion on left, tries right branch:
│            │     │     └── explode(right, depth+1)
│            │     │           ├── if explosion happens on the right:
│            │     │           │    └── add_rightmost(left, lcarry)
│            │     │           └── returns (new_right, None, rcarry)
│            │     │
│            │     └── returns (number, None, None) if nothing exploded
│            │
│            └──> split(number)
│                  │
│                  ├── tries splitting left side first
│                  └── if not needed, tries right side
│
└──> magnitude(total)
      └── recursively computes:
           3 * magnitude(left) + 2 * magnitude(right)