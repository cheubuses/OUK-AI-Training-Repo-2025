import ast
import os
from typing import Dict, List, Tuple, Optional


def parse_file(path: str) -> Optional[ast.AST]:
    """
    Parse a Python file and return its AST.
    Returns None if file doesn't end with .py or on error.
    """
    if not path.endswith(".py"):
        return None

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    tree = ast.parse(text)
    return tree


def _get_call_name(node: ast.Call) -> Optional[str]:
    """
    Try to obtain a readable name for a call node, e.g.
    - foo(...) -> "foo"
    - obj.method(...) -> "obj.method"
    - module.func(...) -> "module.func"
    Returns None for complex callables (lambda, subscripts, etc).
    """
    func = node.func
    if isinstance(func, ast.Name):
        return func.id
    if isinstance(func, ast.Attribute):
        parts = []
        cur = func
        # Walk attribute chain: a.b.c -> ["a", "b", "c"]
        while isinstance(cur, ast.Attribute):
            parts.append(cur.attr)
            cur = cur.value
        if isinstance(cur, ast.Name):
            parts.append(cur.id)
        parts.reverse()
        return ".".join(parts)
    return None


def build_ccg(ast_tree: ast.AST) -> Dict[str, List]:
    """
    Build a simple Code Context Graph (CCG) from a Python AST.
    Returns a dict with:
      - nodes: list of node names (functions, classes, module)
      - edges: list of (caller, callee) pairs representing calls.
    """
    nodes: List[str] = []
    edges: List[Tuple[str, str]] = []

    class CallVisitor(ast.NodeVisitor):
        def __init__(self):
            self.current_stack: List[str] = ["<module>"]

        def visit_ClassDef(self, node: ast.ClassDef):
            # Add the class itself
            if node.name not in nodes:
                nodes.append(node.name)
            # Visit its methods
            for child in node.body:
                if isinstance(child, ast.FunctionDef):
                    method_name = f"{node.name}.{child.name}"
                    if method_name not in nodes:
                        nodes.append(method_name)
            # Continue visiting inside
            self.generic_visit(node)

        def visit_FunctionDef(self, node: ast.FunctionDef):
            # Get function/method name
            name = node.name
            if name not in nodes:
                nodes.append(name)
            self.current_stack.append(name)
            self.generic_visit(node)
            self.current_stack.pop()

        def visit_Call(self, node: ast.Call):
            callee = _get_call_name(node)
            caller = self.current_stack[-1] if self.current_stack else "<module>"
            if callee:
                edges.append((caller, callee))
                if callee not in nodes:
                    nodes.append(callee)
            self.generic_visit(node)

    visitor = CallVisitor()
    visitor.visit(ast_tree)

    # Deduplicate while preserving order
    seen_nodes = []
    for n in nodes:
        if n not in seen_nodes:
            seen_nodes.append(n)

    seen_edges = []
    for e in edges:
        if e not in seen_edges:
            seen_edges.append(e)

    return {"nodes": seen_nodes, "edges": seen_edges}
