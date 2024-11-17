for master in Glyphs.font.masters:
    print(f"Unlocking guides for master: {master.name}")
    for guide in master.guides:
        if guide.locked:
            guide.locked = False  # Unlock the guide
            print(f"Guide at position {guide.position} unlocked")
