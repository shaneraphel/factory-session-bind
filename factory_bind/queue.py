"""Worker-keyed factory jobs."""

TASKS: dict[str, list] = {}


def enqueue(job: dict, worker_id: str | None = None) -> None:
    if not worker_id:
        raise ValueError("factory job requires a worker id")
    TASKS.setdefault(worker_id, []).append(job)
