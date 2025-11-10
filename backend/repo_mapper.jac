// repo_mapper.jac - clone + file tree + readme summary


struct RepoMapper:
has clone_repo(url: str) -> str:
// calls Python helper
dir = py_module.git_tools.clone_repo(url)
return dir


has build_file_tree(repo_dir: str) -> list:
return py_module.git_tools.build_file_tree(repo_dir)


has summarize_readme(repo_dir: str) -> str:
return py_module.summarizer.summarize_readme(repo_dir)


has prioritise(file_tree: list) -> list:
// prioritize by common entrypoints
return py_module.git_tools.prioritise_files(file_tree)


export clone_repo = RepoMapper.clone_repo
export build_file_tree = RepoMapper.build_file_tree
export summarize_readme = RepoMapper.summarize_readme
export prioritise = RepoMapper.prioritise