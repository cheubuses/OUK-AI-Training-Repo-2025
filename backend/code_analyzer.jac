walker code_analyzer {
    has file_path: str;
    has analysis_results: dict = {};

    can analyze_code(file_info: dict) -> dict {
        # file_info contains "file_name" and "content"
        content = file_info["content"]
        file_name = file_info["file_name"]

        # Example static analysis (lines of code)
        loc = py:eval(f"len('''{content}'''.split('\\n'))")
        result = {
            "file_name": file_name,
            "content": content,
            "lines_of_code": loc
        }
        print(f"Analyzed {file_name}")
        return result
    }
}
