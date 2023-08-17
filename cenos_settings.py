# all of the classes defined in the package that you'd like to cross-reference
classes = {"GeometryData", "TopoEntity"}

# default prefix for class cross-references
default_class_prefix = "cenos"

# other prefixes for class cross-references
class_prefix = {"TopoEntity": "cenos.topologyPy.TopoEntity"}

basic_types = {"int", "float", "str", "bytes", "bool"}

# location to inject typing string
typing_inject_location = "import __builtin__"
typing_header = """
from typing import Sequence,Tuple,Iterator
"""

# conversions from SWIG docstrings to RST docstrings
to_python_types = {
    "std::string": "str",
    "double": "float",
    "PyObject *": "object",
    "stringVector": "list[str]",
    "entityVector": "list[TopoEntity]",
    "stringVectorMap": "dict[str, list[str]]",
    "std::shared_ptr< GeometryData >": "GeometryData",
    "std::shared_ptr< TopoEntity >": "TopoEntity",
    "TopAbs_ShapeEnum": "TopAbs_ShapeEnum",
    "TopoDS_Edge const": "TopoDS_Edge",
    "std::map< std::string,std::vector< std::string > >::key_type const &": "str",
    "std::vector< std::string >::value_type": "str",
    "GroupVector": "list[Group]",
    "domainGroupVector": "list[DomainGroup]",
    "boundaryGroupVector": "list[BoundaryGroup]",
    "lumpedElementVector": "list[LumpedElement]",
    # "std::vector< std::shared_ptr< BoundaryGroup >,std::allocator< std::shared_ptr< BoundaryGroup > > >": "BoundaryGroup",
    # "std::shared_ptr< GeometryData >": "GeometryData",
}

to_python_type_hints = {
    "void": "None",
    "bool": "bool",
    "int": "int",
    "float": "float",
    "size_t": "int",
    "ptrdiff_t": "int",
    "json": "str",
    "std::vector< std::string,std::allocator< std::string > > *": "str",
    "SwigPyIterator": "Iterator",
    "swig::SwigPyIterator": "Iterator",
    "swig::SwigPyIterator *": "Iterator",
    "std::shared_ptr< DomainGroup >": "DomainGroup",
    "ShapeStats": "ShapeStats",
    "std::vector< std::shared_ptr< TopoEntity >,std::allocator< std::shared_ptr< TopoEntity > > >": "list[TopoEntity]",
    "std::vector< std::shared_ptr< TopoEntity >,std::allocator< std::shared_ptr< TopoEntity > > > *": "list[TopoEntity]",
    "std::shared_ptr< BoundaryGroup >": "BoundaryGroup",
    "TopoDS_Shape": "TopoDS_Shape",
    "std::vector< std::shared_ptr< DomainGroup >,std::allocator< std::shared_ptr< DomainGroup > > >": "list[DomainGroup]",
    "std::vector< std::shared_ptr< DomainGroup >,std::allocator< std::shared_ptr< DomainGroup > > > *": "list[DomainGroup]",
    "std::vector< double,std::allocator< double > >": "list[double]",
    "std::vector< TopoDS_Shape,std::allocator< TopoDS_Shape > >": "list[TopoDS_Shape]",
    "std::vector< gp_Pnt,std::allocator< gp_Pnt > >": "list[gp_Pnt]",
    "std::vector< std::shared_ptr< BoundaryGroup >,std::allocator< std::shared_ptr< BoundaryGroup > > >": "BoundaryGroup",
    "std::vector< std::shared_ptr< BoundaryGroup >,std::allocator< std::shared_ptr< BoundaryGroup > > > *": "BoundaryGroup",
    "std::vector< std::shared_ptr< TopoEntity > >::value_type const &": "list[TopoEntity]",
    "std::vector< std::shared_ptr< Group >,std::allocator< std::shared_ptr< Group > > >": "list[Group]",
    "std::vector< std::shared_ptr< Group >,std::allocator< std::shared_ptr< Group > > > *": "list[Group]",
    "std::vector< std::shared_ptr< LumpedElement >,std::allocator< std::shared_ptr< LumpedElement > > >": "list[LumpedElement]",
    "std::vector< std::shared_ptr< LumpedElement >,std::allocator< std::shared_ptr< LumpedElement > > > *": "list[LumpedElement]",
    "TopTools_ListOfShape": "TopTools_ListOfShape",
    "gp_Pln": "gp_Pln",
    "gp_Pnt": "gp_Pnt",
    "gp_Dir": "gp_Dir",
    "gp_Ax1": "gp_Ax1",
    "std::map< std::string,std::vector< std::string > >::mapped_type": "list[str]",
    "std::vector< std::shared_ptr< DomainGroup > >::value_type": "DomainGroup",
    "std::vector< std::shared_ptr< DomainGroup > >::value_type const &": "DomainGroup",
    "std::vector< std::shared_ptr< BoundaryGroup > >::value_type": "BoundaryGroup",
    "std::vector< std::shared_ptr< BoundaryGroup > >::value_type const &": "BoundaryGroup",
    "std::vector< std::shared_ptr< LumpedElement > >::value_type": "LumpedElement",
    "std::vector< std::shared_ptr< LumpedElement > >::value_type const &": "LumpedElement",
    "std::vector< std::shared_ptr< Group > >::value_type const &": "Group",
    "std::vector< std::shared_ptr< Group > >::value_type": "Group",
    "std::vector< std::shared_ptr< TopoEntity > >::value_type": "TopoEntity",
    "std::map< std::string,std::vector< std::string,std::allocator< std::string > >,std::less< std::string >,std::allocator< std::pair< std::string const,std::vector< std::string,std::allocator< std::string > > > > >": "dict[str, list[str]]",
    # "blubla": "BoundaryGroup",
    # "std::shared_ptr< GeometryData >": "GeometryData",
    # "std::shared_ptr< TopoEntity >": "TopoEntity",
    # "'std::vector< std::shared_ptr< DomainGroup >,std::allocator< std::shared_ptr< DomainGroup > > >'": "list[DomainGroup]",
}

"""SWIG's bindings of STL has a bunch of garbage"""
stl_to_python_type_hints = {
    "::size_type": "int",
    "::difference_type": "int",
    "::iterator": "Iterator",
    "::reverse_iterator": "Iterator",
    "::allocator_type": None,
}

to_python_defaults = {"NULL": "None"}
