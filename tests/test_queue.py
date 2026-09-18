import pytest
from factory_bind.queue import TASKS, enqueue


def test_requires_worker():
    TASKS.clear()
    with pytest.raises(ValueError):
        enqueue({"step": 1})


def test_binds_worker():
    TASKS.clear()
    enqueue({"step": 1}, worker_id="w1")
    enqueue({"step": 2}, worker_id="w2")
    assert TASKS["w1"] == [{"step": 1}]
    assert TASKS["w2"] == [{"step": 2}]
