# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
from genlayer import *

class EscrowDispute(gl.Contract):
    buyer: str
    seller: str
    spec: str
    deliverable: str
    status: str

    def __init__(self, seller_address: str, agreement_spec: str):
        self.buyer = str(gl.message.sender_address)
        self.seller = seller_address
        self.spec = agreement_spec
        self.deliverable = ""
        self.status = "OPEN"

    @gl.public.view
    def get_status(self) -> str:
        return self.status

    @gl.public.write
    def submit_work(self, work_link: str) -> None:
        self.deliverable = work_link
        self.status = "SUBMITTED"

    @gl.public.write
    def resolve_dispute(self) -> str:
        def nondet() -> str:
            task = (
                f"Does the deliverable '{self.deliverable}' satisfy the "
                f"spec '{self.spec}'? Reply with exactly one word: YES or NO."
            )
            result = gl.nondet.exec_prompt(task).strip().upper()
            return "YES" if "YES" in result else "NO"

        verdict = gl.eq_principle.strict_eq(nondet)

        if verdict == "YES":
            self.status = "RELEASED_TO_SELLER"
            return "Funds Released to Seller"
        else:
            self.status = "REFUNDED_TO_BUYER"
            return "Funds Refunded to Buyer"
