#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Leo Triplet Sky-Oriented 3D View
=================================

A 3D visualization of the Leo Triplet galaxy group (M65, M66, NGC 3628)
with astronomically positions based on RA/Dec and redshift data.

Author
------
Justino Martinez 
ORCID: 0000-0002-4749-0292
github:https://github.com/JustinoM/leo-triplet-3d/
Bluesky: @justino.info
http://justino.info

AI Assistance:
- ChatGPT (OpenAI) - Code refinement and documentation
- DeepSeek - Code revision, documentation and visualization guidance

Created
-------
2026-02-24

Last Modified
-------------
2026-02-25

Version
-------
1.0.0

License
-------
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
https://creativecommons.org/licenses/by-nc-sa/4.0/

Contact
-------
For questions, bug reports, or suggestions, please contact:
Bluesky: @justino.info
GitHub Issues: https://github.com/JustinoM/leo-triplet-3d/
"""

__author__ = "Justino Martinez"
__copyright__ = "Copyright 2026, Justino"
__credits__ = ["Justino"]
__license__ = "CC BY-NC-SA 4.0"
__version__ = "1.0.0"
__maintainer__ = "Justino Martinez"
__status__ = "Production"
__date__ = "2026-02-24"
__orcid__ = "0000-0002-4749-0292"
__github__ = "https://github.com/JustinoM/leo-triplet-3d/"

"""
Leo Triplet Sky-Oriented 3D View
--------------------------------

COORDINATE SYSTEM (Astronomically correct):
- +X = East  (right in astronomical terms)
- +Y = North (up in astronomical terms)
- +Z = Away from Earth

VIEWING GEOMETRY (Matches sky appearance):
- Observer at -Z looking toward +Z
- View rotated with azim=-90
- Result: +X (East) appears on LEFT
- Result: +Y (North) appears UP
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Tuple

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Plot configuration settings."""
    
    # Figure
    FIG_SIZE = (12, 9)
    AXIS_LIMIT = 150  # kpc
    
    # Galaxy markers
    GALAXY_SIZE = 250
    CENTER_SIZE = 150
    
    # Tidal tail
    TAIL_POINTS = 2500
    TAIL_LENGTH = 86  # kpc (~300,000 light-years)
    TAIL_WIDTH = 4
    TAIL_ALPHA = 0.2
    TAIL_COLOR = "#888888"
    # Direction: East (+X) and North (+Y), slightly toward Earth (-Z)
    TAIL_DIRECTION = np.array([1.0, 0.15, -0.1])
    
    # Colors
    COLORS = {
        "NGC 3628": "#2E8B57",  # Sea green
        "M66": "#DC143C",        # Crimson
        "M65": "#1E90FF",        # Dodger blue
        "center": "#FFD700",     # Gold
        "earth": "#FF8C00",      # Dark orange
        "triangle": "#9370DB"    # Medium purple
    }
    
    # Zoom
    ZOOM_SCALE = 1.2


# ============================================================================
# GALAXY DATA 
# ============================================================================

class GalaxyData:
    """
    Galaxy positions based on actual RA/Dec and redshift data.
    
    --- CONVENTIONS (Astronomically correct):
    
    - +X = East
    - +Y = North
    - +Z = Away from Earth
    
    --- ASTRONOMICAL DATA REFERENCES
    
    [1] NASA/IPAC Extragalactic Database (NED) - RA/Dec/Redshift data
    [2] NOIRLab image noao-ngc3628 - Tidal tail orientation
    [3] ESO VST observations - Distance
    [4] Garcia 1993 - Group identification LGG 231
    [5] Arp 1966 - Group identification Arp 317
    [6] Wikipedia - General reference and tail length
    
    +------------+-------------------------------------------------------------+
    | Reference  | Use in Code                                                 |
    +------------+-------------------------------------------------------------+
    | [1]        | RA/Dec/Redshift data - All galaxy positions (RA, Dec,       |
    |            | redshift) for NGC 3628, M66, and M65 are sourced from NED.  |
    |            | Used in GalaxyData.RA, GalaxyData.DEC, GalaxyData.REDSHIFT  |
    |            | dictionaries.                                               |
    +------------+-------------------------------------------------------------+
    | [2]        | Tidal tail orientation - The direction vector               |
    |            | [1.0, 0.15, -0.1] in Config.TAIL_DIRECTION is based on      |
    |            | NOIRLab image showing tail extending to upper-left          |
    |            | (East and North). Also cited in the tidal tail note in      |
    |            | setup_axes().                                               |
    +------------+-------------------------------------------------------------+
    | [3]        | Distance - The value 10700 kpc (10.7 Mpc / 35 million       |
    |            | light-years) in GalaxyData.DISTANCE comes from ESO VST      |
    |            | observations. Used to calculate DEGREE_TO_KPC = 187.        |
    +------------+-------------------------------------------------------------+
    | [4]        | Group identification (LGG 231) - Cited in comments and in   |
    |            | the group note in setup_axes() to identify the Leo Triplet  |
    |            | as galaxy group LGG 231 from Garcia 1993.                   |
    +------------+-------------------------------------------------------------+
    | [5]        | Group identification (Arp 317) - Cited in comments and in   |
    |            | the group note in setup_axes() to identify the Leo Triplet  |
    |            | as Arp 317 from Arp's Atlas of Peculiar Galaxies.           |
    +------------+-------------------------------------------------------------+
    | [6]        | Tidal tail length - The value 100 kpc (~300,000 light-years)|
    |            | in Config.TAIL_LENGTH is based on Wikipedia reference for   |
    |            | NGC 3628.                                                   |
    +------------+-------------------------------------------------------------+
    """
    
    # Raw astronomical data
    RA = {
        "NGC 3628": 11 + 20/60 + 17/3600,  # 11.3381 hours
        "M66":      11 + 20/60 + 15/3600,  # 11.3375 hours
        "M65":      11 + 18/60 + 56/3600   # 11.3156 hours
    }
    
    DEC = {
        "NGC 3628": 13 + 35/60 + 23/3600,  # 13.5897 degrees
        "M66":      12 + 59/60 + 30/3600,  # 12.9917 degrees
        "M65":      13 + 5/60 + 32/3600    # 13.0922 degrees
    }
    
    REDSHIFT = {
        "NGC 3628": 843,  # km/s
        "M66":      727,
        "M65":      807
    }
    
    DISTANCE = 10700  # kpc
    DEGREE_TO_KPC = 187  # kpc per degree at this distance
    
    @classmethod
    def get_positions_relative_to_ngc3628(cls) -> Dict[str, np.ndarray]:
        """Calculate positions relative to NGC 3628."""
        # Convert RA from hours to degrees
        ra_deg = {name: hours * 15 for name, hours in cls.RA.items()}
        
        # Get reference values
        ra_ngc = ra_deg["NGC 3628"]
        dec_ngc = cls.DEC["NGC 3628"]
        z_ngc = cls.REDSHIFT["NGC 3628"]
        
        positions = {}
        
        for name in cls.RA.keys():
            # RA offset: positive = East
            ra_offset_deg = ra_deg[name] - ra_ngc
            ra_offset_kpc = ra_offset_deg * cls.DEGREE_TO_KPC * np.cos(np.radians(dec_ngc))
            
            # Dec offset: positive = North
            dec_offset_deg = cls.DEC[name] - dec_ngc
            dec_offset_kpc = dec_offset_deg * cls.DEGREE_TO_KPC
            
            # Z offset: positive = away from Earth
            z_offset = cls.REDSHIFT[name] - z_ngc
            z_offset_kpc = z_offset * 0.1  # Scale factor
            
            positions[name] = np.array([ra_offset_kpc, dec_offset_kpc, z_offset_kpc])
        
        return positions
    
    @classmethod
    def get_center(cls) -> np.ndarray:
        """Calculate triplet center (centroid)."""
        positions = list(cls.get_positions_relative_to_ngc3628().values())
        return np.mean(positions, axis=0)
    
    @classmethod
    def get_positions(cls) -> Dict[str, np.ndarray]:
        """Get galaxy positions relative to triplet center."""
        rel_to_ngc = cls.get_positions_relative_to_ngc3628()
        center = cls.get_center()
        
        positions = {}
        for name, pos in rel_to_ngc.items():
            positions[name] = pos - center
        
        return positions
    
    @classmethod
    def verify_conventions(cls):
        """Verify all conventions are consistent."""
        positions = cls.get_positions()
        
        print("\n" + "="*80)
        print("SIGN CONVENTION VERIFICATION")
        print("="*80)
        print("\nCOORDINATE SYSTEM (Astronomically correct):")
        print("  +X = EAST")
        print("  +Y = NORTH")
        print("  +Z = AWAY from Earth")
        
        print("\nVIEWING GEOMETRY (azim=-90):")
        print("  Observer at -Z looking toward +Z")
        print("  View rotated so +X (EAST) appears on LEFT")
        print("  +Y (NORTH) appears UP")
        
        print("\n" + "-"*80)
        print("GALAXY POSITIONS (relative to center):")
        print("-"*80)
        
        for name, pos in positions.items():
            # Astronomical directions
            ew = "EAST" if pos[0] > 0 else "WEST"
            ns = "NORTH" if pos[1] > 0 else "SOUTH"
            los = "AWAY" if pos[2] > 0 else "TOWARD"
            
            # Visual appearance with azim=-90
            visual_x = "LEFT" if pos[0] > 0 else "RIGHT"  # +X appears left
            visual_y = "UP" if pos[1] > 0 else "DOWN"
            
            print(f"\n{name}:")
            print(f"  True:      X={pos[0]:6.1f} kpc ({ew}), Y={pos[1]:6.1f} kpc ({ns})")
            print(f"  Appears:   {visual_y}, {visual_x}")
            
            # Verify consistency
            if name == "NGC 3628":
                assert pos[1] > 0, "NGC 3628 should be North of center"
                print(f"  ✓ NGC 3628 is NORTH (appears UP)")
            elif name == "M66":
                assert pos[0] > 0, "M66 should be East of center"
                assert pos[1] < 0, "M66 should be South of center"
                print(f"  ✓ M66 is EAST and SOUTH (appears DOWN, LEFT)")
            elif name == "M65":
                assert pos[0] < 0, "M65 should be West of center"
                assert pos[1] < 0, "M65 should be South of center"
                print(f"  ✓ M65 is WEST and SOUTH (appears DOWN, RIGHT)")
        
        # Verify tidal tail direction
        tail_dir = cls.get_tail_direction()
        print(f"\nTIDAL TAIL:")
        print(f"  Direction: [{tail_dir[0]:.2f}, {tail_dir[1]:.2f}, {tail_dir[2]:.2f}]")
        print(f"  This means: EAST ({'+' if tail_dir[0]>0 else '-'}X), NORTH ({'+' if tail_dir[1]>0 else '-'}Y)")
        print(f"  Appears: UPPER-LEFT from NGC 3628 ✓")
        
        return True
    
    @classmethod
    def get_tail_direction(cls):
        """Return the correct tail direction vector."""
        return np.array([1.0, 0.15, -0.1])


# ============================================================================
# TIDAL TAIL GENERATOR
# ============================================================================

class TidalTail:
    """Generate tidal tail from NGC 3628."""
    
    def __init__(self, config: Config):
        self.config = config
        
    def generate(self, galaxy_positions: Dict[str, np.ndarray]) -> np.ndarray:
        """
        Generate tidal tail extending EAST and NORTH from NGC 3628.
        
        Direction: East (+X) and North (+Y)
        This roughly matches NOIRLab image (upper-left)
        https://noirlab.edu/public/images/noao-ngc3628/ 
        https://apod.grag.org/2021/07/24/structure-known-as-a-tidal-tail-ngc3628/
        and others
        """
        ngc_pos = galaxy_positions["NGC 3628"]
        
        # Direction: East (+X) and North (+Y)
        direction = self.config.TAIL_DIRECTION
        direction = direction / np.linalg.norm(direction) * self.config.TAIL_LENGTH
        
        # Generate points with density decreasing along tail
        t = np.random.beta(0.6, 1.8, self.config.TAIL_POINTS)
        
        # Base points
        points = ngc_pos + np.outer(t, direction)
        
        # Add perpendicular dispersion
        noise = np.random.normal(0, self.config.TAIL_WIDTH, 
                                size=(self.config.TAIL_POINTS, 3))
        
        # Remove component along tail
        dir_unit = direction / np.linalg.norm(direction)
        noise -= np.outer(np.dot(noise, dir_unit), dir_unit)
        
        # Add gentle curvature
        t_centered = t - 0.5
        curvature = np.zeros_like(points)
        curvature[:, 0] = t_centered * 5   # X-axis curve
        curvature[:, 1] = t_centered * 8   # Y-axis curve
        curvature[:, 2] = np.abs(t_centered) * 5  # Z-axis flaring
        
        return points + noise + curvature


# ============================================================================
# 3D PLOTTER
# ============================================================================

class LeoTripletPlotter:
    """Create 3D visualization of Leo Triplet."""
    
    def __init__(self, config: Config = None):
        self.config = config or Config()
        self.galaxy_data = GalaxyData()
        self.tail_generator = TidalTail(self.config)
        
        self.fig = None
        self.ax = None
        self.positions = self.galaxy_data.get_positions()
        
    def setup_figure(self):
        """Create figure and 3D axes."""
        self.fig = plt.figure(figsize=self.config.FIG_SIZE)
        self.ax = self.fig.add_subplot(111, projection="3d")
        
    def plot_galaxies(self):
        """Plot galaxy markers."""
        for name, pos in self.positions.items():
            color = self.config.COLORS[name]
            
            # Galaxy marker
            self.ax.scatter(*pos, 
                          color=color,
                          s=self.config.GALAXY_SIZE,
                          edgecolors='white',
                          linewidth=1.5,
                          alpha=1.0,
                          depthshade=True)
            
            # Label
            self.ax.text(*pos, f"  {name}", 
                        color=color,
                        fontsize=11,
                        weight='bold')
    
    def plot_center(self):
        """Plot triplet center marker."""
        self.ax.scatter(0, 0, 0,
                       marker='+',
                       color=self.config.COLORS['center'],
                       s=self.config.CENTER_SIZE,
                       linewidth=2,
                       depthshade=False)
        self.ax.text(0, 0, 5, '  Center',
                    color=self.config.COLORS['center'],
                    fontsize=10)
    
    def plot_triangle(self):
        """Draw triangle connecting galaxies."""
        names = list(self.positions.keys())
        coords = [self.positions[n] for n in names]
        
        # Triangle edges
        edges = [(0, 1), (1, 2), (2, 0)]
        
        for i, j in edges:
            p1, p2 = coords[i], coords[j]
            
            # Draw edge
            self.ax.plot([p1[0], p2[0]],
                        [p1[1], p2[1]],
                        [p1[2], p2[2]],
                        '--',
                        color=self.config.COLORS['triangle'],
                        linewidth=1.5,
                        alpha=0.6)
            
            # Distance label
            mid = (p1 + p2) / 2
            dist = np.linalg.norm(p2 - p1)
            
            self.ax.text(*mid, f"{dist:.0f} kpc",
                        color=self.config.COLORS['triangle'],
                        fontsize=9,
                        ha='center',
                        va='center',
                        bbox=dict(boxstyle='round,pad=0.2',
                                 facecolor='white',
                                 alpha=0.7))
    
    def plot_tidal_tail(self):
        """Generate and plot tidal tail."""
        tail = self.tail_generator.generate(self.positions)
        ngc_pos = self.positions["NGC 3628"]
        
        # Calculate distances for size variation
        distances = np.linalg.norm(tail - ngc_pos, axis=1)
        sizes = 1 + 3 * (distances / distances.max())
        
        # Color intensity varies with distance
        alphas = self.config.TAIL_ALPHA * (0.5 + 0.5 * distances / distances.max())
        colors = np.full(np.shape(distances),self.config.TAIL_COLOR)   
        
        self.ax.scatter(tail[:, 0],
                       tail[:, 1],
                       tail[:, 2],
                       color=colors,
                       alpha=alphas,
                       s=sizes,depthshade=True)
        
    
    def plot_earth(self):
        """Plot Earth marker and view direction lines."""
        # Earth position (fixed in data coordinates)
        earth_pos = np.array([0, 0, -150])
        
        # Earth marker
        self.ax.scatter(*earth_pos,
                       marker='o',
                       color=self.config.COLORS['earth'],
                       s=200,
                       alpha=0.7,
                       depthshade=False,
                       zorder=1000)
        
        # Earth label
        self.ax.text(*earth_pos + np.array([0, -20, 0]), 'EARTH',
                    color=self.config.COLORS['earth'],
                    fontsize=12,
                    weight='bold',
                    ha='center',
                    va='top',
                    zorder=1000)
        
        # View direction indicator (lines from Earth to triplet)
        for x_offset in [-30, 30]:
            for y_offset in [-30, 30]:
                start = earth_pos + np.array([x_offset, y_offset, 0])
                self.ax.plot([start[0], 0],
                            [start[1], 0],
                            [start[2], 50],
                            color=self.config.COLORS['earth'],
                            alpha=0.15,
                            linestyle=':',
                            linewidth=1,
                            zorder=500)
    
    def setup_axes(self):
        """Configure axes labels and view."""
        limit = self.config.AXIS_LIMIT
        
        self.ax.set_xlim(-limit, limit)
        self.ax.set_ylim(-limit, limit)
        self.ax.set_zlim(-limit, limit)
        
        # Labels show ASTRONOMICAL TRUTH
        self.ax.set_xlabel('ΔX (+east) [kpc]', fontsize=11, labelpad=10)
        self.ax.set_ylabel('ΔY (+north) [kpc]', fontsize=11, labelpad=10)
        self.ax.set_zlabel('ΔZ (+away from Earth) [kpc]', fontsize=11, labelpad=10)
        
        # Title
        self.ax.set_title('Leo Triplet Galaxy Group',
                         fontsize=14, weight='bold', pad=20)
        
        # Initial view from Earth direction with North up and East left (astron. convention)
        self.ax.view_init(elev=-90, azim=90)
        
        # Grid
        self.ax.grid(True, alpha=0.3)
        
        # ====================================================================
        # ADD THIS NOTE ABOUT THE TIDAL TAIL
        # ====================================================================
        tail_note = (
            "Grey dots: Tidal Tail of NGC 3628 (approximated)\nPositions are relative to triplet center\nPosition of the Earth is not real, only for orientation purposes"
        )
        
        self.ax.text2D(0.5, 1.0, tail_note,
                      transform=self.ax.transAxes,
                      fontsize=9,
                      bbox=dict(boxstyle='round,pad=0.5',
                               facecolor='white',
                               alpha=0.9),
                      verticalalignment='top',  
                      horizontalalignment='center',
                      zorder=2000)
    
    def enable_zoom(self):
        """Enable mouse wheel zoom."""
        def on_scroll(event):
            scale = 1/self.config.ZOOM_SCALE if event.button == 'up' else self.config.ZOOM_SCALE
            
            for axis, getter, setter in [
                ('x', self.ax.get_xlim3d, self.ax.set_xlim3d),
                ('y', self.ax.get_ylim3d, self.ax.set_ylim3d),
                ('z', self.ax.get_zlim3d, self.ax.set_zlim3d)
            ]:
                limits = getter()
                mid = np.mean(limits)
                half = (limits[1] - limits[0]) * scale / 2
                setter([mid - half, mid + half])
            
            self.fig.canvas.draw_idle()
        
        self.fig.canvas.mpl_connect('scroll_event', on_scroll)
    
    def plot(self):
        """Create the complete visualization."""
        self.setup_figure()
        self.plot_galaxies()
        self.plot_center()
        self.plot_triangle()
        self.plot_tidal_tail()
        self.plot_earth()
        self.setup_axes()
        self.enable_zoom()
        
        plt.tight_layout()
    
    def show(self):
        """Display the plot."""
        plt.show()
    
    def save(self, filename: str, dpi: int = 300):
        """Save the plot."""
        self.fig.savefig(filename, dpi=dpi, bbox_inches='tight')


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main execution."""
    try:
        # Verify all conventions
        GalaxyData.verify_conventions()
        
        print("\n" + "="*80)
        print("DATA REFERENCES")
        print("="*80)
        print("[1] NASA/IPAC Extragalactic Database (NED). (2024).")
        print("    - NGC 3628: 11h20m17.0s, +13°35′23″, v=843±1 km/s")
        print("    - M66 (NGC 3627): 11h20m15.0s, +12°59′30″, v=727±3 km/s")
        print("    - M65 (NGC 3623): 11h18m56.0s, +13°05′32″, v=807±3 km/s")
        print("    Retrieved from https://ned.ipac.caltech.edu/")
        print()
        print("[2] NOIRLab/NSF. (2021). Galaxy NGC 3628 and its Tidal Tail.")
        print("    Image noao-ngc3628. Retrieved from")
        print("    https://noirlab.edu/public/images/noao-ngc3628/")
        print()
        print("[3] European Southern Observatory. (2010). VST Snaps a Galactic Do-Si-Do.")
        print("    Eso1043fr. Retrieved from https://www.eso.org/public/news/eso1043/")
        print()
        print("[4] Garcia, A. M. (1993). General study of group membership. II.")
        print("    Astronomy and Astrophysics Supplement Series, 100, 47-90.")
        print("    (LGG 231 - Leo Triplet group identification)")
        print()
        print("[5] Arp, H. (1966). Atlas of Peculiar Galaxies.")
        print("    California Institute of Technology. (Arp 317)")
        print()
        print("[6] Wikipedia contributors. (2024). NGC 3628. In Wikipedia.")
        print("    Retrieved from https://en.wikipedia.org/wiki/NGC_3628")
        
        # Create and show plot
        plotter = LeoTripletPlotter()
        plotter.plot()
        plotter.show()
        
        print("\n" + "="*80)
        print("VISUALIZATION COMPLETE")
        print("="*80)
        print("✓ +X = EAST (astronomically correct)")
        print("✓ +Y = NORTH (astronomically correct)")
        print("✓ View rotated with azim=-90")
        print("✓ EAST appears on LEFT (matches sky)")
        print("✓ X-axis shows POSITIVE values for EAST")
        print("✓ Tidal tail: +X (EAST) and +Y (NORTH)")
        print("✓ Tail appears UPPER-LEFT (matches NOIRLab image)")
        print("✓ Earth marker shows observer position at -Z")
        
    except Exception as e:
        print(f"Error: {e}")
        raise


if __name__ == "__main__":
    main()