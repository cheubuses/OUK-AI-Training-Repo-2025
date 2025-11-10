// code_analyzer.jac - parse files and construct a CCG


struct CodeAnalyzer:
has build_ccg(repo_dir: str, filepath: str) -> dict:
// Use py_module parser to parse and return edges/nodes
parsed = py_module.parser.parse_file(join(repo_dir, filepath))
ccg = py_module.parser.build_ccg(parsed)
return ccg


export build_ccg = CodeAnalyzer.build_ccg