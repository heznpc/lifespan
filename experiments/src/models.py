"""Provider-agnostic LLM interface for the direction-effect experiment.

The experiment design (``planning/drafts/experiment-direction-confound.md``)
is deliberately model-agnostic: it needs a *stronger* model ``S``, a *weaker*
model ``W``, and a *third* ``judge`` model disjoint from the debating pair.

This module defines the single seam every other script calls --- ``complete()``
--- and leaves the actual SDK wiring to the executor. It intentionally raises
``NotImplementedError`` until configured, so a stub is never mistaken for a
working call (no silent failure).

To wire it up, set the model IDs in ``MODEL_REGISTRY`` and implement
``_call_provider`` for your provider of choice.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

Role = Literal["strong", "weak", "judge"]

# Fill these with concrete model identifiers before running. Record the exact
# values in each run's manifest (run_direction.py does this automatically).
MODEL_REGISTRY: dict[Role, str] = {
    "strong": "",  # e.g. a frontier-tier model
    "weak": "",    # e.g. a smaller/older tier of the SAME family (reduces vendor confounds)
    "judge": "",   # a THIRD model, not in {strong, weak}
}


@dataclass
class Message:
    role: Literal["system", "user", "assistant"]
    content: str


@dataclass
class GenerationConfig:
    temperature: float = 1.0
    max_tokens: int = 2048
    seed: int | None = None  # vary across repeats; record per call


def _call_provider(model_id: str, messages: list[Message], cfg: GenerationConfig) -> str:
    """Single provider seam. Implement this for your SDK.

    Must return the assistant's text completion. Keep it pure (no global state)
    so runs are reproducible given (model_id, messages, cfg).
    """
    raise NotImplementedError(
        "Wire an LLM provider here (e.g. the Anthropic / OpenAI / Gemini SDK). "
        "This seam is intentionally unimplemented so the harness cannot silently "
        "fabricate results. See experiments/README.md."
    )


def complete(role: Role, system: str, user: str, cfg: GenerationConfig | None = None) -> str:
    """Resolve a role to a model and return its completion to (system, user)."""
    model_id = MODEL_REGISTRY.get(role, "")
    if not model_id:
        raise RuntimeError(
            f"MODEL_REGISTRY[{role!r}] is empty. Set concrete model IDs in models.py."
        )
    cfg = cfg or GenerationConfig()
    return _call_provider(model_id, [Message("system", system), Message("user", user)], cfg)
