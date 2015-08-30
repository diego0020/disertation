# MRI structural image
mri = reader.get("IMAGE",119,"world",name="MRI")

# Free Surfer Label Map
aparc = reader.get("LABEL",119,"world",name="APARC")

# Right Thalamus model
r_tha = reader.get("MODEL",119,"world",name="right-thalamus")

# Now in talairach space
r_tha = reader.get("MODEL",119,"talairach",name="right-thalamus")

# Brain Stem Fibers
bs_fibs = reader.get("FIBERS",119,"talairach", checkpoints="brain-stem")

# Lerft Cortical Surface with thikcness scalars
cortex = reader.get("Surface",119,"talairach",hemi="l", scalar="thickness", name="pial")
