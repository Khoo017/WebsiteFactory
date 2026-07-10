# GM650 — Bill of Materials, Cutting Plans & Hardware Schedule

All dimensions mm. Aluminium stock lengths assumed **6.0 m** (adjust nesting if supplier
stocks 6.5 m). Alloy 6061-T6 preferred; 6063-T6 acceptable for rails and sleeves.

## 1. Fabricated parts

| Part no. | Description | Material | Qty per SK | Qty per PK |
|---|---|---|---|---|
| GM-T01 | Welded trestle frame (DWG-02) | 50×50×3 SHS + 8 mm plate | 1 | 1 |
| GM-R01 | Rail segment, 1250 lg, ends drilled (DWG-03) | 50×50×3 SHS | – | 3 |
| GM-S01 | Splice sleeve, 300 lg, drilled (DWG-03) | 40×40×3 SHS | – | 3 |
| GM-B01 | Bracing strap, 2700 lg, ends drilled (DWG-06) | 40×3 flat bar | 2 | – |

Bracing Kit **BK** (1 per 4 panels in bundles ≥ 6): 2 × GM-B01 + 4 × M10 bolt sets.

### GM-T01 trestle — member cut list (one trestle)

| Mark | Member | Section | Length | Cut angles |
|---|---|---|---|---|
| T1 | Bottom chord | 50×50×3 SHS | 2430 | square both ends |
| T2 | Rafter | 50×50×3 SHS | 2550 | square (overhangs trimmed square) |
| T3 | Rear post | 50×50×3 SHS | 875 | top cut 10° |
| T4 | Front post | 50×50×3 SHS | 450 | top cut 10° |
| T5 | Mid strut | 50×50×3 SHS | 662 | top cut 10° |
| T6 | Baseplate ×2 | 150×150×8 plate | – | 2 × Ø14 holes @ 100 crs each |

Weld: 6 mm fillet all round, 5356 filler. Frame must be built in a jig — supply first
article for dimensional check (±3 mm on overall geometry, posts square to chord ±1°).
Approx. 11.6 kg/trestle. Est. 1.5–2 h welding each in a simple jig at volume.

## 2. Stock nesting plans (6.0 m bars)

**Trestles — per 2 trestles, 3 bars of 50×50×3 SHS:**

| Bar | Cuts | Used | Offcut |
|---|---|---|---|
| 1 | 2550 + 2430 + 875 | 5855 | 145 |
| 2 | 2550 + 2430 + 875 | 5855 | 145 |
| 3 | 662 + 662 + 450 + 450 | 2224 | **3776 → yields 3 × GM-R01 rail segments** |

Net result: **3 bars of 50×50×3 SHS ≈ 2 trestles + 3 rail segments** — one PK consumes
almost exactly 1.5 bars with near-zero waste.

**Sleeves:** 20 × GM-S01 per 6.0 m bar of 40×40×3 SHS.
**Straps:** 2 × GM-B01 per 6.0 m bar of 40×3 flat.
**Baseplates:** ≈128 pcs per 2400×1200×8 sheet (guillotine + drill, or waterjet if available).

### Total stock per bundle (incl. ~5 % waste)

| Bundle | 50×50×3 SHS 6 m bars | 40×40×3 SHS bars | 40×3 flat bars | 8 mm plate |
|---|---|---|---|---|
| 1 panel | 3 | 1 | 1 | 4 plates |
| 4 panels | 8 | 1 | 1 | 10 plates |
| 8 panels | 15 | 1 | 2 | 18 plates |
| 12 panels | 23 | 2 | 2 | 26 plates |

## 3. Fastener schedule (stainless A4/316)

| Item | Size | Per SK | Per PK | Use |
|---|---|---|---|---|
| Hex bolt + nyloc + 2 washers | M8 × 70 | – | 12 | Rail splices (4 per sleeve, through both walls) |
| Button-head bolt + serrated washer | M8 × 25 | 6 | 3 | Clamp to rivnut |
| Rivnut, large-flange | M8 | 6 | 3 | Clamp mounting in rail top face (site-set) |
| Hex bolt + nyloc + washers | M10 × 120 | 3 | 3 | Rail to rafter, vertical through-bolt (site-drilled Ø11) |
| Hex bolt + nyloc | M10 × 20 | 4 | – | Bracing straps (also 4 per BK) |
| J-bolt, hot-dip galv (or M12 A4 chemical stud) | M12 × 300 | 4 | 4 | Baseplate anchors, 2 per plate |
| EPDM isolation pad | 150×150×3 | 2 | 2 | Baseplate to concrete |
| Earth lug + 6 mm² Cu tail | M8 | 3 | – | Rail-line earthing |

## 4. Imported items (the only non-local parts)

| Item | Spec | Per SK | Per PK | Notes |
|---|---|---|---|---|
| End clamp | For 30 mm frame, anodised Al, with M8 slot | 6 | – | Buy the bolt-through type (not T-bolt); pair with M8×25 above |
| Mid clamp | For 30 mm frame, 21 mm gap, M8 slot | – | 3 | Same |
| M8 rivnuts + hand setter | A4 or large-flange Al body | (bulk) | (bulk) | One-time tool ≈ US$30 |

Standard commodity solar clamps — order in bulk (e.g. 500+ pcs) from any AU/NZ/CN solar
hardware supplier. Everything else on this page is stocked or fabricated in Suva
(aluminium SHS/flat/plate: the usual Suva metal and hardware merchants; stainless
fasteners: marine chandlers and fastener suppliers).

## 5. Consumables & site-supplied

- Concrete 20 MPa: 0.3 m³ per trestle (2 pads).
- 5356 MIG/TIG wire, cutting discs.
- Packaging: strap each kit to a timber skid; rails and straps bundled + taped ends.
