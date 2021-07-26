"""
Contains ChimeraX script templates with placeholders to facilitate string formatting.
"""

tpl_main = """\

# Chimera X script to visualize the variants mapped to {id} downloaded from the AlphaFold Protein Structure Database.


# NOTE: to manually customize the details of the script, refer to the sections labeled with the OPTIONS keyword and modify
#     the line of code below accordingly.


# PDB code selection and assembly
# =====================================================

# open PDB file
open {pdb_file}



# General Settings
# =====================================================

# set lighting (OPTIONS: full, soft, simple)
lighting full

# set background (OPTIONS: white, black)
set bg white

# set up silhoutte outline (OPTIONS: true, false)
set silhouettes true

# set molecule style (OPTIONS: ball, sphere, stick)
style ball

# display ribbons if not already displayed (OPTIONS: show, hide)
show ribbons



# Variant Customization
# =====================================================

# color variant residues from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
color {variants} red


"""

tpl_test = """\
id: {id}
pdb_file: {pdb_file}
variants: {variants}
"""