#------------------------------------------------------------------------
# 파이랜스 인텔리센스.
#------------------------------------------------------------------------
# bmesh.pyi
"""블렌더 내장 메쉬 모듈"""

from typing import Any
from mathutils import Matrix, Vector # type: ignore


class BMVert:
	co : Vector
	index : int
	hide : bool
	select : bool
	tag : bool

	def copy_from(self, other : BMVert) -> None:
		...

	def copy(self) -> BMVert:
		...

	def normal_update(self) -> None:
		...

	def select_set(self, value : bool) -> None:
		...

class BMEdge:
	verts : tuple[BMVert, BMVert]
	index : int
	hide : bool
	select : bool
	tag : bool
	seam : bool
	smooth : bool

	def calc_length(self) -> float:
		...

class BMFace:
	verts : list[BMVert]
	edges : list[BMEdge]
	index : int
	hide : bool
	select : bool
	tag : bool
	material_index : int
	normal : Vector

	def calc_area(self) -> float:
		...

	def calc_center_median(self) -> Vector:
		...

	def calc_center_bounds(self) -> Vector:
		...

	def normal_update(self) -> None:
		...

class BMesh:
	verts : list[BMVert]
	edges : list[BMEdge]
	faces : list[BMFace]

	def __init__(self) -> None:
		...

	def clear(self) -> None:
		...

	def copy(self) -> BMesh:
		...

	def free(self) -> None:
		...

	def transform(self, matrix : Matrix) -> None:
		...

	def normal_update(self) -> None:
		...

	def calc_volume(self, signed : bool = False) -> float:
		...

	def to_mesh(self, mesh : Any) -> None:
		...

	def from_mesh(self, mesh : Any) -> None:
		...

	def update_edit_mesh(self, mesh : Any, loop_triangles : bool = True, destructive : bool = True) -> None:
		...

	def select_flush_mode(self) -> None:
		...

def extrude_face_region(bm : BMesh, geom : list[Any], use_normal_flip : bool = False, use_normal_from_adjacent : bool = False) -> dict:
	...
