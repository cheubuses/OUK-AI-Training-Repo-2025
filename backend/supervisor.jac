// supervisor.jac
import repo_mapper from "./repo_mapper.jac"
import code_analyzer from "./code_analyzer.jac"
import doc_genie from "./doc_genie.jac"


struct Supervisor:
has run_pipeline(url: str) -> dict:
// top-level orchestration
repo_dir = repo_mapper.clone_repo(url)
file_tree = repo_mapper.build_file_tree(repo_dir)
readme_summary = repo_mapper.summarize_readme(repo_dir)


// Pick high-priority files
targets = repo_mapper.prioritise(file_tree)


// Build CCGs for targets
ccg_results = []
for t in targets:
ccg = code_analyzer.build_ccg(repo_dir, t)
ccg_results.append(ccg)


// Generate final docs
docs_path = doc_genie.generate(repo_dir, readme_summary, ccg_results)


return {"success": true, "docs_path": docs_path}


has is_valid_repo(url: str) -> bool:
// simple check
return url.starts_with("http")




// Instantiate exported functions so main.jac can call
export run_pipeline = Supervisor.run_pipeline
export is_valid_repo = Supervisor.is_valid_repo