#--------------------------------------------------------------------------------
# 제목.
#--------------------------------------------------------------------------------
TITLE : dict = {
	1: "Texture error",
	2: "Texture name error",
	3: "Unit setup error",
	4: "Pivot error-Position",
	5: "Pivot error-Central axis",
	6: "Pivot error-Scale",
	7: "Pivot error-Rotation",
	8: "Clipping issue",
	9: "Mesh flip issue",
	10: "Mesh Group issue",
	11: "Polygon count error",
	12: "Polygon shape error",
	13: "Vertex error",
	14: "Edge error",
	15: "Face error",
	16: "Mesh error",
	17: "Animation data issue",
	18: "ID count error",
	19: "File format error",
	20: "File standard error-Zepeto",
	21: "File standard error-Altava",
	22: "Duplicated designs-Modeling",
	23: "Duplicated designs-Textures",
	24: "Included incorrect mesh",
}


#--------------------------------------------------------------------------------
# 내용.
#--------------------------------------------------------------------------------
DESC : dict = {
	1: "At least one of the Diffuse map or Basemap must be included.",
	2: "The texture name format is incorrect.",
	3: "The unit setup is incorrect.",
	4: "The position axis is not at (0,0,0).",
	5: "The object\"s central axis is not at (0,0,0).",
	6: "The scale axis is not at (100,100,100).",
	7: "The rotation axis is not at (0,0,0).",
	8: "There are overlapping parts between the costume mesh and the body mesh.",
	9: "Inverted mesh(s) exist.",
	10: "Grouped meshe(s) exist.",
	11: "The maximum number of polygons has been exceeded.",
	12: "Polygons other than triangles or quadrilaterals are included.",
	13: "There are disconnected vertices.",
	14: "There are disconnected edges.",
	15: "There are disconnected faces.",
	16: "There are holes in the mesh.",
	17: "It contains animation data.",
	18: "The number of ID maps has exceeded the limit (maximum of 20).",
	19: "The file format is incorrect.",
	20: "This is not a ZEPETO file standard. Select the [Zepeto to Roblox] tab to upload.",
	21: "This is not an Altava file standard. Please select the [Altava to Roblox/Snapchat] tab to upload.",
	22: "The file contains 3D modeling that has already been registered.",
	23: "The file contains textures that have already been registered.",
	24: "Your file contains mesh(es) with incorrect information.",
}


#--------------------------------------------------------------------------------
# 링크.
#--------------------------------------------------------------------------------
LINK : dict = {
	1: "https://docs.altava.com/creator-guide/modeling-guidelines/texture",
	2: "https://docs.altava.com/creator-guide/modeling-guidelines/texture",
	3: "https://docs.altava.com/creator-guide/modeling-guidelines/units-setup",
	4: "https://docs.altava.com/creator-guide/modeling-guidelines/reset-pivot",
	5: "https://docs.altava.com/creator-guide/modeling-guidelines/reset-pivot",
	6: "https://docs.altava.com/creator-guide/modeling-guidelines/reset-pivot",
	7: "https://docs.altava.com/creator-guide/modeling-guidelines/reset-pivot",
	8: "https://docs.altava.com/creator-guide/modeling-guidelines/clipping",
	9: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	10: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	11: "https://docs.altava.com/creator-guide/modeling-guidelines/polygon-count",
	12: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	13: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	14: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	15: "https://docs.altava.com/creator-guide/modeling-guidelines/mesh-check",
	16: "https://docs.altava.com/creator-guide/3d-modeling/low-polygons/topology",
	17: "https://docs.altava.com/creator-guide/3d-modeling/exporting",
	18: "https://docs.altava.com/creator-guide/3d-modeling/texturing/uv-mapping",
	19: "https://docs.altava.com/creator-guide/overview/overview",
	20: "https://docs.altava.com/creator-guide/overview/overview",
	21: "https://docs.altava.com/creator-guide/overview/overview",
	22: "https://docs.altava.com/creator-guide/overview/overview",
	23: "https://docs.altava.com/creator-guide/overview/overview",
	24: "https://docs.altava.com/creator-guide/making-3d-models/preparing-for-modeling",
}


#--------------------------------------------------------------------------------
# 카테고리.
#--------------------------------------------------------------------------------
CATEGORY : dict = {
    0: "dress",
    1: "outwear",
    2: "top",
    3: "pants",
    4: "skirt",
    101: "shoes",
    201: "bag",
    301: "headwear",
}


#--------------------------------------------------------------------------------
# 성별.
#--------------------------------------------------------------------------------
GENDER : dict = {
	1: "male",
	2: "female",
}


#--------------------------------------------------------------------------------
# 메타버스 타입.
#--------------------------------------------------------------------------------
METAVERSE : dict = {
    0: "altava",
    1: "zepeto",
    2: "clo",
}


#--------------------------------------------------------------------------------
# 메타버스 타입별, 기계검수 오류 처리 리스트
#--------------------------------------------------------------------------------
ERRORLIST : dict = {
	"altava" : [5,11,18,19,22,23,24],
	"zepeto" : [5,11,18,19,22,23,24],
	"clo" : [5,11,18,19,22,23,24],
}

#--------------------------------------------------------------------------------
# Position 오차값
#--------------------------------------------------------------------------------
PIVOT_POS_TOLERANCE_VALUE : float = 0.2


#--------------------------------------------------------------------------------
# Scale 오차값
#--------------------------------------------------------------------------------
SCALE_TOLERANCE_VALUE : float = 1e-4


#--------------------------------------------------------------------------------
# Rotate 오차값
#--------------------------------------------------------------------------------
ROTATE_TOLERANCE_VALUE : int = 1


#--------------------------------------------------------------------------------
# Pivot Check 예외처리 카테고리
#--------------------------------------------------------------------------------
EXCEPTION_PIVOT_CHECK : dict = {
	201: "bag",
    301: "headwear",
}


#--------------------------------------------------------------------------------
# Flip Dot 값
#--------------------------------------------------------------------------------
FLIP_DOT_VALUE : float = -0.935


#--------------------------------------------------------------------------------
# PolygonCount 예외처리 카테고리
#--------------------------------------------------------------------------------
EXCEPTION_POLYCOUNT_CHECK : dict = {
    101: "shoes",
    201: "bag",
    301: "headwear",
}


#--------------------------------------------------------------------------------
# 예외처리 Poly Count 값
#--------------------------------------------------------------------------------
EXCEPTION_POLYCOUNT_VALUE : int = 10000


#--------------------------------------------------------------------------------
# 기본 Poly Count 값
#--------------------------------------------------------------------------------
BASE_POLYCOUNT_VALUE : int = 20000


#--------------------------------------------------------------------------------
# UV IDS Map 제한 값.
#--------------------------------------------------------------------------------
LIMIT_UVMAP_COUNT : int = 200


#--------------------------------------------------------------------------------
# Texture Size 값
#--------------------------------------------------------------------------------
BASIC_TEXTURE_SIZE : int = 1024