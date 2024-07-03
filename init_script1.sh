#!/bin/bash
R --vanilla <<EOF

install.packages("/Volumes/volume01/example_usecases/packages/data.table_1.15.2.tar.gz", type = "source", repos = NULL, dependencies = TRUE)

q()
EOF
