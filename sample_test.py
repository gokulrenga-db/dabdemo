# Databricks notebook source

# COMMAND ----------

# MAGIC %sh
# MAGIC
# MAGIC mkdir -p "/Workspace${WORKSPACEBUNDLEPATH}/Validation/reports/junit/test-reports"

# COMMAND ----------

# Prepare to run pytest.
import sys, pytest, os

# Skip writing pyc files on a readonly filesystem.
sys.dont_write_bytecode = True

# Run pytest.
retcode = pytest.main([f"{os.getenv('WORKSPACEBUNDLEPATH')}/files/tests"])


# Fail the cell execution if there are any test failures.
assert retcode == 0, "The pytest invocation failed. See the log for details."