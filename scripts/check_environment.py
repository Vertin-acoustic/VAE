"""讲解者使用的环境体检；第 0 课不要求学习这段实现。"""

import importlib.metadata
import json
import sys
from pathlib import Path


def main():
    expected = Path(r"D:\Anaconda3\envs\HEUhuqiao\python.exe")
    actual = Path(sys.executable).resolve()
    if actual != expected.resolve():
        raise SystemExit(
            f"解释器不匹配。实际：{actual}\n请使用：{expected}"
        )

    import torch

    if not torch.cuda.is_available():
        raise SystemExit("解释器正确，但 CUDA 不可用；请先排查，暂不进行 GPU 实验。")

    # 实际运行卷积和反向传播，而不是只检测显卡是否存在。
    torch.manual_seed(0)
    layer = torch.nn.Conv2d(1, 4, kernel_size=3, padding=1).cuda()
    sample = torch.randn(2, 1, 16, 16, device="cuda")
    loss = layer(sample).square().mean()
    loss.backward()
    torch.cuda.synchronize()
    if not torch.isfinite(loss).item():
        raise RuntimeError("GPU 检查产生非有限损失。")
    if layer.weight.grad is None or not torch.isfinite(layer.weight.grad).all().item():
        raise RuntimeError("GPU 检查未得到有限梯度。")

    packages = [
        "torch", "torchvision", "numpy", "matplotlib", "ipykernel",
        "nbformat", "nbclient", "jupyter-client", "jupyter-server", "notebook",
    ]
    report = {
        "python": str(actual),
        "python_version": sys.version.split()[0],
        "packages": {name: importlib.metadata.version(name) for name in packages},
        "gpu": torch.cuda.get_device_name(0),
        "torch_cuda_build": torch.version.cuda,
        "gpu_forward_backward": "passed",
        "loss": loss.item(),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
