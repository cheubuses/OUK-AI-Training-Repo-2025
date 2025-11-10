# main.jac
# This is the central walker orchestrating the backend


walker TaskManager {
    has repo_path: str = "";
    has code_files: list = [];
    has analysis_results: list = [];
    has documentation: dict = {};

    can map_repo(path: str) -> list {
        self.repo_path = path
        self.code_files = RepoMapper.map_repository(path)
        return self.code_files
    }

    can analyze_files() -> list {
        self.analysis_results = []
        for file in self.code_files:
            result = CodeAnalyzer.analyze_code(file)
            self.analysis_results.push(result)
        return self.analysis_results
    }

    can generate_documentation() -> dict {
        self.documentation = {}
        for result in self.analysis_results:
            doc = DocGenie.generate_docs(result["content"])
            self.documentation[result["file_name"]] = doc
        return self.documentation
    }

    can run_pipeline(path: str) -> dict {
        self.map_repo(path)
        self.analyze_files()
        return self.generate_documentation()
    }
}
