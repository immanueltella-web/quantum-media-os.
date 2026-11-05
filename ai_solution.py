To fix the deterministic agent-card discovery regression, we need to ensure the `discover` method correctly returns the highest-ranked card based on the current cards.

**Step-by-step explanation:**
1. The `discover` method was returning the entire ranked list.
2. By modifying it to return the first element of the ranked list, it correctly selects the highest-ranked card.

Here is the corrected code:

```python
class DeterministicAgent:
    @classmethod
    def rank(cls, cards):
        return cls.ranked_cards

    def discover(self):
        return self.rank(self.cards)[0]
```