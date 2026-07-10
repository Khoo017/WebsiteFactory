# GM650 — Design Basis

## 1. Module data (from JA Solar datasheet, ver. Aus-EN-20241220A)

| Parameter | Value |
|---|---|
| Model | JAM72S42-LR n-type monofacial, 625–650 W |
| Dimensions | 2465 × 1134 × 30 mm |
| Weight | 29.6 kg |
| Frame | 30 mm anodised aluminium, drain + grounding holes (Ø4.2) |
| Max static load (front / rear) | **3600 Pa / 1600 Pa** (design values, ×1.5 test factor) |
| Mounting | Clamped on long edges within manufacturer's approved clamp zones |

## 2. Wind loading

- Basis: AS/NZS 1170.2:2021, cyclonic region (Fiji is TC-prone; TC Winston 2016
  produced ~285 km/h gusts).
- **Ultimate design gust: V = 70 m/s (252 km/h)**, 3-second gust at panel height.
- Dynamic pressure: q = 0.6 × V² = **2.94 kPa**.
- Structure treated as a free-standing monoslope canopy at 10°:
  - Global net pressure coefficient C_pn ≈ ±1.2 → **design net pressure ±3.5 kPa**
  - Local (row-end / edge zones) C_pn ≈ ±1.8 → **±5.3 kPa** for clamp and end-fixing checks
- Per panel (2.80 m²): ±9.8 kN. Per interior trestle (tributary 1.155 × 2.465 m): **≈10 kN
  ultimate up or down**; ≈5 kN per footing.
- Along-row drag: ≈1.7 kN per trestle — resisted by crossed-strap bracing bays.

The 10° tilt is deliberate: at Fiji's latitude (~18°S) it gives up under ~2 % of annual
yield versus latitude tilt, keeps enough slope for rain self-cleaning, and roughly halves
cyclonic wind load compared with a 20–25° frame.

## 3. Members and materials

| Member | Section | Alloy | Governing check (ULS) | Result |
|---|---|---|---|---|
| Rail (3 lines) | 50×50×3 SHS | 6061-T6 (6063-T6 acceptable) | Continuous span 1155 mm, w ≈ 2.2 kN/m → M ≈ 0.3 kNm | σ ≈ 35 MPa ≪ 0.9·f_y ✔ |
| Trestle rafter | 50×50×3 SHS | 6061-T6 | Rail point loads, mid-strut halves span → M ≈ 1.0 kNm | σ ≈ 120 MPa < 216 MPa ✔ |
| Trestle posts/chord/strut | 50×50×3 SHS | 6061-T6 | Axial + portal action | ✔ ample |
| Splice sleeve | 40×40×3 SHS × 300 | 6061-T6 | Splice at worst location M ≈ 0.37 kNm | σ ≈ 85 MPa ✔ |
| Baseplate | 150×150×8 plate | 5083 / 6061 | 2× M12 anchors @ 100 crs, 2.5 kN/bolt uplift | ✔ |
| Bracing strap | 40×3 flat bar | 6061/5052 | 1.7 kN axial tension | ✔ |

Welds: 6 mm fillet all round at all trestle joints, 5356 filler, by a welder experienced
in structural aluminium (Suva boat/joinery shops routinely do this). Note: welding locally
anneals 6061-T6 (HAZ strength ≈ 0.5 f_y); member utilisations above already leave margin,
and welded joints are at member ends where moments are low.

## 4. Foundations

- Cast-in-place concrete pads **500 × 500 × 600 deep**, top 150 mm above grade,
  2 per trestle at 2430 mm centres.
- Each resists ≈5 kN ultimate uplift via self-weight (≈3.6 kN) + soil overburden/shear.
  **Verify against actual site soil**; in soft or waterlogged ground enlarge to
  600 × 600 × 700.
- Anchors: 2 × M12 hot-dip-galvanised J-bolts cast in per baseplate (or M12 A4 chemical
  studs into cured pads). Concrete: 20 MPa minimum, locally batched is fine.

## 5. Module limit — important commercial note

At the full 70 m/s design event, local panel suction can reach ~5.3 kPa, which **exceeds
the module's rear-side rating (1600 Pa design / 2400 Pa test)** — as it does for
essentially every framed module on the market. The structure is designed to survive
Winston-class wind; the *panels* are the sacrificial element above roughly 45–50 m/s.
Mitigations built into this design: minimum tilt, low profile, 3 rails / 6 clamps per
panel (higher rating per JA's installation manual than 4-clamp mounting), and short spans.
Tell customers plainly: structure is cyclone-rated, panels are insured items. Do not
advertise the panels themselves as cyclone-proof.

## 6. Corrosion (coastal Fiji)

- All aluminium mill finish; no coating required structurally.
- All bolts, nuts, washers, rivnuts: **stainless A4/316** (A2/304 acceptable inland).
- Isolate stainless↔aluminium contact with washers as supplied; isolate baseplate from
  concrete with 3 mm EPDM pad or bituminous paint.
- Earthing per AS/NZS 5033: serrated stainless washers under clamp bolts to pierce
  anodising, 6 mm² Cu row bond, M8 earth lug per rail line.

## 7. Standards referenced

AS/NZS 1170.0/.1/.2 (actions, wind), AS/NZS 1664.1 (aluminium structures),
AS/NZS 5033 (PV installation), Fiji National Building Code.

## 8. Disclaimer

This is a preliminary design prepared for quoting, prototyping and fabricator discussion.
Loads and member sizes are indicative, based on stated assumptions and generic site
conditions. **Before commercial sale or installation, have the design reviewed and
certified by a structural engineer registered in Fiji**, including site-specific wind,
soil and foundation verification. Follow the JA Solar installation manual for approved
clamp zones and torque values; deviations void the module warranty.
