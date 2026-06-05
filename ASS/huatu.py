import matplotlib.pyplot as plt
import numpy as np
import os

# =========================
# Save Path
# =========================

save_dir = r"C:\Users\admin\Desktop\修改的ASS定稿"

# =========================
# Global Style
# =========================

plt.rcParams.update({
    "font.size": 12,
    "axes.labelsize": 13,
    "axes.titlesize": 14,
    "legend.fontsize": 11,
    "xtick.labelsize": 11,
    "ytick.labelsize": 11,
})

# Parameter sets
levels = ['Set-1', 'Set-2', 'Set-3']
x = np.arange(len(levels))
width = 0.34

# ==========================================================
# Figure 5: Runtime Comparison
# ==========================================================

signing = [0.047, 0.061, 0.098]
anamorphic_signing = [0.084, 0.278, 0.309]

fig, ax = plt.subplots(figsize=(7.2, 4.5))

bars1 = ax.bar(
    x - width/2,
    signing,
    width,
    edgecolor='black',
    linewidth=1.0,
    label='Dilithium'
)

bars2 = ax.bar(
    x + width/2,
    anamorphic_signing,
    width,
    edgecolor='black',
    linewidth=1.0,
    label='Anamorphic-Dilithium'
)

# Value labels
for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.006,
            f'{h:.3f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

ax.set_xticks(x)
ax.set_xticklabels(levels)

ax.set_ylabel('Running Time (s)')
ax.set_xlabel('Parameter Sets')

ax.set_ylim(0, 0.35)

ax.grid(axis='y', linestyle='--', alpha=0.6)

for spine in ax.spines.values():
    spine.set_linewidth(1.1)

ax.legend(frameon=True)

plt.tight_layout(pad=0.5)

# Save Figure 1
fig.savefig(
    os.path.join(save_dir, "Figure_1.png"),
    dpi=600,
    bbox_inches='tight'
)

plt.show()


# ==========================================================
# Figure 6: Key Storage Comparison
# ==========================================================

# Standard scheme: vpk + ssk
standard_keys = [
    1.281 + 2.469,
    1.906 + 3.906,
    2.531 + 4.750
]

# Anamorphic scheme: vpk + ssk + apk + ask
anamorphic_keys = [
    1.281 + 2.469 + 1.156 + 1.125,
    1.906 + 3.906 + 1.531 + 1.500,
    2.531 + 4.750 + 1.906 + 1.875
]

fig, ax = plt.subplots(figsize=(7.2, 4.5))

bars1 = ax.bar(
    x - width/2,
    standard_keys,
    width,
    edgecolor='black',
    linewidth=1.0,
    label='Dilithium'
)

bars2 = ax.bar(
    x + width/2,
    anamorphic_keys,
    width,
    edgecolor='black',
    linewidth=1.0,
    label='Anamorphic-Dilithium'
)

# Value labels
for bars in [bars1, bars2]:
    for bar in bars:
        h = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width()/2,
            h + 0.12,
            f'{h:.3f}',
            ha='center',
            va='bottom',
            fontsize=10
        )

ax.set_xticks(x)
ax.set_xticklabels(levels)

ax.set_ylabel('Total Key Storage (kb)')
ax.set_xlabel('Parameter Sets')

ax.set_ylim(0, 12)

ax.grid(axis='y', linestyle='--', alpha=0.6)

for spine in ax.spines.values():
    spine.set_linewidth(1.1)

ax.legend(frameon=True)

plt.tight_layout(pad=0.5)

# Save Figure 2
fig.savefig(
    os.path.join(save_dir, "Figure_2.png"),
    dpi=600,
    bbox_inches='tight'
)

plt.show()