#这是一份根据项目骨架创建文件夹的代码
#导入pathlib库是专门负责系统路径的，比直接导入OS 要好
from pathlib import Path

project_structure = {
# 数据层：存储实验数据，存储原始SXF文件，存储零件处理后的边界连续值
    "data": {
        "experiments": {},
        "boards": {},
        "parts": {},
        "raw_dxf": {}
    },
# 核心算法层：几何体从DXF到连续几何
    "core": [
        "geometry.py",
        "board.py",
        "part.py",
        "placement.py",
        "raster.py",
        "__init__.py"
    ],
#碰撞检测算法
    "collision": [
        "base.py",
        "pixel_detector.py",
        "continuous_detector.py",
        "distance_field.py",
        "__init__.py"
    ],
#读数据和存储数据
    "io": [
        "load.py",
        "save.py",
        "__init__.py"
    ],
#评价指标
    "metrics": [
        "utilization.py",
        "placed_ratio.py",
        "minimal_box.py",
        "__init__.py"
    ],
#零件摆放算法
    "algorithms": [
        "base.py",
        "bottom_left.py",
        "nfp_algorithm.py",
        "continuous_optimizer.py",
        "__init__.py"
    ],
#工作流
    "pipeline": [
        "coarse_runner.py",
        "refine_runner.py",
        "two_stage_runner.py",
        "__init__.py"
    ],
#可视化
    "visualization": [
        "plot_board.py",
        "plot_metrics.py",
        "__init__.py"
    ],
#辅助工具
    "utils": [
        "logger.py",
        "timer.py",
        "helpers.py",
        "__init__.py"
    ],
#实验配置
    "config": {}
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        #这是pathlib库的用法，两个路径中间用/分隔开
        path = base_path / name
        path.mkdir(parents=True, exist_ok=True)

        if isinstance(content, dict):
            create_structure(path, content)
        elif isinstance(content, list):
            for file in content:
                (path / file).touch()

if __name__ == "__main__":
    create_structure(Path("."), project_structure)
    print("✅ SDD2026 项目结构已创建完成")