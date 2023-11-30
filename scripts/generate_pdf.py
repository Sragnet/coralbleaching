#!/bin/python3

# Takes 2 arguments:
# 1. file path
# 2. name of path of export file excluding extension (as extension may vary)

import subprocess, os, shutil, sys

if len(sys.argv) > 1:
    input_name = sys.argv[1]
    output_name = ".".join(input_name.split(".")[:-1]) if len(sys.argv) < 3 else sys.argv[2]
    print("Generating PDF...")
    nf = output_name + ".pdf"
    p = subprocess.run(["jupyter", "nbconvert", "--to", "pdf", "--output", output_name + ".pdf", input_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if p.returncode != 0:
        print("Failed to generate PDF, falling back to HTML")
        p = subprocess.run(["jupyter", "nbconvert", "--to", "html", "--output", output_name + ".html", input_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        nf = output_name + ".html"
    if os.path.isdir("nbconvert"):
        shutil.rmtree("nbconvert")
    if p.returncode == 0:
        print(f"{nf} generated")
    else:
        print("Failed to generate file")
else:
    print("Usage: python3 generate_pdf.py <input_file> [output_file_no_extension]")