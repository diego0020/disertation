#! /bin/bash

convert_to_pdf () {
local pdf_name=`basename -s .svg $0`.pdf
echo cairosvg \"$0\" -o $pdf_name;
cairosvg "$0" -o "$pdf_name";
}
export -f convert_to_pdf
find . -name "*.svg" -execdir bash -c convert_to_pdf {} \;

