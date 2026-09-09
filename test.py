from databricks.sdk import WorkspaceClient

ws=WorkspaceClient(
    host="https:xxxxxxxxxxcloud.databricks.com",
    token="dapi14c0xxxxxxxxxx32ab95ebbd" 
) 

job_trigger = ws.jobs.run_now(job_id="1034334116677675")

while True:

    job_run = ws.jobs.get_run(job_trigger.run_id)
    if job_run.state.life_cycle_state in ["TERMINATED", "SKIPPED", "INTERNAL_ERROR"]:
        if job_run.state.result_state == "SUCCESS":
            print("Job completed successfully.")    
            break
        else:
            raise Exception(f"Job failed with state: {job_run.state.result_state}")

    time.sleep(5)  # Wait for 5 seconds before checking the job status again