import random

# Generate random positions and sizes for hearts and flowers
elements = [
    {"type": "heart", "size": random.randint(50, 100), "top": random.randint(0, 400), "left": random.randint(0, 800)},
    {"type": "flower", "size": random.randint(50, 100), "top": random.randint(0, 400), "left": random.randint(0, 800)},
    {"type": "heart", "size": random.randint(50, 100), "top": random.randint(0, 400), "left": random.randint(0, 800)},
    {"type": "flower", "size": random.randint(50, 100), "top": random.randint(0, 400), "left": random.randint(0, 800)},
    {"type": "heart", "size": random.randint(50, 100), "top": random.randint(0, 400), "left": random.randint(0, 800)},
]

# Output the generated elements
for element in elements:
    print(f"{element['type']} with size {element['size']} at top {element['top']}px and left {element['left']}px")
