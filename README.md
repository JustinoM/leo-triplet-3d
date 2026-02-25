# Leo Triplet 3D Visualization

An interactive 3D visualization of the **Leo Triplet** (M65, M66, NGC 3628), a famous group of interacting galaxies approximately 35 million light-years away [3].

## Features

- Astronomically-accurate positions based on RA/Dec and redshift data from the NASA/IPAC Extragalactic Database (NED) [1]
- Tidal tail of NGC 3628 correctly oriented to match NOIRLab imagery (extends east/north) [2]
- Earth perspective with viewer located at -Z looking toward the triplet
- Interactive zoom using mouse wheel
- Rotatable 3D view to explore spatial relationships
- Distance annotations showing separations between galaxies
- Constant-size Earth marker for scale reference

## Data Sources

| Galaxy | RA (J2000) | Dec (J2000) | Redshift | Apparent Magnitude |
|--------|------------|-------------|----------|-------------------|
| NGC 3628 | 11h20m17.0s | +13°35′23″ | 843 ± 1 km/s | 9.5 [6] |
| M66 (NGC 3627) | 11h20m15.0s | +12°59′30″ | 727 ± 3 km/s | 8.9 [6] |
| M65 (NGC 3623) | 11h18m56.0s | +13°05′32″ | 807 ± 3 km/s | 9.3 [6] |

*All RA/Dec/redshift data from NASA/IPAC Extragalactic Database (NED) [1]*

## Complete References

[1] NASA/IPAC Extragalactic Database (NED)
    California Institute of Technology. (2024). NASA/IPAC Extragalactic Database.
    For NGC 3628: https://ned.ipac.caltech.edu/byname?objname=NGC+3628
    For M66 (NGC 3627): https://ned.ipac.caltech.edu/byname?objname=MESSIER+066
    For M65 (NGC 3623): https://ned.ipac.caltech.edu/byname?objname=MESSIER+065
    Primary source for all RA/Dec/redshift data used in this visualization.

[2] NOIRLab/NSF. (2021). Galaxy NGC 3628 and its Tidal Tail (noao-ngc3628).
    Kitt Peak National Observatory, Mayall 4-meter Telescope.
    https://noirlab.edu/public/images/noao-ngc3628/
    Definitive image showing the tidal tail extending to the upper-left (North and East).

[3] European Southern Observatory (ESO). (2011). New ESO telescope looks at the Leo Triplet — and beyond.
    VST (Very Large Telescope Survey Telescope) observations.
    https://www.eso.org/public/news/eso1126/
    Also: Astronomy Magazine. https://www.astronomy.com/science/new-eso-telescope-looks-at-the-leo-triplet-and-beyond/
    Source for the 35 million light-year distance measurement.

[4] Garcia, A. M. (1993). General study of group membership. II – Determination of nearby groups.
    Astronomy and Astrophysics Supplement Series, Vol. 100, pp. 47-90.
    Bibcode: 1993A&AS..100...47G
    Group identification as LGG 231 (Lyons Groups of Galaxies Catalog).

[5] Arp, H. (1966). Atlas of Peculiar Galaxies.
    Astrophysical Journal Supplement, Vol. 14, pp. 1-20.
    Bibcode: 1966ApJS...14....1A
    DOI: 10.1086/190147
    Catalog identification as Arp 317 for NGC 3628's peculiar morphology.

[6] SEDS (Students for the Exploration and Development of Space). Messier 65, Messier 66, and NGC 3628.
    Messier Catalog and NGC Catalog.
    http://messier.seds.org/
    Source for apparent magnitudes and additional descriptive information.

## Additional References

- AstroPixels (Espenak, F., 2012). NGC 3628. Bifrost Astronomical Observatory.
  http://astropixels.com/galaxies/NGC3628-A01.html
  Amateur astronomy confirmation of tidal tail length (300,000 light-years).

- Wikipedia contributors. (2024). NGC 3628. In Wikipedia, The Free Encyclopedia.
  https://en.wikipedia.org/wiki/NGC_3628
  General reference and tidal tail length.

- Wikipedia contributors. (2024). Leo Triplet. In Wikipedia, The Free Encyclopedia.
  https://en.wikipedia.org/wiki/Leo_Triplet
  Group overview.

## Usage

Clone the repository and run:

git clone https://github.com/justino/leo-triplet-3d.git
cd leo-triplet-3d
pip install numpy matplotlib
python leo_triplet_3d.py

Use mouse wheel to zoom, click and drag to rotate view.

## Requirements

- Python 3.7+
- NumPy >= 1.20.0
- Matplotlib >= 3.5.0

## Acknowledgments

### Data Sources
- NASA/IPAC Extragalactic Database (NED) for fundamental astronomical data [1]
- NOIRLab/NSF for tidal tail imagery and orientation [2]
- European Southern Observatory (ESO) for VST observations and distance measurements [3]
- Garcia, A. M. for group catalog identification (LGG 231) [4]
- Arp, H. for peculiar galaxy catalog (Arp 317) [5]
- SEDS for Messier catalog information [6]

### Technical Assistance
- ChatGPT (OpenAI) for code refinement, documentation assistance, and debugging support
- DeepSeek for code revision, visualization improvements, and technical guidance
- Open Source Python Community for NumPy and Matplotlib libraries

### Individual Contributors
- Justino - Primary development and astronomical data integration

### Special Thanks
- The scientific community for maintaining open-access astronomical databases
- All contributors to the Python scientific computing ecosystem

## License

MIT License - See LICENSE file for details

## Author

Justino
Web: justino.info
Bluesky: @justino.info
GitHub: @justinoM
ORCID: 0000-0002-4749-0292

## Citation

If you use this visualization in your work, please cite:

Justino. (2026). Leo Triplet 3D Visualization. GitHub.
https://github.com/justinoM/leo-triplet-3d

Data sources:
[1] NASA/IPAC Extragalactic Database (NED)
[2] NOIRLab image noao-ngc3628
[3] ESO VST observations (eso1126)
[4] Garcia 1993 (LGG 231)
[5] Arp 1966 (Arp 317)
[6] SEDS Messier Catalog

AI Assistance:
- ChatGPT (OpenAI) - Code refinement and documentation
- DeepSeek - Code revision and visualization guidance

## Related Links

- NASA/IPAC Extragalactic Database: https://ned.ipac.caltech.edu/
- NOIRLab NGC 3628 Image: https://noirlab.edu/public/images/noao-ngc3628/
- ESO VST Leo Triplet: https://www.eso.org/public/news/eso1126/
- SEDS Messier Catalog: http://messier.seds.org/

## Tags

astronomy, galaxies, leo-triplet, 3d-visualization, matplotlib, python, astrophysics, ngc-3628, m66, m65, tidal-tail, data-visualization, space, ned, noirlab, eso, arp-317, lgg-231, messier-objects

---

Repository: https://github.com/JustinoM/leo-triplet-3d
Issues: https://github.com/justinoM/leo-triplet-3d/issues
License: CC-BY-NC-SA-4.0
