import subprocess

from svgutils.compose import Panel, SVG, Text, Figure

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

fig_in = split_and_prepend_path("""
figures/bcr-mut-sel/ablang2-neighbor-csp.svg
figures/bcr-mut-sel/ablang2-vs-neutral.svg
figures/bcr-mut-sel/koenig_ablang_expression_reveal_2.svg
""")
fig_out = "fig1.svg"

make_figure("16cm", "16cm", 
        Panel(
              SVG(fig_in[0]).scale(0.18),
              Text("A", 2, 2, size=2, weight='bold')
             ),
        Panel(
              SVG(fig_in[1]).scale(0.105),
              Text("B", 0, 2, size=2, weight='bold')
             ).move(54, 0),
        Panel(
              SVG(fig_in[2]).scale(0.15),
              Text("C", 2, 2, size=2, weight='bold')
             ).move(0, 55),
        out_path=fig_out
        )