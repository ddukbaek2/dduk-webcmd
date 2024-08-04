#------------------------------------------------------------------------
# 파이랜스 인텔리센스.
#------------------------------------------------------------------------
# bpy.pyi
"""블렌더 내장 제어 모듈"""

from __future__ import annotations
from typing import Any, Iterator, Union, Optional
from mathutils import Vector, Matrix # type: ignore


class bpy_struct:
	"""블렌더의 최상위 기본 클래스"""
	...


class types:
	"""데이터 타입 목록"""
	...


	class Scene:
		"""씬 객체"""
		...

		objects : types.SceneObjects
		"""씬에 속한 오브젝트 목록"""
		...

		camera : types.Object
		"""카메라 오브젝트"""
		...

		collection : types.Collection
		"""컬렉션"""
		...
		

	class ID(bpy_struct):
		"""블렌더의 모든 데이터 블록 계열의 부모 클래스"""
		...

		name : str
		users : int
		use_fake_user : bool
		is_library_indirect : bool
		library : Optional[types.Library]
		def copy(self) -> types.ID: ...
		def user_clear(self) -> None: ...
		def user_remap(self, new_id : types.ID) -> None: ...
		def make_local(self) -> None: ...


	class Library(ID):
		"""라이브러리 데이터 블록 계열의 부모 클래스"""
		...
		filepath : str
		version : tuple[int, int, int]

	class Object(ID):
		"""계층구조 상의 오브젝트"""
		...

		# name : str
		location : Vector
		rotation_euler : Vector # tuple[float, float, float]
		scale : Vector # tuple[float, float, float]
		bound_box : list[Vector] # list[tuple[float, float, float]]
		matrix_world : Matrix
		
		def select_set(self, state : bool) -> None: ...
		def to_mesh(self, depsgraph : Any, apply_modifiers : bool) -> types.Mesh: ...


	class Camera(ID):
		"""카메라"""
		...

		lens : float
		sensor_width : float
		sensor_height : float

		def __init__(self, name : str) -> None: ...

	class Material(types.ID):
		"""재질"""
		...

		use_nodes : bool
		node_tree : Optional[types.NodeTree]


	class Node(bpy_struct):
		"""노드"""
		...

		name : str
		location : Vector # tuple[float, float]

	class NodeSocket(bpy_struct):
		"""노드소켓"""
		...

	class NodeLink(bpy_struct):
		"""노드링크"""
		...

		from_node : types.Node
		from_socket : types.NodeSocket
		to_node : types.Node
		to_socket : types.NodeSocket

	class Nodes(bpy_struct):
		"""노드 목록"""
		...

		def new(self, type : str) -> types.Node: ...
		def remove(self, node : types.Node) -> None: ...

	class NodeLinks:
		"""노드링크 목록"""
		...

		def new(self, from_socket : types.NodeSocket, to_socket : types.NodeSocket) -> types.NodeLink: ...
		def remove(self, link : types.NodeLinks) -> None: ...


	class NodeTree(types.ID):
		"""노드트리"""
		...

		nodes : types.Nodes
		links : types.NodeLinks

	class ContextObjects:
		"""컨텍스트에 속한 오브젝트 목록"""
		...

		def __len__(self) -> int: ...
		def __getitem__(self, key: Union[int, str]) -> types.Object: ...
		def __iter__(self) -> Iterator[types.Object]: ...

	class SceneObjects:
		"""씬에 속한 오브젝트 목록"""
		...

		def __len__(self) -> int: ...
		def __getitem__(self, key : Union[int, str]) -> types.Object: ...
		def __iter__(self) -> Iterator[types.Object]: ...
		def link(self, object : types.Object) -> None: ...
		def unlink(self, object : types.Object) -> None: ...
		def new(self, name: str, object_data : types.ID) -> types.Object: ...

	class Mesh:
		vertices : list[types.MeshVertex]
		edges : list[types.MeshEdge]
		polygons : list[types.MeshPolygon]


	class MeshVertex:
		co : Vector # tuple[float, float, float]


	class MeshEdge:
		vertices : Vector # tuple[int, int]


	class MeshPolygon:
		vertices : list[int]
		loop_indices : list[int]

	class Collection(types.ID):
		"""컬렉션"""
		...

		objects : list[types.Object]
		"""오브젝트 목록"""
		...

		children : list[types.Collection]
		hide_viewport : bool
		hide_render : bool

		def link(self, object : types.Object) -> None: ...
		def unlink(self, object : types.Object) -> None: ...


class WindowManager:
	"""윈도우매니저"""
	...

	def open_mainfile(self, filepath : str) -> None:
		""".blend 파일 불러오기"""
		...


class Ops:
	"""명령"""
	...

	wm : WindowManager
	"""윈도우매니저 객체"""
	...


class Context:
	"""현재 실행중인 블렌더 인스턴스의 컨텍스트 메모리"""
	...

	scene : types.Scene
	object : types.Object
	selected_objects : list[types.Object]
	selected_editable_objects : list[types.Object]
	objects : types.ContextObjects

class Cameras:
	"""카메라 데이터 블록 관련 메서드 목록"""
	...

	def new(self, name : str) -> types.Camera:
		"""새로운 카메라를 생성"""
		...

class Materials:
	"""재질 데이터 관련 메서드 목록"""
	...

	def new(self, name : str) -> types.Material:
		"""새로운 재질을 생성"""
		...

class Data:
	"""데이터 블록 관련 객체 목록"""
	...

	cameras : Cameras
	"""카메라 데이터 블록 관련 객체"""
	...

	materials : Materials
	"""재질 데이터 블록 관련 객체"""
	...

	objects : list[types.Object]
	"""오브젝트 객체"""
	...


data = Data()
"""데이터 블록 목록 객체"""
...

ops = Ops()
"""명령 목록 객체"""
...

context  = Context()
"""컨텍스트 객체"""
...