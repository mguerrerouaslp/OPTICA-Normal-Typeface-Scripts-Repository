current_master_id = Glyphs.font.selectedFontMaster.id
for glyph in Glyphs.font.glyphs:
    print(f"Processing glyph: {glyph.name}")
    layer = glyph.layers[current_master_id]
    for path in layer.paths:
        path.reverse()
    bounds = layer.bounds
    rect = GSPath()

    rect.nodes.append(GSNode((bounds.origin.x, bounds.origin.y), type=LINE))  # Bottom-left node
    rect.nodes.append(GSNode((bounds.origin.x + bounds.size.width, bounds.origin.y), type=LINE))  # Bottom-right node
    rect.nodes.append(GSNode((bounds.origin.x + bounds.size.width, bounds.origin.y + bounds.size.height), type=LINE))  # Top-right node
    rect.nodes.append(GSNode((bounds.origin.x, bounds.origin.y + bounds.size.height), type=LINE))  # Top-left node
    rect.closed = True

    layer.paths.append(rect)
    layer.removeOverlap()
    print(f"Glyph '{glyph.name}' processed with background as a figure on the current master's layer.")
print("Reversal completed for all glyphs on the current master's layer.")
