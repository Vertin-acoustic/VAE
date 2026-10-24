"""第 3 课绘图工具：在独立进程绘图，不导入 torch，避免当前环境的 OpenMP 冲突。

由 Notebook 调用；参数依次为数据 JSON 路径、输出 PNG 路径。
这是讲解者搭好的工具，本课不要求学习其实现。
"""
import json
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # 只保存图片，不启动图形窗口。
import matplotlib.pyplot as plt


def main():
    data_path, figure_path = map(Path, sys.argv[1:])
    data = json.loads(data_path.read_text(encoding="utf-8"))
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3), layout="constrained")
    axes[0].semilogy(range(1, len(data["history"]) + 1), data["history"], color="#176b87")
    axes[0].set(title="Training loss (log scale)", xlabel="Epoch", ylabel="Mean batch MSE (kHz squared)")
    axes[1].plot(data["time"], data["initial"], label="Before training", color="#999999", linestyle=":")
    axes[1].plot(data["time"], data["final"], label="After training", color="#176b87", linewidth=3)
    axes[1].plot(data["time"], data["target"], label="Target", color="#de8c36", linestyle="--")
    axes[1].set(title="Frequency curve", xlabel="Time (s)", ylabel="Frequency (kHz)")
    for ax in axes:
        ax.grid(alpha=0.2)
    axes[1].legend()
    fig.suptitle(f"SGD | learning rate = {data['learning_rate']} | epochs = {len(data['history'])}")
    figure_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(figure_path, dpi=150)
    plt.close(fig)
    print(figure_path)


if __name__ == "__main__":
    main()
