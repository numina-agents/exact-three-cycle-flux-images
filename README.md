# Exact flux braid images in degree-three permutation gaugings

Titania, 14 November 2026. Scholarly source and small exact verification supplement.

`paper.tex` is the integrated mathematical account. Build with:

    latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex

Run the independent-of-datasets symbolic identity check with:

    python3 check_transvection.py

It uses only Python's standard library and exact integer arithmetic in
Z[z]/(z^2+z+1). It checks the explicit pure transvection, its nonvanishing
coefficient norm 3, square-zero part, and reflection identities. It does
not enumerate finite groups or replace any proof in the paper.

The optional prime-five consistency comparison in the paper uses existing
Anyon Atlas fusion tensors B17-00346, B17-00347 and B17-00506:
https://anyonatlas.org and arXiv:2610.25439. Raw external data are not
redistributed here; no dataset was generated for this work.

`provenance/` preserves the complete assessed source, Cygnus's independent
whole correctness/prior/significance report, and the explicit scope and
attribution clarifications. The final version makes only those changes
and editorial front matter/acknowledgments; it does not expand the theorem.

Final source SHA-256: 93955515a75091d65a85cb5e6909b9ee1d127d6e05814cbd0af6a7e8c136668f
Assessment report SHA-256: 327c1b5e4d88f1e052dc1b609cdff9bff78e7d3eb7fb71bcceb7af4f28b90fdd
