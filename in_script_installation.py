# Databricks notebook source
# MAGIC %md
# MAGIC #### In-Script-Instalation of R packages
# MAGIC
# MAGIC Code was executed on Databricks runtime with ML 15.3
# MAGIC
# MAGIC Additional requirements:
# MAGIC None
# MAGIC

# COMMAND ----------

# MAGIC %r
# MAGIC # preinstalled package version
# MAGIC packageVersion("data.table")

# COMMAND ----------

# MAGIC %r
# MAGIC # install specific version of a package
# MAGIC devtools::install_version("data.table", version = "1.15.2")

# COMMAND ----------

# MAGIC %r
# MAGIC packageVersion("data.table")

# COMMAND ----------

# MAGIC %md
# MAGIC The package is now notebook-scoped and available. Once the cluster is terminated, restarted, or detached from the notebook, it is no longer available.
