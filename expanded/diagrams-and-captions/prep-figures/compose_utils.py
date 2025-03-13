import subprocess

from svgutils.compose import Figure

def split_and_prepend_path(fig_str, base_path="/Users/matsen/writing/talks/"):
    figs = fig_str.split()
    return [base_path + fig for fig in figs]

def reset_svg_bbox_inkscape(input_file, output_file):
    subprocess.run([
        "inkscape",
        input_file,
        "--export-area-drawing",
        "--export-filename=" + output_file
    ], check=True)

def make_figure(*argv, out_path):
    fig = Figure(*argv)
    fig.save(out_path)
    reset_svg_bbox_inkscape(out_path, out_path)