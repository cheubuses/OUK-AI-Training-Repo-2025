import os
import tempfile
import git
from pathlib import Path


def clone_repo(url: str) -> str:
	tmp = tempfile.mkdtemp(prefix="codebase_gen_")
	repo = git.Repo.clone_from(url, tmp)
	return tmp


def build_file_tree(repo_dir: str):
	tree = []
	for root, dirs, files in os.walk(repo_dir):
		# skip .git, node_modules
		dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__']]
		relative = os.path.relpath(root, repo_dir)
		for f in files:
			if f.endswith(('.py', '.jac', '.md', '.js', '.java')):
				tree.append(os.path.join(relative, f))
	return sorted(tree)


def prioritise_files(file_list):
	# simple heuristic: look for common entry points first
	priority = []
	entry_candidates = ['main.py', 'app.py', 'server.py', 'index.js', 'main.jac']
	for e in entry_candidates:
		for f in file_list:
			if f.endswith(e):
				priority.append(f)
	# append rest
	for f in file_list:
		if f not in priority:
			priority.append(f)
	return priority
    