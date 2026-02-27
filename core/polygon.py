from typing import List, Tuple
import math

Point = Tuple[float, float]


class ContinuousPolygon:
    """
    连续真值多边形（单位：mm）
    只负责几何表达与基础几何计算
    """

    def __init__(self, vertices: List[Point]):
        if len(vertices) < 3:
            raise ValueError("Polygon must have at least 3 vertices")

        self.vertices: List[Point] = vertices

    # =========================
    # 基础几何计算
    # =========================

    def area(self) -> float:
        """
        使用 Shoelace 公式计算面积
        """
        area = 0.0
        n = len(self.vertices)

        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1

        return abs(area) / 2.0

    def bounding_box(self):
        """
        返回 (min_x, min_y, max_x, max_y)
        """
        xs = [v[0] for v in self.vertices]
        ys = [v[1] for v in self.vertices]
        return min(xs), min(ys), max(xs), max(ys)

    # =========================
    # 变换操作（不修改自身，返回新对象）
    # =========================

    def translated(self, dx: float, dy: float):
        """
        平移，返回新的多边形
        """
        new_vertices = [(x + dx, y + dy) for x, y in self.vertices]
        return ContinuousPolygon(new_vertices)

    def rotated(self, angle_deg: float, origin: Point = (0, 0)):
        """
        绕 origin 旋转
        """
        angle_rad = math.radians(angle_deg)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        ox, oy = origin
        new_vertices = []

        for x, y in self.vertices:
            tx = x - ox
            ty = y - oy

            rx = tx * cos_a - ty * sin_a
            ry = tx * sin_a + ty * cos_a

            new_vertices.append((rx + ox, ry + oy))

        return ContinuousPolygon(new_vertices)

    # =========================

    def __repr__(self):
        return f"ContinuousPolygon(n={len(self.vertices)}, area={self.area():.2f})"