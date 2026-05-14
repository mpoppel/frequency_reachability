"""
paper_style.py — shared matplotlib style for frequency_reachability paper.

Usage in any notebook or script:
    from paper_style import apply_paper_style, COLORS
    apply_paper_style()
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ── Colour palette ─────────────────────────────────────────────
COLORS = {
    "blue":   "#0066CC",
    "red":    "#CC0000",
    "green":  "#006600",
    "orange": "#FF6600",
    "purple": "#6600CC",
}

# Convenience aliases
BLUE   = COLORS["blue"]
RED    = COLORS["red"]
GREEN  = COLORS["green"]
ORANGE = COLORS["orange"]
PURPLE = COLORS["purple"]

# Approach-level color mapping used across all figures
APPROACH_COLORS = {
    "Fixed Unary":      RED,
    "Trainable Unary":  BLUE,
    "Fixed Ternary":    ORANGE,
    "Trainable Ternary": GREEN,
}


def apply_paper_style():
    """Apply the project-wide matplotlib style.
    Call once at the top of each notebook after imports.
    """
    plt.style.use("default")
    plt.rcParams.update({
        "text.usetex":          True,
        "font.family":          "serif",
        "font.serif":           ["Computer Modern Roman"],
        "font.size":            8,
        "axes.labelsize":       9,
        "legend.fontsize":      8,
        "xtick.labelsize":      8,
        "ytick.labelsize":      8,
        "axes.prop_cycle":      plt.cycler("color", list(COLORS.values())),
        "figure.facecolor":     "white",
        "axes.facecolor":       "white",
        "savefig.facecolor":    "white",
        "image.cmap":           "viridis",
    })


def boxplot_panel(ax, data_dict, colors, y_clip=(-2.0, 1.05),
                  show_ylabel=True, threshold=0.95):
    """Styled boxplot panel matching paper conventions.

    Parameters
    ----------
    ax          : matplotlib Axes
    data_dict   : dict {label: array_of_R2_values}
    colors      : list of hex color strings, one per condition
    y_clip      : (ymin, ymax) — values outside are clipped for display
    show_ylabel : whether to draw the y-axis label (False for right panels)
    threshold   : R² success threshold line (default 0.95)
    """
    labels    = list(data_dict.keys())
    positions = np.arange(1, len(labels) + 1)
    ymin, ymax = y_clip
    clipped   = [np.clip(v, ymin, ymax) for v in data_dict.values()]

    bp = ax.boxplot(
        clipped,
        positions=positions,
        patch_artist=True,
        widths=0.55,
        medianprops=dict(color="black", linewidth=2.0),
        whiskerprops=dict(linewidth=0.9),
        capprops=dict(linewidth=0.9),
        flierprops=dict(marker="o", markersize=2.5,
                        markerfacecolor="grey", alpha=0.5,
                        linestyle="none"),
        boxprops=dict(linewidth=0.9),
    )
    for patch, col in zip(bp["boxes"], colors):
        patch.set_facecolor(col)
        patch.set_alpha(0.70)

    ax.axhline(threshold, color="black", linestyle="--",
               linewidth=0.9, zorder=0,
               label=rf"$R^2\!=\!{threshold}$")
    ax.grid(True, alpha=0.5, linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(ymin - 0.45, ymax)
    ax.legend(loc="lower right", frameon=True,
              fancybox=False, shadow=False, fontsize=8)
    if show_ylabel:
        ax.set_ylabel(r"$R^2$ (test set)", fontsize=9, fontweight="bold")

    # Show true minimum for any clipped condition
    for i, lbl in enumerate(labels):
        true_min = np.min(data_dict[lbl])
        if true_min < ymin:
            ax.text(positions[i], ymin + 0.06,
                    rf"$\min\!=\!{true_min:.1f}$",
                    ha="center", va="bottom",
                    fontsize=6, color=colors[i], style="italic")


def approach_legend(fig, approaches=None, ncol=4, y=-0.03):
    """Add a shared approach legend below a multi-panel figure."""
    if approaches is None:
        approaches = list(APPROACH_COLORS.keys())
    patches = [
        mpatches.Patch(fc=APPROACH_COLORS[a], alpha=0.70,
                       ec="black", lw=0.8, label=a)
        for a in approaches
    ]
    fig.legend(handles=patches, loc="lower center", ncol=ncol,
               frameon=False, fontsize=8,
               bbox_to_anchor=(0.5, y))
