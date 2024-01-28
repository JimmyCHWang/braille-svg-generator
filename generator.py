#!/usr/bin/env python3

# change width and height of svg if required
# it is recommended that the width, height, and diameters are even numbers
svg_width = 154
svg_height = 216
dot_diameter = 30

svg_head = f"""
<svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
"""

svg_tail = "</svg>"

svg_black_dot_template_str = '<circle cx="{}" cy="{}" r="{}" fill="black" />'
svg_white_dot_template_str = '<circle cx="{}" cy="{}" r="{}" stroke="black" fill="none" />'

from itertools import product

def generate_combination_lists():
    # Create a list of numbers from 1 to 6
    numbers = list(range(1, 7))
    
    # Generate all combinations of picking or not picking each number
    all_combinations = list(product([0, 1], repeat=len(numbers)))
    
    # Generate lists with only the picked numbers for each combination
    picked_lists = [
        [str(numbers[i]) for i, choice in enumerate(combination) if choice == 1] 
        for combination in all_combinations
    ]
    
    return picked_lists

# Generate all combinations that will draw a black dot
combination_lists = generate_combination_lists()

half_width = svg_width / 2
half_height = svg_height / 2
half_diameter = dot_diameter / 2

for combination in combination_lists:
    name = ''.join(combination)
    if len(name) == 0:
        name = '0'
    with open(f"svgs/dot-{name}.svg", "w") as f:
        f.write(svg_head)
        for dot_id in range(1, 7):
            dot_x = (half_width - dot_diameter) if dot_id <= 3 else (half_width + half_diameter)
            dot_y = (half_height - 1.5 * dot_diameter) if dot_id % 3 == 1 else (
                (half_height + 1.5 * dot_diameter) if dot_id % 3 == 0 else half_height
            )
            if str(dot_id) in combination:
                f.write(svg_black_dot_template_str.format(dot_x, dot_y, half_diameter))
            else:
                f.write(svg_white_dot_template_str.format(dot_x, dot_y, half_diameter))
        f.write(svg_tail)
        