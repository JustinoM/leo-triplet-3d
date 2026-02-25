# Leo Triplet 3D Visualization

An interactive 3D visualization of the **Leo Triplet** (M65, M66, NGC 3628), 
a famous group of interacting galaxies approximately 35 million light-years away.

## 🌌 Features

- **Astronomically-accurate positions** based on RA/Dec and redshift data from the NASA/IPAC Extragalactic Database (NED)
- **Tidal tail of NGC 3628** correctly oriented to match NOIRLab imagery (extends east/north)
- **Earth perspective** with viewer located at -Z looking toward the triplet
- **Interactive zoom** using mouse wheel
- **Rotatable 3D view** to explore spatial relationships
- **Distance annotations** showing separations between galaxies
- **Constant-size Earth marker** for scale reference

## 📊 Data Sources

| Galaxy | RA (J2000) | Dec (J2000) | Redshift | Distance |
|--------|------------|-------------|----------|----------|
| NGC 3628 | 11h20m17.0s | +13°35′23″ | 843 km/s | 35 Mly |
| M66 (NGC 3627) | 11h20m15.0s | +12°59′30″ | 727 km/s | 35 Mly |
| M65 (NGC 3623) | 11h18m56.0s | +13°05′32″ | 807 km/s | 35 Mly |

## 📚 References

- [1] NASA/IPAC Extragalactic Database (NED)
- [2] NOIRLab image noao-ngc3628
- [3] ESO VST observations (eso1043)
- [4] Garcia 1993 (LGG 231)
- [5] Arp 1966 (Arp 317)

## 🚀 Usage

```python
python leo_triplet_3d.py
