from typing import List
import ezdxf    #这是DXF解析库

from core.polygon import ContinuousPolygon


class DxfLoader:
    """
    负责：
    DXF 文件 → ContinuousPolygon 列表
    """

    def load(self, file_path: str) -> List[ContinuousPolygon]:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()

        polygons: List[ContinuousPolygon] = []

        # 处理 LWPOLYLINE
        for entity in msp.query("LWPOLYLINE"):
            if entity.closed:
                points = [(p[0], p[1]) for p in entity.get_points()]
                polygons.append(ContinuousPolygon(points))

        # 处理 POLYLINE
        for entity in msp.query("POLYLINE"):
            if entity.is_closed:
                points = [(v.dxf.location.x, v.dxf.location.y)
                          for v in entity.vertices]
                polygons.append(ContinuousPolygon(points))

        if not polygons:
            raise ValueError("No closed polygons found in DXF.")

        return polygons