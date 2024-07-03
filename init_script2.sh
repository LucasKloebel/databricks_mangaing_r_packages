#!/bin/bash
R --vanilla <<EOF

new_lib_path <- "/Volumes/volume01/example_usecases/library"
.libPaths(c(new_lib_path, .libPaths()))

q()
EOF