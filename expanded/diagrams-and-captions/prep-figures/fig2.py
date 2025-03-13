from compose_utils import split_and_prepend_path, make_figure
from svgutils.compose import Panel, SVG, Text

fig_in = split_and_prepend_path("""
figures/bcr-mut-sel/dasm-neighbor-csp.svg
figures/bcr-mut-sel/perplexity_comparison-v1rodriguez.svg
""")
fig_out = "fig2.svg"

make_figure("16cm", "16cm", 
        Panel(
              SVG(fig_in[0]).scale(0.19),
              Text("A", 2, 2, size=2, weight='bold')
             ),
        Panel(
              SVG(fig_in[1]).scale(0.19),
              Text("B", 0, 2, size=2, weight='bold')
             ).move(54, 0),
        out_path=fig_out
        )