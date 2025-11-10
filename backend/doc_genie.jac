// doc_genie.jac - assemble docs
struct DocGenie:
has generate(repo_dir: str, readme_summary: str, ccg_results: list) -> str:
out_path = py_module.summarizer.write_docs(repo_dir, readme_summary, ccg_results)
return out_path


export generate = DocGenie.generate
