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

# color protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
color bisque

# display atoms if not already displayed (OPTIONS: show, hide)
show surfaces; surface color bisque; transparency 90 surfaces



# Variant Customization
# =====================================================

# color silent variants from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
select :{silent}; color sel green; label sel height 1.5 size 68; ~select

# color missense variants from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
select :{missense}; color sel orange; label sel height 1.5 size 68; ~select

# color nonsense variants from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
select :{nonsense}; color sel red; label sel height 1.5 size 68; ~select

# color deletion variants from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
select :{deletion}; color sel midnight blue; label sel height 1.5 size 68; ~select

# color frameshift variants from the protein (OPTIONS: https://www.rbvi.ucsf.edu/chimerax/docs/user/commands/colornames.html)
select :{frameshift}; color sel dark violet; label sel height 1.5 size 68; ~select

"""

tpl_test = """\
id: {id}
pdb_file: {pdb_file}
silent: {silent}
missense: {missense}
nonsense: {nonsense}
deletion: {deletion}
frameshift: {frameshift}
"""