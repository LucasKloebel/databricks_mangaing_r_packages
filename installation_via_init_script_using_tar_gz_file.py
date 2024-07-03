# Databricks notebook source
# MAGIC %md
# MAGIC #### Installation of R packages via init-script using tar.gz-file
# MAGIC
# MAGIC Code was executed on Databricks runtime with ML 15.3
# MAGIC
# MAGIC Additional requirements:
# MAGIC - Unity catalog (Databricks Premium or above)
# MAGIC - managed volume

# COMMAND ----------

# MAGIC %md
# MAGIC To install a specific version of a package cluster-scoped using an init script, download the specific version of the package from CRAN ot the CRAN Archive, upload it to the volume, and then install it using an init script. 
# MAGIC
# MAGIC CRAN: https://cran.r-project.org/web/packages/available_packages_by_date.html
# MAGIC CRAN Archive: https://cran.r-project.org/src/contrib/Archive
# MAGIC

# COMMAND ----------

## Define contents of script 
script = """
#!/bin/bash
R --vanilla <<EOF

install.packages("/Volumes/volume01/example_usecases/packages/data.table_1.15.2.tar.gz", type = "source", repos = NULL, dependencies = TRUE)

q()
EOF
"""

## Save the script to Volume
dbutils.fs.put("/Volumes/volume01/example_usecases/init_scripts/init_script1.sh", script, True)

# COMMAND ----------

# MAGIC %md
# MAGIC Now go to the left pane and click on "Compute", then click on your cluster, and select "Edit". Under "Advanced options", go to "Init Scripts". Choose "Volumes" under "Source" and navigate to the folder where init_script1.sh was written.
# MAGIC
# MAGIC Now, every time you restart the cluster, the init script installs the packages cluster-scoped from the tar.gz file on the managed volume without the need to download them.
