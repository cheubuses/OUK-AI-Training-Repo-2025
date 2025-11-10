# backend/helpers/summarizer.py
import os
from typing import List, Union

def summarize_readme(repo_dir: str) -> Union[str, List[str]]:
    """
    Return the first 10 lines of README if present, otherwise a "No README found" message.
    """
    candidates = ['README.md', 'README.MD', 'readme.md']
    for c in candidates:
        p = os.path.join(repo_dir, c)
        if os.path.exists(p) and os.path.isfile(p):
            with open(p, 'r', encoding='utf-8') as f:
                text = f.read()
            # TODO: replace this naive approach with an LLM summarizer
            lines = text.split('\n')
            return lines[:10]  # naive short summary as list of lines
    return "No README found"


def write_docs(repo_dir: str, readme_summary, ccg_results) -> str:
    """
    Write a generated docs.md file under <repo_dir>/outputs/docs.md and return the path.
    readme_summary may be a list of strings (lines) or a single string.
    ccg_results is expected to be a structure (e.g., list/dict) that can be stringified.
    """
    out_dir = os.path.join(repo_dir, 'outputs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'docs.md')

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('# Generated Documentation\n\n')

        f.write('## README summary\n\n')
        if isinstance(readme_summary, list):
            # write lines with blank-line separation for readability
            f.write('\n'.join(readme_summary))
            f.write('\n')
        else:
            f.write(str(readme_summary) + '\n')

        f.write('\n## CCG Results\n\n')
        # pretty-print ccg_results conservatively
        try:
            import json
            f.write(json.dumps(ccg_results, indent=2))
        except Exception:
            f.write(str(ccg_results))

    return out_path

