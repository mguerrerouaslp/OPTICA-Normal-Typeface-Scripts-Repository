for master in Glyphs.font.masters:
    print(f"global guides {master.name}:")
        for guide in master.guides:
        print(f"  - position: {guide.position}, angle: {guide.angle}")
