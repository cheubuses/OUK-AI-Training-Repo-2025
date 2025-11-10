// main.jac - registers modules and exposes a walker to accept a repo URL
import supervisor from "./supervisor.jac"


// API walker called by HTTP POST requests
walker api_generate_docs( url: str ) -> str:
// Validate URL
if !supervisor.is_valid_repo(url):
return json.dumps({"success": false, "error": "invalid repo url"})


// Kick off the supervisor flow
res = supervisor.run_pipeline(url)
return json.dumps(res)