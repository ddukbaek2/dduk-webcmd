#------------------------------------------------------------------------
# 참조 모듈 목록.
#------------------------------------------------------------------------
from __future__ import annotations
from typing import Any, Final, Optional, Type, TypeVar, Union, List, Dict, Set, cast
import builtins
import unittest
import bpy
import bmesh # type: ignore
import os
from pyappcore.module_util import Node


#------------------------------------------------------------------------
# 전역 상수 목록.
#------------------------------------------------------------------------
SEMICOLON : str = ";"
CURRENTFILEPATH : str = os.path.abspath(__file__)
TESTSPATH : str = os.path.dirname(CURRENTFILEPATH).replace("\\", "/")
ROOTPATH : str = os.path.dirname(TESTSPATH).replace("\\", "/")
SRCPATH : str = f"{ROOTPATH}/src"


#------------------------------------------------------------------------
# 테스트 케이스.
#------------------------------------------------------------------------
class Test_ConversionModelValidator(unittest.TestCase):
	#------------------------------------------------------------------------
	# 테스트 : 출력.
	#------------------------------------------------------------------------
	def test_Print(self):
		builtins.print("__tests_main__")
		builtins.print("Test_ConversionModelValidator.test_Print()")

		node = Node.BuildTree(SRCPATH, None)
		modules = Node.GetModuleNames(node)
		for moduleFullName, moduleName in modules.items():
			packageName = moduleFullName.replace(moduleName, "")
			if moduleName.startswith("__"):
				continue
			if packageName.endswith("."):
				packageName = packageName[:-1]
			builtins.print(f"- package: {packageName}, module: {moduleName}")