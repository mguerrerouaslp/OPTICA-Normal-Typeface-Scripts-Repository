horizontal_guides = []
vertical_guides = []

for master in Glyphs.font.masters:
    for guide in master.guides:
        if guide.angle == 0:
            horizontal_guides.append(guide)
        elif guide.angle == 90:
            vertical_guides.append(guide)

if not horizontal_guides or not vertical_guides:
    print("No global horizontal or vertical guides found in the font.")
else:
    threshold = 2
    for glyph in Glyphs.font.glyphs:
        print(f"Processing glyph: {glyph.name}")
        for layer in glyph.layers:
            for path in layer.paths:
                for node in path.nodes:
                    if node.type != 'curve':
                        is_at_left = abs(node.x - layer.bounds.origin.x) < threshold
                        is_at_right = abs(node.x - (layer.bounds.origin.x + layer.bounds.size.width)) < threshold
                        is_at_top = abs(node.y - layer.bounds.origin.y) < threshold
                        is_at_bottom = abs(node.y - (layer.bounds.origin.y + layer.bounds.size.height)) < threshold

                        if is_at_left or is_at_right or is_at_top or is_at_bottom:
                            closest_horizontal_guide = min(horizontal_guides, key=lambda g: abs(g.position.y - node.y))
                            closest_vertical_guide = min(vertical_guides, key=lambda g: abs(g.position.x - node.x))
                            original_x, original_y = node.x, node.y
                            node.x = closest_vertical_guide.position.x
                            node.y = closest_horizontal_guide.position.y

                            if node.x != original_x or node.y != original_y:
                                if node.x != original_x and node.y != original_y:
                                    print(f"{glyph.name} - Node modified in both coordinates: x: {original_x} -> {node.x}, y: {original_y} -> {node.y}")
                                elif node.x != original_x:
                                    print(f"{glyph.name} - Node modified in x: {original_x} -> {node.x}")
                                elif node.y != original_y:
                                    print(f"{glyph.name} - Node modified in y: {original_y} -> {node.y}")
