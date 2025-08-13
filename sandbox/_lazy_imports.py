from __future__ import annotations
from typing import TYPE_CHECKING
import importlib


def setup_lazy_imports(
        base_globals: dict,
        module_map: dict[str, str], 
        setup_type_checking: bool = True) -> None:
    """
    UNUSED: Sets up lazy imports and type-checking imports for a package.
 
    Used in __init__.py files throughout sdatools to enable shortened
    imports, e.g. (from sdatools.distributions import NormalDistribution),
    whilst preventing circular imports at runtime.

    Read more about lazy imports: https://peps.python.org/pep-0690/

    Args:
        base_globals (dict): Pass in globals() from the calling module
        module_map (dict[str, str]): Mapping of class or module name -> module path string.
            e.g. {'NormalDistribution': 'sdatools.distributions.continuous.normal'}
        type_checking (bool): Whether to set up TYPE_CHECKING imports for IDEs.

    Example:
        # sdatools/foo/__init__.py
        from __future__ import annotations
        from sdatools.core._lazy_imports import setup_lazy_imports

        setup_lazy_imports(globals(), {
            'Bar1': 'sdatools.foo.abc.def.bar_1',
            'Bar2': 'sdatools.foo.ghi.jkl.bar_2',
            'Bar3': 'sdatools.foo.mno.pqr.bar_3',
        })

        # Now you can import modules using:
        # from sdatools.foo import Bar1, Bar2, Bar3
    """

    # Set public API list
    __all__ = base_globals.setdefault("__all__", [])
    __all__.extend(module_map.keys())

    # Immediate imports to support type checkers in IDEs
    if setup_type_checking:
        if TYPE_CHECKING: # True for static analysis tools, False at runtime
            for module_name, module_path in module_map.items():
                module = importlib.import_module(module_path)
                base_globals[module_name] = getattr(module, module_name)

    # Lazy imports for runtime
    def __getattr__(module_name):
        if module_name in module_map:
            module = importlib.import_module(module_map[module_name])
            obj = getattr(module, module_name)
            base_globals[module_name] = obj  # cache
            return obj
        raise AttributeError(f"Module {base_globals['__name__']} has no attribute {module_name}")
    
    base_globals["__getattr__"] = __getattr__
