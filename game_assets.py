# Asset
# ├── Building
# │   ├── Tower
# │   │   ├── Tower
# │   │   └── Tower + electricity
# │   │   └── Tower + fire
# │   │   └── Tower + toxic
# │   └── Castle
# │
# ├── Unit
# │   ├── Orc
# │   ├── Knight
# │   └── Archer
# │
# └── Effect
#     ├── Fire
#     ├── ToxicCloud
#     └── Lightning

class Asset:
    STYLE = """
classic hand-painted fantasy game artwork,
thick black outline around the main silhouette,
2D painted game asset,
traditional fantasy illustration aesthetic,
chunky stylized forms,
warm painterly surfaces,
softly exaggerated shapes,
rich but restrained colors,
visible brushwork,
organic painted texture,
simplified fantasy architecture.
dark charcoal-brown rather than pure black,
slightly irregular brush-painted edges,
natural hand-painted contour variation.
Use stronger contour definition around the outer silhouette,
while keeping most internal edges softer and painterly.
"""

    NEGATIVE = """
anime, manga, comic-book ink, vector art,
3D render, CGI, PBR, photorealism,
glossy 3D surfaces, plastic materials,
extreme contrast, neon colors, hard cel shading
"""

    SUBJECT = ""
    FEATURES = ""
    CAMERA = ""
    COMPOSITION = ""

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def namelvl(self):
        return self.__class__.__name__

    def subject(self):
        return self.SUBJECT

    def prompt(self):
        return f"""
{self.STYLE}

SUBJECT:
{self.subject()}

KEY FEATURES:
{self.FEATURES}

CAMERA:
{self.CAMERA}

COMPOSITION:
{self.COMPOSITION}
""".strip()


# ======================
#
class Building(Asset):
    def __init__(self, level: int):
            self.level = level

    @property
    def namelvl(self):
        return self.__class__.__name__ + "Lvl" + str(self.level)

    def subject(self):
        return self.SUBJECT[self.level]

    CAMERA = """
elevated three-quarter view,
slightly above the subject,
isometric-inspired perspective
"""

    COMPOSITION = """
single isolated building,
centered,
full silhouette visible,
clean white background
"""

# ======================
#
class Unit(Asset):

    CAMERA = """
three-quarter character view,
slightly elevated viewpoint,
full body visible
"""

    COMPOSITION = """
single isolated character,
centered,
clear silhouette,
clean white background
"""

# ======================
#
class Effect(Asset):

    CAMERA = """
clear view of the complete effect,
appropriate three-quarter or elevated perspective
"""

    COMPOSITION = """
single isolated magical effect,
fully visible,
centered,
clean simple background
"""

    EFFECT_STYLE = """
dynamic organic painted shapes,
layered overlapping forms,
soft translucent edges,
clear directional movement,
painted energy and atmospheric texture
"""

    def prompt(self):
        return super().prompt() + "\n\n" + self.EFFECT_STYLE


# =========================
#
class ArcherTower(Building):

    SUBJECT={
        1:"""
A small makeshift medieval defensive barricade.
The structure is acrude semi-circular breastwork
built upon a low elevated dirt mound,
loosely stacked irregular fieldstones and thick rough-hewn wooden logs,
a simple gap-opening for access at the rear,
an elevated wooden platform on timber stilts rising behind the stone wall,
a single ragged blank cloth flag hanging from a wooden post.
""",
        2:"""
A small makeshift medieval defensive barricade.
The structure is acrude semi-circular breastwork
built upon a low elevated dirt mound,
loosely stacked irregular fieldstones and thick rough-hewn wooden logs,
a simple gap-opening for access at the rear,
an elevated wooden tower on timber stilts rising behind the stone wall,
a single ragged blank cloth flag hanging from a wooden post.
""",
        3:"""
A small medieval stone archer tower.
The tower is a compact cylindrical stone fortress with thick chunky masonry,
large irregular individual stone blocks,
a rounded wooden doorway at the front,
sturdy battlements and crenellations at the top,
and two blue heraldic cloth banners hanging from the sides.
""",
        4:"""
A medieval stone archer tower with a large spherical wooden roof covering the entire tower.
The tower is a compact cylindrical stone fortress with thick, chunky masonry
and large irregular stone blocks.
A small wooden side tower is attached directly to one side.
A rounded wooden doorway faces the front,
with large blue heraldic cloth banners hanging from the sides.
""",
        5:"""
A fully upgraded medieval stone archer tower with a massive spherical wooden roof covering the entire tower.
The compact cylindrical fortress has thick reinforced masonry,
large irregular stone blocks, additional defensive walls and platforms,
and a small fortified side tower attached directly to one side.
Multiple wooden supports, battlements and blue heraldic banners add detail.
A rounded wooden doorway faces the front.""",
        '5-fire':"""
A fully upgraded medieval stone archer tower with a massive spherical red wood roof covering the entire tower.
The compact cylindrical fortress has thick reinforced masonry,
large irregular stone blocks, additional defensive walls and platforms,
and a small fortified side tower attached directly to one side.
The tower is infused with magical fire, with glowing flames and fiery elements integrated into its architecture.
Multiple wooden supports, battlements and blue heraldic banners add detail.
""",
        '5-poison':"""
A fully upgraded medieval stone archer tower with a massive spherical green wood roof covering the entire tower.
The compact cylindrical fortress has thick reinforced masonry,
large irregular stone blocks covered in extensive toxic corrosion,
with deep eroded grooves,
pitted surfaces and spreading poisonous stains,
additional defensive walls and platforms,
and a small fortified side tower attached directly to one side.
The tower is infused with magical poison, with glowing toxic elements and poisonous details integrated into its architecture.
Multiple wooden supports, battlements and blue heraldic banners add detail.
"""
    }
    FEATURES="""
warm beige and gray medieval stone,
slightly weathered masonry,
dark brown wood,
muted blue cloth,
dark steel details,
subtle moss and small patches of grass around the bottom,
painted material variation and edge highlights.
"""

# =========================
#
class HandTower(Building):

    SUBJECT={
            1:"""
A fantastical tower formed entirely from a gigantic human hand emerging from the ground.
The wrist and forearm form a broad, solid foundation.
The palm faces upward, with a large magical fireball blazing directly above its center.
Five thick, chunky, slightly curved fingers surround the fireball.
The hand itself IS the tower architecture, not a statue holding a structure.
"""
    }
    FEATURES = """
deep black stone masonry,
slightly weathered surface,
ornate metallic gold trim and accents,
dark charcoal shadows,
subtle painted texture and warm highlights.
"""