# OPTICA Normal Typeface Scripts Repository

This repository contains a collection of Python scripts designed to assist in the production of the OPTICA Normal typeface. The scripts streamline common tasks in the font design process, focusing on alignment, guide manipulation, and glyph optimization.

---

## About OPTICA Normal

**OPTICA Normal** is a typeface built using orthogonal lines arranged in a fixed order. This unique optic game creates a pattern-like texture that reveals readable text upon closer inspection. The typeface is ideal for large sizes, where its intricate details can shine. OPTICA Normal is inspired by the optical art of Colombian artist Omar Rayo, serving as a tribute to his geometric and visual experimentation.

Visit the official [OPTICA typeface](https://bluetypo.com/site/en/2017/04/23/optica-normal/) for more information.

---

## Repository Structure

```
.
├── README.md        # Repository documentation
├── screenshots/     # Visual examples of the scripts in action
├── scripts/         # Python scripts for Glyphs app
└── LICENSE          # License file
```

---

## Python Scripts

### 1. **Remove Curve Handles**
- **Filename:** `remove_curve_handles.py`
- **Description:** Eliminates all curve handles from the glyphs, ensuring that only straight orthogonal lines remain. Maintains the typographic consistency of OPTICA Normal by removing unwanted bezier curve adjustments.

### 2. **Identify Global Guides**
- **Filename:** `identify_global_guides.py`
- **Description:** Scans the font project to locate all global guides in the file, making them easier to work with. Helps streamline alignment processes by identifying key reference points across glyphs.

### 3. **Align Extreme Nodes**
- **Filename:** `align_extreme_nodes.py`
- **Description:** Automatically aligns extreme nodes to preserve the optical rhythm and geometric accuracy of the glyphs. Ensures precision and consistency in OPTICA's orthogonal structure.

### 4. **Unlock Global Guides**
- **Filename:** `unlock_global_guides.py`
- **Description:** Unlocks all global guides, allowing full manipulation and repositioning as needed. Facilitates modifications during the design process.

### 5. **Lock Global Guides**
- **Filename:** `lock_global_guides.py`
- **Description:** Locks all global guides to prevent accidental changes during production. Ensures guide stability during final adjustments.

### 6. **Reverse Glyph Strokes**
- **Filename:** `reverse_glyph_strokes.py`
- **Description:** Inverts the direction of strokes for all glyphs in the font. Useful for troubleshooting direction-related issues or creating stylistic effects.

---

## Screenshots

The `screenshots` folder contains examples showcasing the scripts in action, including before-and-after comparisons of glyph manipulations.

**Example:**
1. **Before align extreme nodes**  
   ![Before Screenshot](screenshots/before_align_extreme_nodes.png)

2. **After align extreme nodes**  
   ![After Screenshot](screenshots/after_align_extreme_nodes.png)

---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the scripts as per the license terms.

---

## Contribution

Contributions are welcome! If you have improvements, new ideas, or encounter issues, feel free to open a pull request or issue.

## 📚 How to Cite

If you use this code or its results, please cite:

**APA 7**

Guerrero-Salinas, M. (2025). *OPTICA Normal Typeface Scripts Repository* (v1.0.0) [Software]. GitHub. https://github.com/mguerrerouaslp/OPTICA-Normal-Typeface-Scripts-Repository. https://doi.org/10.5281/zenodo.16324052

---

**BibTeX**
```bibtex
@software{guerrero-salinas_2025_optica_normal,
  author    = {Guerrero-Salinas, Manuel},
  title     = {OPTICA Normal Typeface Scripts Repository},
  year      = {2025},
  version   = {1.0.0},
  url       = {https://github.com/mguerrerouaslp/OPTICA-Normal-Typeface-Scripts-Repository},
  doi       = {10.5281/zenodo.16324052},
  publisher = {GitHub},
  note      = {Software}
}


