layer = Glyphs.font.selectedLayers[0]
modified = False
for path in layer.paths:
    for node in path.nodes:
        if node.type == 'curve':
            node.type = 'line'
            print(f"Handles were removed from the node at position ({node.x}, {node.y})")
            modified = True
if not modified:
    print("No handles found.")
