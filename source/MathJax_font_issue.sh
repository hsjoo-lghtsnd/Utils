#!/bin/bash
curl https://codeload.github.com/mathjax/MathJax/tar.gz/2.7.5 \
  | tar xz \
      --strip-components=6 \
      --directory=$CONDA_ENV_DIR/lib/python3.10/site-packages/notebook/static/components/MathJax/fonts/HTML-CSS/TeX/otf/ \
      MathJax-2.7.5/unpacked/jax/output/SVG/fonts/TeX