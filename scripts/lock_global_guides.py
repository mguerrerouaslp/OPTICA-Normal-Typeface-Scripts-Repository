for master in Glyphs.font.masters:
    print(f"Locking guides for master: {master.name}")
    for guide in master.guides:
        guide.locked = True
        print(f"Guide at position {guide.position} locked")
