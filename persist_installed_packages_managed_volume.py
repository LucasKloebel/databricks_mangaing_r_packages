# Databricks notebook source
# MAGIC %md
# MAGIC #### Persist installed packages on managed volume
# MAGIC
# MAGIC Code was executed on Databricks runtime with ML 15.3
# MAGIC
# MAGIC Additional requirements:
# MAGIC - Unity catalog (Databricks Premium or above)
# MAGIC - managed volume
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC .libPaths()

# COMMAND ----------

# MAGIC %r
# MAGIC packageVersion("data.table")

# COMMAND ----------

# MAGIC %r
# MAGIC # Append to the search path
# MAGIC .libPaths(c("/usr/lib/R/lib_current_usecase", .libPaths()))
# MAGIC # Check if new libPath is correctly appended
# MAGIC .libPaths()

# COMMAND ----------

# MAGIC %r
# MAGIC # Now when installing a package via devtools, the packages is installed into this path
# MAGIC devtools::install_version("data.table", version = "1.15.2", lib = "/usr/lib/R/lib_current_usecase")
# MAGIC ## Copy to Volume
# MAGIC system("cp -R /usr/lib/R/lib_current_usecase /Volumes/volume01/example_usecases/library_usecase1", intern = T)

# COMMAND ----------

## Define contents of script 
script = """
#!/bin/bash
R --vanilla <<EOF

new_lib_path <- "/Volumes/volume01/example_usecases/library"
.libPaths(c(new_lib_path, .libPaths()))

q()
EOF
"""

## Save the script to Volume
dbutils.fs.put("/Volumes/volume01/example_usecases/init_scripts/init_script2.sh", script, True)

# COMMAND ----------

# MAGIC %md
# MAGIC Now go to the left pane and click on "Compute", then click on your cluster, and select "Edit". Under "Advanced options", go to "Init Scripts". Choose "Volumes" under "Source" and navigate to the folder where init_script2.sh was written.
# MAGIC
# MAGIC Now, every time you restart the cluster, the managed volume path is appended to your libPaths, and the installed packages and their dependencies are available without needing to download or install them again.
